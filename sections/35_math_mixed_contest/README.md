# Section 35: Math Mixed Contest

This section closes the first math phase with a contest-style set mixing
modular arithmetic, combinatorics, sieve factorization, inclusion-exclusion,
and expected probability complements.

## Category Coverage

| Math category | Problem |
|---|---|
| Modular arithmetic | A. Blocked Path; C. At Least One |
| GCD, LCM, and Diophantine equations | E. Modular Appointment; F. Festival Synchronization |
| Sieve, primes, and factorization | B. Coprime Pairs; H. GCD-One Subsets; J. Target LCM Subsets |
| Combinatorics under modulo | A. Blocked Path; G. Capped Allocation; I. Exactly K Colors |
| Inclusion-exclusion | B. Coprime Pairs; D. Complete Alphabet; G. Capped Allocation; H. GCD-One Subsets; I. Exactly K Colors; K. Weighted Coupon Collection |
| Probability and expected value | C. At Least One; K. Weighted Coupon Collection; L. Random Divisor Descent |
| Totients and square-free sieves | M. Totient Prefix; N. Square-Free Queries; O. GCD Sum |
| Advanced divisor counting | P. Subarray GCD Sum; Q. Coprime Rectangles; R. Exact Divisor Count |

Modular Appointment is the local blind-practice representative for Euclid and linear
congruence reasoning.

## Six-step progression

The added problems are deliberately ordered by difficulty:

| Level | Problems |
|---|---|
| Easy | M. Totient Prefix; N. Square-Free Queries |
| More difficult | O. GCD Sum; P. Subarray GCD Sum |
| Challenging | Q. Coprime Rectangles; R. Exact Divisor Count |

## Study Order

1. Read `lesson.qmd`.
2. Attempt the local exercises:
   - `a_blocked_path`
   - `b_coprime_pairs`
   - `c_at_least_one`
   - `d_complete_alphabet` (blind practice: attempt from its README only)
   - `e_modular_appointment`
   - `f_festival_synchronization`
   - `g_capped_allocation`
   - `h_gcd_one_subsets`
   - `i_exactly_k_colors`
   - `j_target_lcm_subsets`
   - `k_weighted_coupon_collection`
   - `l_random_divisor_descent`
   - `m_totient_prefix`
   - `n_squarefree_queries`
   - `o_gcd_sum`
   - `p_subarray_gcd_sum`
   - `q_coprime_rectangles`
   - `r_exact_divisor_count`
3. Run the checker:

```bash
python3 sections/35_math_mixed_contest/check.py
```

To test the reference solutions:

```bash
CP_TARGET=solution python3 sections/35_math_mixed_contest/check.py
```

4. Read `editorial.qmd`.
5. Work through `PRACTICE.md`.
