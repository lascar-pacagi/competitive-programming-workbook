# Isotonic Tree Labels

A tree is rooted at vertex `1`. Vertex `v` has an observed integer value
`a[v]`. Choose an integer label `x[v]` for every vertex such that

```text
x[parent] <= x[child]
```

for every tree edge directed away from the root. Minimize

```text
sum |x[v] - a[v]|.
```

## Input

```text
n
a[1] ... a[n]
n-1 lines: u v
```

- `1 <= n <= 200000`;
- `|a[v]| <= 10^9`;
- the edges form a tree.

## Output

Print the minimum possible total cost.

## Sample input

```text
3
10 0 0
1 2
1 3
```

## Sample output

```text
10
```
