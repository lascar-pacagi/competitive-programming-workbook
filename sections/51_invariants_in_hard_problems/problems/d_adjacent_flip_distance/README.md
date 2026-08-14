# D. Adjacent Flip Distance

You are given two binary strings `A` and `B` of the same length `n`.

In one operation, choose `i` with `1 <= i < n` and flip both `A[i]` and
`A[i+1]`. Find the minimum number of operations needed to transform `A` into
`B`, or print `-1` if it is impossible.

## Input

```text
n
A
B
```

## Constraints

```text
1 <= n <= 200,000
A and B contain only 0 and 1
```

## Output

Print the minimum number of operations, or `-1`.

## Sample

Input:

```text
4
0000
1001
```

Output:

```text
3
```
