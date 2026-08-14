# D. Pattern Permutation

For each test case, you are given an integer `n` and a pattern `p` of length
`n - 1` containing only `<` and `>`.

Construct the lexicographically smallest permutation `a` of the integers from
`1` through `n` satisfying every comparison in the pattern:

- `p[i] = '<'` means `a[i] < a[i + 1]`;
- `p[i] = '>'` means `a[i] > a[i + 1]`.

The comparison positions are zero-indexed in this description. A solution
always exists.

## Input

```text
T
n p
...
```

`1 <= T <= 100`, `2 <= n <= 200000`, and the sum of all `n` is at most
`200000`.

## Output

For each test case, print the required permutation.

## Sample

Input:

```text
4
6 ><<>>
2 >
5 <<<<
5 >>>>
```

Output:

```text
2 1 3 6 5 4
2 1
1 2 3 4 5
5 4 3 2 1
```

For the first pattern, the output satisfies
`2 > 1 < 3 < 6 > 5 > 4`. No lexicographically smaller valid permutation
exists.
