# Section 27: Bitmask DP

This section teaches dynamic programming where a small set is stored inside an
integer mask. The focus is on recognizing `n <= 20` style constraints, using
bits to represent completed work, and choosing transitions that add one new
item at a time.

## Study Order

1. Read `lesson.qmd`.
2. Attempt the local exercises:
   - `a_skill_coverage`
   - `b_assignment_profit`
   - `c_inspection_route`
3. Run the checker:

```bash
python3 sections/27_bitmask_dp/check.py
```

To test the reference solutions:

```bash
CP_TARGET=solution python3 sections/27_bitmask_dp/check.py
```

4. Read `editorial.qmd`.
5. Work through `PRACTICE.md`.
