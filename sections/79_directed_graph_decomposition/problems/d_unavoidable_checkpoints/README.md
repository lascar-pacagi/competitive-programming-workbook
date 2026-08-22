# Unavoidable Checkpoints

In a directed graph, vertex `1` is the entrance and vertex `n` is reachable. Print all vertices other than `1` and `n` that occur on every directed path from `1` to `n`.

Input: `n m`, followed by directed edges. `2 <= n <= 1500`, `m <= 10000`.

Output the count and then the sorted vertices.

Sample input
```text
5 6
1 2
1 3
2 4
3 4
4 5
2 3
```
Sample output
```text
1
4
```
