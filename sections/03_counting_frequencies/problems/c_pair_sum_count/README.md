# C. Pair Sum Count

## Statement

For each test case, you are given an array and a target `k`. Count the number
of index pairs `(i, j)` such that `i < j` and:

```text
ai + aj = k
```

## Input

```text
T
n k
a1 a2 ... an
...
```

`1 <= T <= 50`, the total `n` over all test cases is at most `200000`, and all
values fit in signed 32-bit integers.

## Output

For each test case, print the number of valid pairs.

