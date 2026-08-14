# D. Project Selection

There are `n` projects. Project `i` has profit `w[i]`, which may be negative.

Each rule `a b` means: if you select project `a`, you must also select project
`b`. Select any set of projects, possibly empty, satisfying all rules and
maximize the total profit.

## Input

```text
n m
w1 w2 ... wn
a1 b1
a2 b2
...
am bm
```

## Constraints

```text
1 <= n <= 200
0 <= m <= 1,000
-1,000,000,000 <= w[i] <= 1,000,000,000
1 <= a[i], b[i] <= n
a[i] != b[i]
```

## Output

Print the maximum total profit.

## Sample

Input:

```text
4 3
9 -5 7 -3
1 2
3 4
3 2
```

Output:

```text
8
```
