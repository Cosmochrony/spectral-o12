This repository contains the source of the **O12** Cosmochrony paper  
[*Exact Weil-Block Projective Capacity on Heisenberg Graphs: Resolving the Final Obstruction to δ Extraction*](out/SpectralO12.pdf).

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

The paper establishes that the proxy-level observable of O11 and the exact Weil
observable are **not in the same quantitative regime**.

Starting from:

- the O7 capacity observable $\Sigma_n$
- the O9 Heisenberg graph setting
- the O10 diagnosis of dense representation failure
- the O11 proxy-level block construction
- the exact Weil representation including the central phase $\gamma$

the analysis shows that:

- a measurable pre-saturation decay regime is present already at accessible primes
- the exact mean block capacity satisfies:
  \[
  \bar\Sigma_n \sim C\,n^{-\delta_{\mathrm{exact}}}
  \]
  over a short but structurally meaningful fitting window
- the extracted exact decay exponent is consistently larger than the O11 proxy value:
    - $\hat\delta_{\mathrm{exact}} \approx 4.83 \pm 0.24$ at $q = 29$
    - $\hat\delta_{\mathrm{exact}} \approx 4.40$ at $q = 53$
    - $\hat\delta_{\mathrm{exact}} \approx 4.57$ at $q = 61$
- the log-log fits are strong:
    - $R^2 > 0.98$ at all tested primes
- the central coherence observable $\ell_\gamma(n)$ decays significantly over the fitting window,
  showing that the central coordinate is dynamically active

Thus:

- the exact Weil projection yields a larger decay exponent than the proxy
- **Case B** is confirmed:
  \[
  \hat\delta_{\mathrm{exact}} > \hat\delta_{\mathrm{cap}}
  \]
- the proxy O11 underestimated the exact decay rate
- the remaining issue is no longer observability, but asymptotic convergence in $q$

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
- the central coherence observable
  \[
  \ell_\gamma(n)
  \]
  as an independent diagnostic of the metaplectic mechanism
- the first exact extraction of the capacity exponent
- numerical evidence that:
    - the exact exponent exceeds the proxy exponent
    - the central coordinate $\gamma$ is dynamically active
    - the mean decay law is robust even when blockwise universality is violated

# Interpretation of the Result

The main conceptual outcome is that the central coordinate is **not a passive correction**
to the proxy-level dynamics.

The exact Weil projection shows that:

- the proxy does not merely approximate the exact observable
- the exact and proxy observables belong to different quantitative regimes
- the metaplectic phase accelerates saturation of the exact blocks

This leads to:

- a steeper decay exponent in the exact representation
- shorter fitting windows, not because of numerical failure, but because the exact
  ambient block dimension is $q$ rather than $q^2$
- a refined picture of universality:
    - **universality in mean** is observed
    - strict block-by-block universality is not established

In particular:

- O11 identified the correct proxy-level observable
- O12 shows that the exact observable shifts the exponent upward by about one unit

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
- a direct comparison between proxy and exact decay exponents
- a structural explanation of the discrepancy via the metaplectic phase
- a quantitatively testable tension with the phenomenological target for $\beta^*$

# Main Tension Identified

Using the structural relation inherited from O3–O7,
\[
\beta^* = \frac{1}{\delta + \tfrac12},
\]
the exact values of $\hat\delta_{\mathrm{exact}}$ imply:
\[
\beta^* \approx 0.19\text{--}0.20,
\]
which lies above the phenomenological target
\[
\beta^* \in (0.09, 0.13).
\]

This is an **incompatible outcome** in the current accessible prime range.

The paper reports this tension explicitly and does not adjust the analysis to remove it.

# Residual Open Problem

What remains is no longer the existence of an exact observable.

The remaining tasks are:

- extending the exact computation to larger primes
- determining whether the exact series converges upward toward the O7 target range
- deciding whether the structural relation $\delta \mapsto \beta^*$ must be revised
  in the exact setting
- clarifying the exact role of inter-block heterogeneity

# Open Directions

1. **Larger-prime exact computation (O12-O1)**  
   Extend the exact Weil-block computation to $q \geq 101$ and beyond

2. **Asymptotic convergence of $\delta_{\mathrm{exact}}$**  
   Determine whether the current mismatch is a finite-size artefact

3. **Revision of the structural relation $\delta \mapsto \beta^*$**  
   Re-derive the mapping using the exact observable rather than the proxy-level one

4. **Full block survey**  
   Test whether blockwise heterogeneity persists at larger sample sizes

5. **Analytical derivation of $\delta_{\mathrm{exact}}$**  
   Derive the exponent directly from the metaplectic structure and BFS geometry

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

# Repository Structure

```text
paper/
├── out/      # Compiled O12 PDF
├── tex/      # LaTeX sources
└── README.md
```
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
