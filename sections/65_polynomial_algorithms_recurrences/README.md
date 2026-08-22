# Section 65: Polynomial Algorithms And Recurrences

This section treats polynomials as algorithmic data structures. A and B build
the NTT progressively; C introduces polynomial reduction for huge recurrence
indices; D is the blind exercise and requires recurrence discovery.

| Problem | Main tool |
|---|---|
| A. Cyclic Agreement | correlation by NTT |
| B. Bounded Sum Product | generating functions and product-tree NTT |
| C. Huge Linear Recurrence | polynomial exponentiation (Kitamasa) |
| D. Recurrence Recovery | Berlekamp--Massey plus Kitamasa |

Run:

```bash
CP_TARGET=solution python3 sections/65_polynomial_algorithms_recurrences/check.py
```
