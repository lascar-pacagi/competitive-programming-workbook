# A. Coordinate Compression

## Statement

For each test case, you are given `n` integers. Replace every value by its
zero-based rank among the distinct values in the same test case.

Equal values must receive equal ranks. Smaller values must receive smaller
ranks.

## Input

```text
T
n
a1 a2 ... an
...
```

The sum of `n` over all test cases is at most `200000`. Values may be as large
as `10^18` in absolute value.

## Output

For each test case, print `n` integers: the compressed ranks.

