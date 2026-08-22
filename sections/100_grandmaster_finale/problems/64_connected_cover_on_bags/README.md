# Connected Cover On Bags

Nice-bag weighted cover transitions are the kernel; canonical connectivity partitions refine each selected-mask state.

This nice-tree-decomposition vertex-cover kernel supplies the weighted selection layer used before connectivity partitions are added.

Find the minimum weight of a vertex cover using a supplied valid nice tree decomposition of width at most 15. Vertex weights are nonnegative. The decomposition format and guarantees are the same as in Nice-Decomposition Independent Set: `L`, `I child vertex`, `F child vertex`, and `J left right`; nodes are topologically ordered and node `t` is an empty-bag root. `n <= 60`, `t <= 200000`.

Sample input
```text
2 1
5 7
1 2
5
L
I 1 1
I 2 2
F 3 1
F 4 2
```
Sample output
```text
5
```
