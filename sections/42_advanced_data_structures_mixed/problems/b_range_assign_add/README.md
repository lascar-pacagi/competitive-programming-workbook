# B. Range Assign and Add

Maintain an array `a[1..n]` under three kinds of operations:

- `1 l r x`: set `a[i] = x` for every `i` in `[l, r]`;
- `2 l r x`: add `x` to `a[i]` for every `i` in `[l, r]`;
- `3 l r`: print the sum of `a[l..r]`.

All indices are 1-based and inclusive.

## Input

```text
n q
a1 a2 ... an
op1
op2
...
opq
```

Each operation is one line in one of the three forms above.

## Constraints

```text
1 <= n, q <= 200,000
-1,000,000,000 <= a[i] <= 1,000,000,000
-1,000,000,000 <= x <= 1,000,000,000   for operation 1
-1,000,000 <= x <= 1,000,000           for operation 2
1 <= l <= r <= n
```

The two update kinds have different bounds on `x`. Together they keep every
value, and every printed sum, inside a signed 64-bit integer.

## Output

For every operation of type `3`, print the requested sum on its own line.

## Sample

```text
5 6
1 2 3 4 5
3 1 5
1 2 4 7
3 1 5
2 1 3 -2
3 1 5
3 2 3
```

```text
15
27
21
10
```

The array starts as `1 2 3 4 5`, whose total is `15`. The first update makes it
`1 7 7 7 5`, totalling `27`. The second makes it `-1 5 5 7 5`, totalling `21`,
and the last query covers only positions `2` and `3`.
