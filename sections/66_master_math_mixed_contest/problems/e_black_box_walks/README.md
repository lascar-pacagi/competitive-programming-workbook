# E. Black-Box Walks

A directed graph has edge weights modulo `998244353`. The weight of a walk is
the product of its edge weights; the empty walk has weight one.

For a given start vertex `s`, target vertex `t`, and length `K`, compute the
sum of the weights of all walks of exactly `K` edges from `s` to `t`.

Parallel edges and self-loops are allowed.

## Input

```text
n m K s t
u1 v1 w1
...
um vm wm
```

- `1 <= n <= 80`
- `0 <= m <= 5000`
- `0 <= K <= 10^18`
- `1 <= u,v,s,t <= n`
- `0 <= w < 998244353`

## Output

Print the required sum modulo `998244353`.

## Sample

```text
2 3 5 1 2
1 1 1
1 2 1
2 2 1
```

```text
5
```
