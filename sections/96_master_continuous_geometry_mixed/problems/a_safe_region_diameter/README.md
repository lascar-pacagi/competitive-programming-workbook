# A. Safe Region Diameter

Each directed line from `A` to `B` keeps the closed half-plane on its left.
Their intersection is guaranteed to be nonempty and bounded. Print the maximum
Euclidean distance between two points of the intersection.

`3 <= n <= 200000`; coordinates have absolute value at most `10^6`.

## Sample

```text
4
0 0 2 0
2 0 2 2
2 2 0 2
0 2 0 0
```

```text
2.8284271247
```
