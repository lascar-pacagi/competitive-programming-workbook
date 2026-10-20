# C. Minimal Period

You are given a string `s` of length `n`. Find the length of the shortest
nonempty block whose copies can be concatenated to form **exactly** `s`.
Every copy must be complete: a partial final copy is not allowed.

For example, `ababab` consists of three copies of `ab`, so its answer is `2`.
For `ababa`, repeating `ab` would leave an incomplete final copy, so its answer
is `5`. Using the whole string as a single block is always allowed.

## Input

The only line contains `s`.

- `1 <= n <= 200000`.
- `s` contains only lowercase English letters (`a`-`z`).

## Output

Print one integer: the smallest block length `k` such that `k` divides `n`
and `s` consists of `n / k` copies of its first `k` characters.
If no shorter block works, print `n`.

## Sample

Input:

```text
abcabcabc
```

Output:

```text
3
```

The string consists of three copies of `abc`, and no shorter block works.
