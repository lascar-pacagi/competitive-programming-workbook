# Echo Census

A radio operator records a transmission as a string `s` of lowercase letters.
An **echo** is a nonempty string of the form `ww`: some nonempty string `w`
immediately repeated once, such as `aa`, `abab`, or `abcabc`.

Count the **different** echoes that occur somewhere in `s` as a contiguous
substring. An echo that occurs several times is counted once.

## Input

One line containing `s`.

- `1 <= |s| <= 200000`.

## Output

Print the number of different echoes.

## Sample input

```text
abaababaab
```

## Sample output

```text
5
```

The echoes are `aa`, `abab`, `baba`, `abaaba`, and `abaababaab`.
