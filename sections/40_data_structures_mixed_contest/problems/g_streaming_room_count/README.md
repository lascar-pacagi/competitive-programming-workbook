# G. Streaming Room Count

Meetings arrive in nondecreasing order of starting time. Meeting `i` occupies
one room on `[s_i, e_i)`, so a room whose meeting ends at `s_i` may be reused.
After every arrival, print the minimum number of rooms needed for all meetings
seen so far.

## Input
```text
n
s1 e1
...
sn en
```
`1 <= n <= 200000`, `0 <= s_i < e_i <= 10^9`, and starts are nondecreasing.

## Output
Print `n` integers on one line.

## Sample
```text
5
1 4
2 3
3 5
6 7
6 8
```
```text
1 2 2 2 2
```
