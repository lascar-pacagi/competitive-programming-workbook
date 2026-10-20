# D. Prefix Frequency

You are given a string `s` of length `n`. A **prefix** of `s` is a string
formed by taking its first characters. For example, the nonempty prefixes
of `ababa` are `a`, `ab`, `aba`, `abab`, and `ababa`.

For each of these prefixes, count how many times it appears **anywhere in
the original string `s`**. Each appearance must use consecutive characters
and match the entire prefix exactly.

Count appearances at different starting positions separately, even when
they overlap. For example, `aba` appears twice in `ababa`: once using
positions `1` through `3`, and once using positions `3` through `5`.
Both appearances count, although they share the character at position `3`.

Positions are 1-based. The prefix itself, at position `1`, always counts
as one appearance. Compute each count independently using the same full
string `s`.

## Input

The only line contains `s`.

- `1 <= n <= 200000`.
- `s` contains only lowercase English letters (`a`-`z`).

## Output

Print `n` integers on one line, separated by spaces:

- The first integer counts appearances of the first character of `s`.
- The second integer counts appearances of the first two characters of `s`.
- Continue in this order up to the whole string `s`.

Thus, the `L`-th integer counts appearances of the prefix of length `L`.
The last integer is always `1`.

## Sample

Input:

```text
ababa
```

Output:

```text
3 2 2 1 1
```

Search for each prefix in the original string `ababa`:

- `a` starts at positions 1, 3, and 5. Its count is 3.
- `ab` starts at positions 1 and 3. Its count is 2.
- `aba` starts at positions 1 and 3. Its count is 2.
- `abab` starts only at position 1. Its count is 1.
- `ababa` starts only at position 1. Its count is 1.

Print these five counts in order: `3 2 2 1 1`.
