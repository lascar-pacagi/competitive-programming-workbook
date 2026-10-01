# XOR Walk Spectrum

All arithmetic is modulo `998244353`.

Arrays `a` and `b` have length `2^k`. Print the array `c` of the same length
with

```text
c[s] = sum over pairs (x, y) with x XOR y = s of a[x] * b[y].
```

## Input

```text
k
a[0] ... a[2^k - 1]
b[0] ... b[2^k - 1]
```

- `0 <= k <= 20`;
- all values lie in `[0, 998244353)`.

## Output

Print `c[0] ... c[2^k - 1]` on one line.

## Sample input
```text
2
1 2 3 4
4 3 2 1
```
## Sample output
```text
20 22 28 30
```
