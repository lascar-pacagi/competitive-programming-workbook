# H. Connectivity Countdown

An undirected graph starts with `m` numbered edges. Process:

- `D e`: delete edge `e` (each edge is deleted at most once);
- `Q u v`: print `YES` if `u` and `v` are currently connected, otherwise
  `NO`.

## Input
```text
n m q
m lines: u v
q operations
```
`1 <= n,m,q <= 200000`.

## Sample
```text
4 4 6
1 2
2 3
3 4
1 4
Q 1 3
D 2
Q 1 3
D 4
Q 1 3
Q 3 4
```
```text
YES
YES
NO
YES
```
