# Section 30: GCD, LCM, and Diophantine Equations

This section teaches Euclid's algorithm, safe lcm computation, extended Euclid,
modular inverses under composite moduli, and solving equations of the form
`ax + by = c`.

## Study Order

1. Read `lesson.qmd`.
2. Attempt the local exercises:
   - `a_gcd_lcm_queries`
   - `b_general_inverse`
   - `c_linear_diophantine`
3. Run the checker:

```bash
python3 sections/30_gcd_lcm_diophantine/check.py
```

To test the reference solutions:

```bash
CP_TARGET=solution python3 sections/30_gcd_lcm_diophantine/check.py
```

4. Read `editorial.qmd`.
5. Work through `PRACTICE.md`.
