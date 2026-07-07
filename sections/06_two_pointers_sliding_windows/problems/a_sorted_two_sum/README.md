# A. Sorted Two Sum

## Statement

For each test case, you are given a sorted nondecreasing array and a target
`k`. Determine whether there exist two distinct indices `i < j` such that:

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

`1 <= T <= 50`, `2 <= n`, the total `n` over all test cases is at most
`200000`, and the array is already sorted.

## Output

Print `YES` if such a pair exists, otherwise print `NO`.

