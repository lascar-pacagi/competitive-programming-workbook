# Dynamic Forest XOR

Maintain a forest with vertex values. Operations are `LINK u v`, `CUT u v`, `SET u x`, and `XOR u v`; link/cut validity and query connectivity are guaranteed. `n,q <= 200000`.

Sample input
```text
3 6
1 2 4
LINK 1 2
LINK 2 3
XOR 1 3
SET 2 7
XOR 1 3
CUT 2 3
```
Sample output
```text
7
2
```
