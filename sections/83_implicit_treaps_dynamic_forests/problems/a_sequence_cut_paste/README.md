# Sequence Cut And Paste

Start with permutation `1..n`. Operation `CUT l r p` removes positions `l..r`, then inserts that block immediately before position `p` in the remaining sequence (`p=len+1` appends). Print the final sequence. `n,q <= 200000`.

Sample input
```text
5 2
CUT 2 3 4
CUT 1 1 3
```
Sample output
```text
4 5 1 2 3
```
