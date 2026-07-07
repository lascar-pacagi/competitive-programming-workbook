# B. Assignment Profit

There are `n` workers and `n` jobs. If worker `i` is assigned to job `j`, the
profit is `a[i][j]`.

Assign every worker to exactly one job and every job to exactly one worker.
Maximize the total profit.

## Input

```text
n
a1,1 a1,2 ... a1,n
a2,1 a2,2 ... a2,n
...
an,1 an,2 ... an,n
```

`1 <= n <= 18`, `0 <= a[i][j] <= 10^9`.

## Output

Print the maximum total profit.

## Sample

Input:

```text
3
8 2 5
4 9 7
6 3 10
```

Output:

```text
27
```
