# Persistent Text Occurrences

For every query pattern `p` and positive integer `k`, print the starting
position of the `k`-th occurrence of `p` in text `s`, ordered by position.
Print `-1` if fewer than `k` occurrences exist. Occurrences may overlap.

## Input
```text
s
q
q lines: p k
```
`s` and every `p` contain lowercase English letters. `1 <= |s|,q <= 100000`,
and the total pattern length is at most `200000`.

## Output
One answer per query. Positions are one-based.

## Sample input
```text
banana
4
ana 1
ana 2
na 2
apple 1
```
## Sample output
```text
2
4
5
-1
```
