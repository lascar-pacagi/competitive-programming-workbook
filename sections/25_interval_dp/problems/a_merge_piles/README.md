# A. Merge Piles

There are `n` piles in a row. Pile `i` contains `a[i]` stones. In one move, you
may merge two adjacent groups of piles. The cost of that move is the total
number of stones in the new merged group.

Find the minimum total cost to merge all piles into one group.

## Input

```text
n
a1 a2 ... an
```

`1 <= n <= 200`, `1 <= ai <= 10^6`.

## Output

Print the minimum total cost.

## Sample

Input:

```text
4
10 20 30 40
```

Output:

```text
190
```

