# A. Primitive Necklaces

A necklace of length `n` is a circular sequence colored with `c` colors. Two
necklaces are the same if one is a rotation of the other.

A necklace is **primitive** if no rotation by `1..n-1` positions leaves it
unchanged. Equivalently, its smallest period is exactly `n`.

For each query, count primitive necklaces modulo `1,000,000,007`.

## Input

```text
q
n1 c1
...
nq cq
```

- `1 <= q <= 50`
- `1 <= n <= 10^6`
- `1 <= c <= 10^9`

## Output

Print one answer per query.

## Sample

```text
3
1 3
2 2
3 2
```

```text
3
1
2
```
