# N. Wildcard Choice Map

For every `?` in a parenthesis string, determine which replacements can occur
in at least one valid completion of the whole string.

Build an answer string as follows:

- keep every fixed `(` or `)` unchanged;
- print `(` for a `?` if only `(` can occur there;
- print `)` for a `?` if only `)` can occur there;
- print `?` for a `?` if both choices can occur there.

If the original string has no valid completion, print `IMPOSSIBLE`.

A completion is valid if both of the following conditions hold:

1. In every prefix, the number of `(` is greater than or equal to the number
   of `)`. A prefix is allowed to have more `(` than `)`.
2. In the complete string, the number of `(` is equal to the number of `)`.

Equivalently, start with `balance = 0`, add `1` for every `(`, and subtract
`1` for every `)`. The balance must never become negative while scanning the
string, and it must be exactly zero at the end.

For example, `(())` and `()()` are valid. The string `)(` is not valid: its
first prefix is `)`, which makes the balance negative, even though the complete
string contains one parenthesis of each kind.

## Input

One string `s`.

`1 <= |s| <= 200000`, and every character is `(`, `)`, or `?`.

## Output

Print the choice map, or `IMPOSSIBLE`.

## Sample Input

```text
????
```

## Sample Output

```text
(??)
```

The only valid completions are `(())` and `()()`. Therefore the first
position is always `(`, the last is always `)`, and both middle positions can
use either parenthesis.
