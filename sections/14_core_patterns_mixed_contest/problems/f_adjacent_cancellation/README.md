# F. Adjacent Cancellation

Repeatedly delete two equal adjacent characters from a lowercase string until
no such pair remains. Print the final string, or `EMPTY` if nothing remains.

## Input

```text
T
s1
...
sT
```

`1 <= T`, every string is nonempty, and the total input length is at most
`200000`.

## Output

Print one reduced string per test case.

## Sample

```text
4
abbaca
azxxzy
aaaa
abc
```

```text
ca
ay
EMPTY
abc
```
