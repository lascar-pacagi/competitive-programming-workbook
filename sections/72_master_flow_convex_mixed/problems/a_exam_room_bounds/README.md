# A. Exam Room Bounds

There are `R` exam groups and `C` rooms. Group `r` needs exactly `need[r]` distinct rooms, and room `c` must be used by between `low[c]` and `high[c]` groups. Only listed group-room pairs are allowed. Print whether a valid selection exists.

## Input
`R C E`; one line with the `R` needs; `C` lines `low high`; then `E` allowed pairs `r c`.

`1 <= R,C <= 200`, `0 <= E <= 20000`.

## Sample
```text
2 3 5
2 1
1 1
1 2
0 2
1 1
1 2
2 2
2 3
1 3
```
```text
YES
```
