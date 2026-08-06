This repository contains the source of the **O12** Cosmochrony paper  
*Exact Weil-Block Projective Capacity on Heisenberg Graphs: Resolving the Final Obstruction to δ Extraction*.

This work extends the **spectral admissibility sub-programme** by replacing the
proxy-level Weil-block construction of **O11** with the **exact Weil projection**,
and by providing the first exact representation-level measurement of the projective
capacity decay exponent.

While **O11** established that the representation-level obstruction identified in
**O10** could be overcome at the proxy level, it left open the central question
of whether the exact metaplectic dynamics, including the central coordinate
$\gamma$ of the discrete Heisenberg group, would yield the same exponent.

The present work answers this question by introducing an **exact blockwise
projective capacity** based on the irreducible Weil blocks of the three-step
fingerprint on Heisenberg Cayley graphs.

The central observable is now the **exact incremental block capacity**
\[
\Sigma_n^{(c)} = \frac{\Delta r_n^{(c)}}{|S_n|},
\]
where $\Delta r_n^{(c)}$ is the rank increment contributed by shell $S_n$
inside an exact Weil block $H_c$.

# Core Result

The paper measures the exact Weil observable at $q\in\{29,53,61\}$, and separately derives
its intrinsic asymptotic exponent in closed form.

Starting from:

- the O7 capacity observable $\Sigma_n$
- the O9 Heisenberg graph setting
- the O10 diagnosis of dense representation failure
- the O11 proxy-level block construction
- the exact Weil representation including the central phase $\gamma$

the analysis shows that:

- a measurable pre-saturation decay regime is present already at accessible primes
- the exact mean block capacity satisfies $\bar\Sigma_n \sim C\,n^{-\hat\delta_{\mathrm{exact}}}$
  over a short but structurally meaningful fitting window, with fitted slopes:
    - $\hat\delta_{\mathrm{exact}} = 4.37 \pm 0.08$ at $q = 29$
    - $\hat\delta_{\mathrm{exact}} = 4.28$ at $q = 53$
    - $\hat\delta_{\mathrm{exact}} = 4.80$ at $q = 61$
  ($R^2 > 0.98$ at all tested primes), independently reproduced by pure combinatorial set
  arithmetic (no Weil phase, no Gram–Schmidt, no SVD)
- these fitted slopes admit an exact closed form: $\Sigma_n^{(c)}$ depends on the block $c$
  only through a projective pair $(\alpha,\beta)$, and is therefore, by algebraic identity,
  **exactly independent of the central coordinate $\gamma$** and of the translational
  coordinate $a$ — no coherence or metaplectic-phase mechanism can affect it
- using this closed form, the fitted slopes above are shown to be **finite-$q$ crossover
  statistics** of the block saturation-depth distribution, not estimates of an intrinsic
  asymptotic exponent
- the intrinsic unfolded exponent is derived exactly:
  \[
  \delta_{\mathrm{exact}} = 3 \qquad (q\to\infty,\ n\to\infty,\ n=o(\sqrt q)),
  \]
  from Heisenberg shell growth alone, holding block-by-block (not only in the mean)

Thus:

- the central coordinate $\gamma$, contrary to the paper's original motivation for building
  the exact projection, is provably inert for this observable
- the gap between the finite-$q$ fitted slopes and the O11 proxy value
  $\hat\delta_{\mathrm{cap}}\approx 3.39$ is real and reproducible but is not evidence of a
  central-coordinate/coherence mechanism
- the remaining issue is no longer observability or asymptotic convergence (both are now
  settled) but determining which regime the O3–O7 $\delta\mapsto\beta^*$ relation legitimately
  takes as input

# Structural Role of O12

O12 completes the extraction chain initiated in O8:

- **O8**: geometric obstruction from exponential shell growth
- **O9**: polynomial-growth geometry restores the observable window
- **O10**: dense fingerprints fail at the representation level
- **O11**: proxy Weil-block construction restores observability
- **O12**: exact Weil projection reveals the true exponent regime

O12 is the first step where the exponent is measured in the **exact irreducible representation**.

# What O12 Adds

O12 introduces several decisive advances:

- the **exact Weil-block observable** replacing the O11 proxy
- a blockwise rank-tracking algorithm in irreducible dimension $q$
- an exact closed form for that observable (Proposition on the projective pair
  $(\alpha,\beta)$), proving it independent of $\gamma$ rather than merely diagnosing its
  effect empirically — the central coherence observable $\ell_\gamma(n)$ is retained as a
  diagnostic of the BFS geometry, not of the capacity observable itself
- the first exact extraction of the finite-$q$ capacity slope, cross-checked by pure
  combinatorial set arithmetic
- the first derivation of the intrinsic unfolded asymptotic exponent, $\delta_{\mathrm{exact}}=3$,
  in closed form
- a decomposition showing the finite-$q$ fitted slopes are crossover statistics of the
  saturation-depth distribution, not a departure from a shared per-block exponent

# Interpretation of the Result

The main conceptual outcome is that the central coordinate is **exactly irrelevant** to
this rank-based capacity observable — a stronger and more surprising finding than the
paper originally set out to test.

The exact Weil projection shows that:

- the metaplectic phase $\psi_c(\gamma)$ is present in the representation and in the group
  action, but is provably invisible to the rank observable $\Sigma_n^{(c)}$ computed here
- the gap between the finite-$q$ exact and proxy fitted slopes reflects different ambient
  dimensions and covering geometries, not different sensitivity to $\gamma$
- the finite-$q$ fitted slopes are crossover statistics, not evidence of a steeper
  intrinsic decay: the intrinsic unfolded exponent is exactly $3$, block-by-block, not
  merely in the mean

This leads to:

- shorter finite-$q$ fitting windows than the proxy, because the exact ambient block
  dimension is $q$ rather than $q^2$ — a real structural feature, unrelated to $\gamma$
- a refined picture of universality: block-by-block universality of the intrinsic exponent
  is now **established analytically** (not merely tested for at the mean level), with the
  observed finite-$q$ inter-block variance attributable to the saturation-depth
  distribution rather than to a failure of universality

In particular:

- O11 identified the correct proxy-level observable
- O12 shows the exact observable's finite-$q$ fitted slope is not directly comparable to
  it as a measure of $\gamma$-dynamics, and derives the exact observable's own asymptotic
  exponent independently

# Relation to Previous Steps

O12 preserves all previous structural results:

- spectral admissibility from **Step 1**
- binary-polyhedral maximality from **Step 2**
- three-level ADE stratigraphy from **Step 3**
- projective ordering via **O1**
- hierarchical amplification via **O3**
- structural upper bound on $\beta$ from **O4**
- admissible-frontier saturation from **O5**
- fixed finite-dimensional no-go from **O6**
- capacity formulation and state law from **O7**
- growing fingerprint and geometric obstruction from **O8**
- polynomial-growth resolution from **O9**
- algorithmic obstruction diagnosis from **O10**
- proxy-level representation-adapted extraction from **O11**

It does not replace the capacity definition of O7,
but replaces the O11 proxy by the exact Weil representation.

# Conceptual Structure

O12 advances the structural chain as follows:

1. Spectral admissibility → mode selection
2. Spectral capacity → binary-polyhedral maximality
3. Spectral stratigraphy → discrete ADE levels
4. O1 → ordering via support contraction
5. O3 → amplification via valence growth
6. O4 → structural upper bound on $\beta$
7. O5 → admissible-frontier saturation
8. O6 → fixed finite-dimensional no-go
9. O7 → projective capacity formulation
10. O8 → growing fingerprint + geometric obstruction
11. O9 → polynomial-growth geometry
12. O10 → algorithmic obstruction
13. O11 → proxy-level representation-adapted extraction
14. O12 → exact Weil-block extraction of $\delta$

The programme now identifies:

- the correct observable class (O7)
- the correct geometry (O9)
- the correct proxy-level representation (O11)
- the first exact representation-level regime shift (O12)

# What O12 Resolves

O12 provides:

- the exact implementation left open in O11
- a proof, not merely a numerical comparison, that the finite-$q$ exact and proxy fitted
  slopes cannot differ because of $\gamma$-dynamics
- the exact combinatorial mechanism behind the finite-$q$ fitted slopes (saturation-depth
  crossover, not an estimate of the asymptotic exponent), and the intrinsic asymptotic
  exponent itself, derived independently in closed form ($\delta_{\mathrm{exact}}=3$)
- a determination that no $\beta^*$ constraint can currently be drawn from this observable

# Status of the Cascade Exponent $\beta^*$

No constraint on $\beta^*$ is drawn from O12.
The O3–O7 structural relation
\[
\beta^* = \frac{1}{\delta + \tfrac12}
\]
takes a capacity decay exponent $\delta$ as input, but O12 shows this construction carries
three structurally distinct exponent-like quantities: the finite-$q$ fitted slope, the
unfolded intrinsic exponent ($=3$), and a saturation-scale scaling function with no exponent
at all. The O3–O7 derivation does not, on its own text, specify which of these is the
intended input. Substituting any of them into the relation without first settling this
would repeat the same category error the present paper corrects. Resolving it requires
re-auditing O3–O7 itself.

# Residual Open Problem

What remains is no longer the existence of an exact observable, nor its asymptotic
exponent — both are now settled.

The remaining tasks are:

- re-auditing the O3–O7 structural relation to determine which regime its $\delta$ input
  is drawn from, before any $\beta^*$ constraint can be stated
- auditing O13 and O15, which share this pipeline, for the same regime confusion
- classifying O16 and O17's own use of this construction

# Open Directions

1. **Larger-prime exact computation (O12-O1), as an empirical check**  
   Extend the exact Weil-block computation to $q \geq 101$ to confirm empirically that the
   fitted crossover slope moves toward the analytic prediction $\delta_{\mathrm{exact}}=3$
   as the fitting window is pushed further into the unfolded regime.

2. **Re-audit of the structural relation $\delta \mapsto \beta^*$**  
   Determine which of the three exponent-like regimes identified above O3–O7's derivation
   actually presupposes.

3. **Full block survey**  
   Test the analytically-derived block-by-block universality at larger sample sizes.

# Status

This framework is now:

- free of algebraic obstruction (**O6**)
- free of geometric obstruction (**O8 → O9**)
- free of representation obstruction at the proxy level (**O10 → O11**)
- extended to the exact Weil representation (**O12**)

It does not assume:

- that the proxy and exact observables coincide
- that blockwise universality must hold exactly
- that the exact finite-$q$ regime already matches the asymptotic phenomenological target

# Reproduction

```bash
cd code
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 spectral_O12.py --mode paper
```

Reproduces the published figures (`fig2_variance.pdf`–`fig5_coherence.pdf`) and Table~3
(`δ̂_exact = 4.37, 4.28, 4.80` at `q = 29, 53, 61`) at fixed `RNG_BASE = 42`. The exact
`(α,β)` closed-form cross-check reported in the paper (Section 5) — an independent,
representation-free reproduction of the same three values — is
`admissibility/notes/o12_set_arithmetic.py` in the parent Cosmochrony workspace; the
saturation-depth law and BFS-truncation checks underlying the correction are
`admissibility/notes/o12_saturation_law.py` and
`admissibility/notes/o12_bfs_truncation_check.py`.

# Repository Structure

```text
o12/
├── tex/      # LaTeX sources
├── code/     # Reproduction script, figures, requirements.txt
└── README.md
```
`out/` (compiled PDF) is generated locally by `compile.sh` and is git-ignored, not part of the
repository; the citable PDF is the one attached to the Zenodo record (see Citation below).
# Citation

If you reference this work, please cite:

J. Beau, Exact Weil-Block Projective Capacity on Heisenberg Graphs:
Resolving the Final Obstruction to δ Extraction, Zenodo, 2026.

# Acknowledgements

Portions of the derivations, conceptual synthesis, numerical strategy,
and editorial refinement benefited from iterative interactions with
large language models used as analytical assistants.
All theoretical results, computations, and interpretations remain the
sole responsibility of the author.

# Contributions

This repository is intended as a research reference.

Critical feedback, independent verification, alternative implementations
of exact Weil-block tracking, and asymptotic extensions to larger primes
are welcome.

Please open an issue to discuss conceptual points,
technical details, or possible extensions.
