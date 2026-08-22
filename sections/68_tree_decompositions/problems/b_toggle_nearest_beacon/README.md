# B. Toggle Nearest Beacon

An unweighted tree initially has no active beacons.

- `T u`: toggle the beacon at `u`;
- `Q u`: print the distance from `u` to the nearest active beacon, or `-1` if
  none exists.

## Input

```text
n q
n-1 edges
q operations
```

`1 <= n,q <= 200000`.

## Sample

```text
5 7
1 2
1 3
3 4
3 5
Q 2
T 4
Q 2
T 5
Q 1
T 4
Q 4
```

```text
-1
3
2
2
```
