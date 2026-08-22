# L. Random Divisor Descent

For each query, start with the integer `x`. If the current value is greater
than `1`, choose one of its proper positive divisors uniformly at random and
replace the current value by that divisor. Stop upon reaching `1`.

A **proper positive divisor** of `x` is a positive divisor `d` satisfying
`1 <= d < x`; in particular, `x` itself is not proper, while `1` is. For
example, the proper positive divisors of `12` are `1, 2, 3, 4, 6`. The value
`1` has no need for a divisor choice because the process stops immediately.

Find the expected number of replacements. Print the expectation modulo
`1000000007`; represent a fraction `p/q` as `p * q^(-1)` modulo that prime.

## Input

```text
q
x1 x2 ... xq
```

`1 <= q <= 200000`, `1 <= x[i] <= 1000000`.

## Output

Print one modular expectation per query.

## Sample

```text
3
1 4 6
```

```text
0
500000005
666666673
```
