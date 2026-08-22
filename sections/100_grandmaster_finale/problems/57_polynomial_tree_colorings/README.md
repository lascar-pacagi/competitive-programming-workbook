# Polynomial Tree Colorings

The validated NTT convolution kernel combines child-generated coefficient classes; tree small-to-large scheduling supplies the outer traversal.

Every vertex of an unweighted tree has color `0` or `1`. For every distance
`d` from `0` through `n-1`, count unordered pairs of **distinct** vertices
having the same color and tree distance exactly `d`.

Print all counts modulo `998244353`. Consequently, the answer for `d=0` is
always zero.

## Input

```text
n
c[1] c[2] ... c[n]
n-1 lines: u v
```

- `1 <= n <= 100000`
- `c[i]` is `0` or `1`.

## Output

Print `n` integers: the answers for distances `0,1,...,n-1`.

## Sample input

```text
4
0 1 0 1
1 2
2 3
3 4
```

## Sample output

```text
0 0 2 0
```
