# Nice-Decomposition Independent Set

Find a maximum-weight independent set using a supplied valid nice tree decomposition of width at most 15. Vertices are `1..n`; weights may be negative. Decomposition nodes are topologically ordered and the root is node `t` with empty bag.

Node formats are `L`, `I child vertex`, `F child vertex`, and `J left right`. `I` adds the vertex to its child's bag, `F` removes it, and `J` has two children with identical bags. The input guarantees the nice-decomposition properties and that every graph edge appears together in some bag. `n <= 60`, `t <= 200000`, and the aggregate state budget `sum(2^|bag|)` over all decomposition nodes is at most `2000000`.

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
7
```
