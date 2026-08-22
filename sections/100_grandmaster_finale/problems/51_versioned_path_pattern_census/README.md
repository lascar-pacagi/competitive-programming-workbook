# Versioned Path Pattern Census

Failure-tree activation is the pattern-lifetime kernel; version-tree DFS adds rollback around these range updates.

There are `n` lowercase patterns, initially inactive. Operations are `+ i`
(activate), `- i` (deactivate), and `? text`. Activation commands are valid.
For a query, print the total number of occurrences of active patterns in
`text`; overlapping occurrences and equal patterns with different indices are
counted separately.

## Input
```text
n q
n patterns
q operations
```
Total pattern and query-text length is at most `400000`; `n,q <= 200000`.

## Sample input
```text
3 6
a
aba
ba
+ 1
+ 2
? ababa
- 1
+ 3
? ababa
```
## Sample output
```text
5
4
```
