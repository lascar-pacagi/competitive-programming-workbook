# Cavern Descent

A cave system forms a tree rooted at chamber `1`. Chamber `v` has a launch
factor `a[v]` and a landing factor `b[v]`; either may be negative.

From chamber `x` an explorer may jump to **any** chamber `y` that lies in the
subtree of `x` with `y != x`. The jump costs `a[x] * b[y]`. Jumps may be
chained, and the total cost is the sum of the jump costs. An exit is a chamber
without children in the rooted tree (so the root is an exit only when
`n = 1`).

For every chamber, print the minimum total cost of reaching some exit from it.
Starting at an exit costs `0`.

## Input

```text
n
a[1] ... a[n]
b[1] ... b[n]
n-1 lines: u v
```

- `1 <= n <= 200000`;
- `|a[v]|, |b[v]| <= 100000`;
- the edges form a tree.

## Output

Print `n` integers on one line: the answers for chambers `1..n`.

## Sample input

```text
6
2 -3 1 4 0 -1
1 5 -2 3 2 7
1 2
1 3
2 4
2 5
3 6
```

## Sample output

```text
1 -9 7 0 0 0
```
