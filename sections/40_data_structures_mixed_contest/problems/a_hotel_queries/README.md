# A. Hotel Queries

For each arriving group, place it in the first hotel with enough remaining capacity, subtract the group size from that capacity, and print the hotel's index. Print `0` if no hotel has enough capacity.

## Input

The first line contains `n` and `q`. The second line contains the `n` hotel capacities. The third line contains the sizes of the `q` groups in arrival order.

## Output

Print the assigned 1-based hotel index for each group, or `0` if it is rejected.

## Constraints

- `1 <= n, q <= 200000`
- `0 <= capacity[i] <= 10^9`
- `1 <= group[i] <= 10^9`

## Sample

Input:

```text
5 5
3 1 4 1 5
2 4 4 1 6
```

Output:

```text
1 3 5 1 0
```
