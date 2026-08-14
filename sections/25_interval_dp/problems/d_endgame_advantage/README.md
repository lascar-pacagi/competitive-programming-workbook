# D. Endgame Advantage

Two players alternately take one value from either end of an array. The first
player moves first. Both players play optimally to maximize their own final
sum.

Print the maximum possible value of:

```text
first player's sum - second player's sum
```

## Input

```text
n
a1 a2 ... an
```

`1 <= n <= 3000` and `-10^9 <= ai <= 10^9`.

## Output

Print the final score difference under optimal play.

## Sample

```text
4
1 5 233 7
```

```text
222
```
