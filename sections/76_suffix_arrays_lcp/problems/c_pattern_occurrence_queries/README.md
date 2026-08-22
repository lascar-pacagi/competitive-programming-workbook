# Pattern Occurrence Queries

Store a lowercase text `s`. For each query pattern, report how many starting positions of `s` contain that pattern.

Input: `s`, then `q`, then `q` nonempty lowercase patterns. The total pattern length is at most `200000`; `|s| <= 200000`.

Output: one count per query.

Sample input
```text
banana
3
ana
na
x
```
Sample output
```text
2
2
0
```
