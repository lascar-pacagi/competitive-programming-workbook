# Z. Smallest Alternating Partition

Partition the positions of a binary string `s` into subsequences. Within every
subsequence, consecutive selected characters must be different.

First minimize the number of subsequences. Among all partitions using that
minimum number, print the lexicographically smallest sequence of labels
`group[1], group[2], ..., group[n]`.

Group labels are canonical: they are positive integers, and the first
occurrence of label `g` must appear before the first occurrence of label
`g + 1`. Thus new groups are named `1, 2, 3, ...` in creation order.

## Input

One binary string `s`.

`1 <= |s| <= 200000`

## Output

On the first line, print the minimum number of subsequences.

On the second line, print `n` group labels. Position `i` belongs to
subsequence `group[i]`.

## Sample Input

```text
0110
```

## Sample Output

```text
2
1 1 2 1
```
