"""
o12_bfs_truncation_check.py
Targeted check (task: O12 correction, pre-drafting control #2, Jerome 2026-08-06):
does the mid-shell-truncating bfs_shells() bug in the CANONICAL
admissibility/o12/code/spectral_O12.py (the same bug already found and fixed in
Q1's vendored copy -- see quantum-structure/notes/q1-central-theorem-audit.md)
actually corrupt any of O12's own published shells, i.e. shells[0..n_max] for
n_max in {8,11,10} at q in {29,53,61} (Table 3, 05-results.tex)?

bfs_shells(gens, q, max_fraction) stops -- possibly mid-shell -- once
max_fraction*q^3 nodes have been visited. Only the LAST shell it returns can
be partial: every earlier shell was appended in full because the while-loop
only proceeds to build the next shell in full when the running total is still
below max_nodes at the top of that iteration.

Method: for each published q, run the EXACT paper call
  bfs_shells(None, None, build_generators(q), q, 0.99)
and separately a bfs_frac=1.0 control run (truncates only at the true graph
diameter, i.e. as late as structurally possible). Report, for each n up to
n_max: the shell size from both runs. If they agree for all n <= n_max, the
published shells are untruncated and the bug is provably irrelevant to the
published numbers. If they first disagree at some n* <= n_max, the bug
affects shell n* and everything computed from it downstream (Sigma_n, the
OLS fit) for that prime.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from spectral_O12 import build_generators, bfs_shells  # noqa: E402

PAPER_N_MAX = {29: 8, 53: 11, 61: 10}


def check(q: int) -> None:
    n_max = PAPER_N_MAX[q]
    gens = build_generators(q)

    shells_paper = bfs_shells(None, None, gens, q, 0.99)
    shells_full = bfs_shells(None, None, gens, q, 1.0)

    print(f"=== q={q} (paper n_max={n_max}) ===")
    print(f"  bfs_frac=0.99 returned {len(shells_paper)} shells, "
          f"total nodes={sum(len(s) for s in shells_paper)} "
          f"(threshold={int(0.99*q**3)}, |group|={q**3})")
    print(f"  bfs_frac=1.00 returned {len(shells_full)} shells, "
          f"total nodes={sum(len(s) for s in shells_full)} "
          f"(threshold={int(1.00*q**3)}, |group|={q**3})")

    first_mismatch = None
    for n in range(0, min(len(shells_paper), len(shells_full), n_max + 5)):
        sp, sf = len(shells_paper[n]), len(shells_full[n])
        flag = "" if sp == sf else "  <-- MISMATCH"
        marker = " (used by paper)" if n <= n_max else ""
        print(f"    n={n:3d}: |S_n| paper-run={sp:6d}  full-run={sf:6d}{marker}{flag}")
        if sp != sf and first_mismatch is None:
            first_mismatch = n

    if first_mismatch is None:
        print(f"  RESULT: shells 0..{n_max} identical between bfs_frac=0.99 and 1.00. "
              f"The truncation bug does NOT affect any shell used in the published q={q} table.")
    elif first_mismatch > n_max:
        print(f"  RESULT: first mismatch at shell {first_mismatch} > n_max={n_max}. "
              f"The published q={q} table uses only complete shells; bug irrelevant to it.")
    else:
        print(f"  RESULT: first mismatch at shell {first_mismatch} <= n_max={n_max}. "
              f"The published q={q} table DOES use a truncated shell -- affected.")
    print()


if __name__ == "__main__":
    for q in (29, 53, 61):
        check(q)
