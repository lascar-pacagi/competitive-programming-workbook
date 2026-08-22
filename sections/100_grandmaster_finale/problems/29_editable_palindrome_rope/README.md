# Editable Palindrome Rope

Maintain a lowercase string under operations `SET i c`, `REV l r`, and
`PAL l r`. Reverse the requested substring or print `YES`/`NO` according as
the queried substring is a palindrome.

## Input
```text
s
q
q operations
```
`|s|,q <= 200000`; indices are one-based and valid.

## Sample input
```text
abca
5
PAL 1 4
SET 2 c
PAL 1 4
REV 2 4
PAL 1 3
```
## Sample output
```text
NO
YES
NO
```
