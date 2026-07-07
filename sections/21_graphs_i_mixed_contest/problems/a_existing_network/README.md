# A. Existing Network

Some pairs of cities are already connected by free existing cables. You may buy
additional undirected weighted cables. Find the minimum additional cost needed
to make all cities connected.

If it is impossible, print `IMPOSSIBLE`.

## Input

```text
n f p
free_u1 free_v1
...
free_uf free_vf
paid_u1 paid_v1 paid_w1
...
paid_up paid_vp paid_wp
```

`1 <= n <= 2 * 10^5`, `0 <= f,p <= 2 * 10^5`, `0 <= wi <= 10^9`.

## Output

Print the minimum additional cost, or `IMPOSSIBLE`.

## Sample

Input:

```text
5 2 4
1 2
4 5
2 3 4
3 4 7
1 5 20
2 5 10
```

Output:

```text
11
```

