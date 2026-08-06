"""Exact saturation-depth law for the projective O12 reduction.

For a generic O12 block, projective coordinates satisfy

    beta != 0, alpha != beta, alpha != 1,

and every admissible pair (alpha, beta) has exactly q - 1 preimages under
the map from triples (c1, c2, c3).  Uniform generic-block sampling therefore
induces the uniform law on this two-dimensional domain.

The cumulative support at shell n is the union of circular intervals of
radius r = n + 1 centred on

    Z_{alpha,beta} = alpha * {-1, 0, 1} + beta * {-1, 0, 1}.

If g_max is the largest circular gap between the distinct centres, the first
saturated shell is exactly

    n_star = max(0, floor((g_max - 2) / 2)),

because radius-r discrete intervals cover Z/qZ iff g_max <= 2r + 1.
This script exhaustively enumerates the induced law without BFS, Weil
vectors, phases, Gram--Schmidt, or random sampling.
"""

from __future__ import annotations

import argparse

import numpy as np


def saturation_depths(q: int, chunk_size: int = 256) -> np.ndarray:
    """Return n_star for every admissible (alpha, beta), exactly once."""
    if q < 3:
        raise ValueError("q must be an odd prime")

    betas = np.arange(1, q, dtype=np.int64)
    depths = []
    signs = np.array([-1, 0, 1], dtype=np.int64)

    for alpha_start in range(0, q, chunk_size):
        alphas = np.arange(alpha_start, min(alpha_start + chunk_size, q), dtype=np.int64)
        aa, bb = np.meshgrid(alphas, betas, indexing="ij")
        admissible = (aa != 1) & (aa != bb)

        centres = (
            aa[..., None, None] * signs[None, None, :, None]
            + bb[..., None, None] * signs[None, None, None, :]
        ) % q
        centres = np.sort(centres.reshape(*aa.shape, 9), axis=-1)

        gaps = np.diff(centres, axis=-1)
        closing_gap = (centres[..., :1] + q) - centres[..., -1:]
        max_gap = np.concatenate((gaps, closing_gap), axis=-1).max(axis=-1)
        n_star = np.maximum(0, (max_gap - 2) // 2)
        depths.append(n_star[admissible])

    result = np.concatenate(depths)
    # For beta=1 the two exclusions alpha!=beta and alpha!=1 coincide.
    expected = (q - 1) + (q - 2) ** 2
    if result.size != expected:
        raise AssertionError(f"enumerated {result.size} pairs, expected {expected}")
    return result


def summarise(q: int, chunk_size: int = 256) -> None:
    depths = saturation_depths(q, chunk_size)
    quantiles = np.quantile(depths / q, [0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0])
    values = " ".join(f"{x:.6f}" for x in quantiles)
    # Nine centres have a circular gap of at least ceil(q/9).
    lower_bound = max(0, ((q + 8) // 9 - 2) // 2)
    print(
        f"q={q:5d} pairs={depths.size:9d} min={depths.min():4d} "
        f"median={np.median(depths):6.1f} max={depths.max():4d} "
        f"gap_lower_bound={lower_bound:d}"
    )
    print(f"  quantiles(n_star/q; 0,.1,.25,.5,.75,.9,1): {values}")
    tail_grid = [1 / 18, 0.06, 0.08, 0.10, 0.12, 0.15, 0.20, 0.25, 0.30, 0.40]
    tails = [np.mean(depths / q >= t) for t in tail_grid]
    labels = " ".join(f"{t:.6f}" for t in tail_grid)
    values = " ".join(f"{p:.6f}" for p in tails)
    print(f"  t:                   {labels}")
    print(f"  Pr(n_star/q >= t):   {values}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("q", nargs="*", type=int, default=[29, 53, 61, 101, 211, 401, 809])
    parser.add_argument("--chunk-size", type=int, default=256)
    args = parser.parse_args()
    for q in args.q:
        summarise(q, args.chunk_size)


if __name__ == "__main__":
    main()
