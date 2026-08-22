# C. Marked Pair Distances

You are given a weighted tree. Each query supplies a set of distinct marked
vertices. Print the sum of distances over every unordered pair of marked
vertices.

## Input

```text
n q
n-1 lines: u v w
q queries: k v1 ... vk
```

- `1 <= n,q <= 200000`
- `1 <= w <= 10^9`
- the sum of all `k` is at most `200000`
- answers fit signed 64-bit integers

## Sample

```text
5 2
1 2 2
1 3 1
3 4 4
3 5 3
3 2 4 5
2 1 3
```

```text
20
1
```
