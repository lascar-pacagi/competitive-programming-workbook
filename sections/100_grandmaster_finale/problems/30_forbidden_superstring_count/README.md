# Forbidden Superstring Count

Over alphabet `abc`, count length-`L` strings that contain every required
pattern and contain no forbidden pattern. Print the answer modulo `998244353`.

## Input
```text
R F L
R required patterns
F forbidden patterns
```
`0 <= R <= 5`, `0 <= F <= 5`, `0 <= L <= 10^18`; total pattern length `<= 18`.

## Sample input
```text
1 1 3
ab
cc
```
## Sample output
```text
5
```
