# Offline companion: ARC108_E -- Random IS

This is an original, locally judgeable companion for [ARC108_E -- Random IS](https://atcoder.jp/contests/arc108/tasks/arc108_e?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


There are `p` piles of stones. On a turn, a player chooses one pile and removes
one number of stones from the allowed set. A move is legal only if the chosen
pile contains at least that many stones. The player who cannot move loses.

Both players play optimally. Print whether the first player wins.

## Input

```text
m p
d1 d2 ... dm
h1 h2 ... hp
```

## Constraints

```text
1 <= m <= 20
1 <= p <= 200000
1 <= di <= 200000
0 <= hi <= 200000
```

The allowed move sizes are distinct. At least one move is legal whenever a pile
has enough stones.

## Output

Print `WIN` if the first player can force a win, otherwise print `LOSE`.

## Sample

```text
3 3
1 3 4
2 4 7
```

```text
WIN
```
