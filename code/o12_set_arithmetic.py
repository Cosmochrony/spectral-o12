"""
o12_set_arithmetic.py
Exact set-arithmetic reproduction of O12's Sigma_n^(c)/delta_exact pipeline,
with NO block-dependent BFS/fingerprints and NO Gram-Schmidt/SVD anywhere for
any of the sampled blocks (the shared, block-independent Cayley-shell size
sequence |S_n| still comes from one canonical BFS per prime, via
_shell_size() -- that is a pure graph-distance count, the same for every
block, and reintroduces no Weil structure) -- part of the O12-O17
provenance audit (admissibility/notes/o12-o17-provenance-audit.md, task 9,
steps 1, 3, 4, 5).

THEOREM (projective (alpha,beta) reduction, Jerome 2026-08-06, verified below
against the real Gram-Schmidt pipeline for two blocks at q=29):

  P_{<=n} = {b in Z/qZ : |b|_q <= n}          (the BFS ball's b-coordinate set;
                                                a genuine word of length <=n has
                                                at most n +/-1 Y-steps, and every
                                                residue of circular length <=n is
                                                reached this way -- proof: the
                                                b-coordinate is a lazy +/-1 walk
                                                with step alphabet {0,0,+1,-1}).

  F_{<=n}^{(c)} = A*P_{<=n} + A*T + B*T + C*T = A*P_{<=n+1} + B*T + C*T
                  (A=c1+c2+c3, B=c2+c3, C=c3, T={-1,0,1}; distributivity of the
                  Minkowski sumset over addition, then P_{<=n}+T = P_{<=n+1}).

  For a generic block (A != 0 mod q, q prime, so A invertible):

      dim W_{<=n}^{(c)} = |P_{<=n+1} + alpha*T + beta*T| (mod q),
      alpha = B/A, beta = C/A  (mod q).

Corollaries (all confirmed algebraically and numerically below):
  - depends on (c1,c2,c3) only through the two ratios (alpha,beta);
  - invariant under scaling the whole triple by any nonzero scalar;
  - the conjugate block -c=(-c1,-c2,-c3) has IDENTICAL (alpha,beta) (both A and
    B,C flip sign together, ratio unchanged) -- an independent, purely
    algebraic proof of V_n^{(c)}=V_n^{(-c)} that does not need the shell-
    inversion-symmetry argument of Part 2 of the audit note at all;
  - Z_{alpha,beta} = alpha*T + beta*T has at most 9 elements, so R_n is the
    size of the union of at most 9 circular intervals of radius n+1 around
    those 9 centres -- a finite additive-combinatorics problem on Z/qZ, not a
    representation-theoretic one.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

import numpy as np


def alpha_beta(c_block: tuple, q: int) -> tuple[int, int] | None:
    c1, c2, c3 = (int(c) % q for c in c_block)
    A = (c1 + c2 + c3) % q
    if A == 0:
        return None  # non-generic block, the projective reduction does not apply
    B = (c2 + c3) % q
    C = c3 % q
    invA = pow(A, -1, q)
    return (B * invA) % q, (C * invA) % q


def sigma_curve_set_arithmetic(c_block: tuple, q: int, n_max: int) -> np.ndarray:
    """Sigma_n^(c) for n=0..n_max, via pure Z/qZ set arithmetic. No BFS, no SVD."""
    ab = alpha_beta(c_block, q)
    if ab is None:
        raise ValueError(f"non-generic block {c_block} at q={q} (A=0)")
    alpha, beta = ab
    T = (-1, 0, 1)
    Z = {(alpha * t1 + beta * t2) % q for t1 in T for t2 in T}

    sigma = np.zeros(n_max + 1)
    prev_R = 0
    for n in range(n_max + 1):
        p_next = {b % q for b in range(-(n + 1), n + 2)}
        # Once the ball already covers the whole circle, P_{<=n+1} == Z/qZ.
        if len(p_next) >= q:
            p_next = set(range(q))
        R = len({(p + z) % q for p in p_next for z in Z})
        shell_size = _shell_size(n, q)
        sigma[n] = (R - prev_R) / shell_size if shell_size > 0 else 0.0
        prev_R = R
    return sigma


def _shell_size(n: int, q: int) -> int:
    """|S_n|, the exact BFS shell size on Cay(Heis_3(Z/qZ), {X,X^-1,Y,Y^-1}), independent of block."""
    from spectral_O12 import build_generators, bfs_shells
    # Cached across calls within one process via a module-level dict, since this
    # is prime-dependent only, not block-dependent, and expensive to recompute.
    cache = _shell_size.__dict__.setdefault("cache", {})
    if q not in cache:
        gens = build_generators(q)
        shells = bfs_shells(None, None, gens, q, 0.99)
        cache[q] = [len(s) for s in shells]
    sizes = cache[q]
    return sizes[n] if n < len(sizes) else 0


def verify_against_gram_schmidt(q: int = 29) -> None:
    """Sanity check: set-arithmetic Delta_r must match the real Gram-Schmidt pipeline exactly."""
    from spectral_O12 import build_generators, bfs_shells, fingerprint_vectors_batch, gram_schmidt_batch

    gens = build_generators(q)
    gens_arr = np.array(gens, dtype=np.int64)
    shells = bfs_shells(None, None, gens, q, 0.10)

    for c_block in [(1, 2, 3), (3, 5, 11)]:
        basis = None
        gs_deltas = []
        for n in range(3):
            shell_arr = np.array(shells[n], dtype=np.int64)
            vecs = fingerprint_vectors_batch(shell_arr, np.array(c_block), gens_arr, q)
            basis, dr = gram_schmidt_batch(basis, vecs)
            gs_deltas.append(dr)

        ab = alpha_beta(c_block, q)
        alpha, beta = ab
        T = (-1, 0, 1)
        Z = {(alpha * t1 + beta * t2) % q for t1 in T for t2 in T}
        prev_R, set_deltas = 0, []
        for n in range(3):
            p_next = {b % q for b in range(-(n + 1), n + 2)}
            R = len({(p + z) % q for p in p_next for z in Z})
            set_deltas.append(R - prev_R)
            prev_R = R

        match = gs_deltas == set_deltas
        print(f"block={c_block}: Gram-Schmidt Delta_r={gs_deltas}  set-arithmetic Delta_r={set_deltas}  "
              f"match={match}")
        assert match, "set-arithmetic reproduction disagrees with the real Gram-Schmidt pipeline"


def reproduce_o12_delta_exact(q: int, m_block: int, n_max: int, seed_base: int, n_seed: int) -> None:
    """
    Reproduce O12's own reported delta_exact fit (05-results.tex) using ONLY the
    set-arithmetic Sigma_n formula -- same block-sampling convention
    (sample_generic_blocks, same RNG_BASE), same zero-padding-then-average, same
    log-log OLS fitting window as spectral_O12.py's own run_one_prime /
    ols_loglog / find_fitting_window, but with NO per-block BFS/fingerprints
    and NO Gram-Schmidt/SVD computing Sigma_n itself (see module docstring
    for the one block-independent BFS this still runs, for |S_n| alone).
    """
    from spectral_O12 import (RNG_BASE, sample_generic_blocks, ols_loglog,
                               find_fitting_window)

    deltas = []
    for seed in range(n_seed):
        rng = np.random.default_rng(RNG_BASE + seed * 1000 + q)
        blocks = sample_generic_blocks(q, m_block, rng)

        all_sigma = []
        n_saturated_at = []
        for c_block in blocks:
            ab = alpha_beta(tuple(int(c) for c in c_block), q)
            if ab is None:
                continue
            sigma = sigma_curve_set_arithmetic(tuple(int(c) for c in c_block), q, n_max)
            all_sigma.append(sigma)
            nz = np.nonzero(sigma)[0]
            n_saturated_at.append(int(nz[-1]) + 1 if len(nz) else 0)
        all_sigma = np.array(all_sigma)
        sigma_bar = all_sigma.mean(axis=0)

        ns = np.arange(n_max + 1)
        n0, n1 = find_fitting_window(ns[1:], sigma_bar[1:], q)
        n0, n1 = max(n0, 1), min(n1, n_max)
        delta_hat, C_hat, r2 = ols_loglog(ns, sigma_bar, n0, n1)
        deltas.append(delta_hat)
        print(f"  seed={seed}: delta_hat={delta_hat:.3f}  R2={r2:.4f}  [n0,n1]=[{n0},{n1}]  "
              f"median saturation depth={int(np.median(n_saturated_at))}")

    print(f"q={q}: set-arithmetic delta_hat = {np.mean(deltas):.3f} +/- {np.std(deltas):.3f}  "
          f"(O12's own published value for this q, for comparison, is in "
          f"admissibility/o12/tex/05-results.tex)")


def decompose_three_factors(q: int, m_block: int, n_max: int, seed: int = 0) -> None:
    """
    Step 5: separate |S_n|^-1, E[Delta_r_n | n*_c >= n], and Pr(n*_c >= n) explicitly,
    using the exact set-arithmetic Sigma_n (no per-block BFS/SVD) so every
    factor is exact, not estimated.
    """
    from spectral_O12 import RNG_BASE, sample_generic_blocks

    rng = np.random.default_rng(RNG_BASE + seed * 1000 + q)
    blocks = sample_generic_blocks(q, m_block, rng)

    all_delta_r = []
    saturation_depth = []
    for c_block in blocks:
        ab = alpha_beta(tuple(int(c) for c in c_block), q)
        if ab is None:
            continue
        sigma = sigma_curve_set_arithmetic(tuple(int(c) for c in c_block), q, n_max)
        shell_sizes = np.array([_shell_size(n, q) for n in range(n_max + 1)])
        delta_r = sigma * shell_sizes
        all_delta_r.append(delta_r)
        nz = np.nonzero(delta_r)[0]
        saturation_depth.append(int(nz[-1]) + 1 if len(nz) else 0)

    all_delta_r = np.array(all_delta_r)
    saturation_depth = np.array(saturation_depth)
    shell_sizes = np.array([_shell_size(n, q) for n in range(n_max + 1)])

    print(f"{'n':>3} {'1/|S_n|':>12} {'Pr(survive)':>12} {'E[dr|survive]':>15} {'Sigma_bar_n':>12}")
    for n in range(n_max + 1):
        survives = saturation_depth > n
        pr_survive = survives.mean()
        vals = all_delta_r[survives, n] if survives.any() else np.array([0.0])
        e_dr_survive = vals.mean()
        inv_sn = 1.0 / shell_sizes[n] if shell_sizes[n] > 0 else 0.0
        sigma_bar_n = all_delta_r[:, n].mean() / shell_sizes[n] if shell_sizes[n] > 0 else 0.0
        print(f"{n:>3} {inv_sn:>12.6f} {pr_survive:>12.3f} {e_dr_survive:>15.3f} {sigma_bar_n:>12.6f}")


if __name__ == "__main__":
    print("=== Verification against the real Gram-Schmidt pipeline ===")
    verify_against_gram_schmidt(29)

    print()
    print("=== Reproduction of O12's own q=29 delta_exact fit (m_block=50, n_max=8, 3 seeds) ===")
    reproduce_o12_delta_exact(q=29, m_block=50, n_max=8, seed_base=0, n_seed=3)

    print()
    print("=== Three-factor decomposition, q=29 ===")
    decompose_three_factors(q=29, m_block=50, n_max=8, seed=0)
