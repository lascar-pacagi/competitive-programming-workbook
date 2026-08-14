# Offline companion: Booking a Room

This is an original, locally judgeable companion for [Booking a Room](https://open.kattis.com/problems/bookingaroom). It is **not** a copied contest statement. Solve this package offline to practise the course technique, then solve the linked official task on its judge.


Given closed busy intervals and a required duration `d`, find the smallest
integer start time `s >= 0` such that every integer time from `s` through
`s+d-1` is not busy. Print `-1` if no such slot exists before or at `limit`.

## Input
```text
T
n d limit
l1 r1
...
```
`1 <= T <= 30`, total `n <= 200000`, `1 <= d <= 10^9`, `0 <= l <= r <= limit <= 10^9`.

## Output
Print the earliest valid start, or `-1`.

## Sample
```text
2
3 3 12
1 2
5 7
7 9
1 2 5
0 4
```
```text
10
-1
```
