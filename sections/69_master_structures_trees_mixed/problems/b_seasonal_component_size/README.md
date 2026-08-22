# B. Seasonal Component Size

An undirected graph starts empty. Operations add or remove a currently absent
or present edge, and `S u` asks for the current size of `u`'s connected
component.

## Input
```text
n q
q operations (`+ u v`, `- u v`, or `S u`)
```
`1 <= n,q <= 200000`.

## Sample
```text
4 7
+ 1 2
+ 2 3
S 1
- 1 2
S 1
+ 3 4
S 2
```
```text
3
1
3
```
