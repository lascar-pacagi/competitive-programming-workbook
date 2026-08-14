# G. Next Smaller Distance

For every array position `i`, find the first position `j > i` with
`a[j] < a[i]`. Print `j-i`, or `0` if no such position exists.

## Input

```text
n
a1 a2 ... an
```

`1 <= n <= 200000`, `|a[i]| <= 10^9`.

## Output

Print `n` distances.

## Sample

```text
6
5 2 2 6 1 4
```

```text
1 3 2 1 0 0
```
