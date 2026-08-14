# Section 30: GCD, LCM, and Diophantine Equations

This section teaches Euclid's algorithm, safe lcm computation, extended Euclid,
modular inverses under composite moduli, and solving equations of the form
`ax + by = c`. It now derives the generalized Chinese Remainder Theorem from
that equation instead of first assuming it in the later math mixed contest.

## Study Order

1. Read `lesson.qmd`.
2. Attempt the local exercises:
   - `a_gcd_lcm_queries`
   - `b_general_inverse`
   - `c_linear_diophantine`
   - `d_clock_offset` (blind practice: attempt it before the editorial)
   - `e_merge_congruences` (direct CRT practice)
   - `f_shared_maintenance_window` (blind recognition practice)
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
