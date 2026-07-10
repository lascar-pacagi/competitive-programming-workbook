# C. First-Round Assignment

At the start of a contest, each teammate can independently own at most one
problem card. There is an edge from a teammate to a card when that teammate can
take the card in the first round. Find the maximum number of cards that can be
given distinct owners.

## Input

The first line contains `L R E`: the number of teammates, cards, and
compatibility edges. Each of the next `E` lines contains `teammate card`.
Teammates are numbered `1..L`, cards `1..R`. Duplicate edges may appear.

## Output

Print the maximum number of cards that can receive distinct owners.

## Constraints

`1 <= L, R <= 300`, `0 <= E <= 50000`.

## Sample

Input:

```text
3 3 5
1 1
1 2
2 1
3 2
3 3
```

Output:

```text
3
```
