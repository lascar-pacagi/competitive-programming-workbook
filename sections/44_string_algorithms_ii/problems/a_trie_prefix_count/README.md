# A. Trie Prefix Count

You are given a dictionary containing `n` words and `q` query strings.
For each query string `p`, count how many dictionary words begin with `p`.

A string `p` is a **prefix** of a word if it consists of that word's first
`|p|` characters. The whole word is also one of its prefixes. For example,
`ap` is a prefix of `apple` and `ape`, but is not a prefix of `bat`.

Dictionary entries are counted separately: if the same word appears twice,
both copies contribute to every matching query. Queries do not change the
dictionary. A query longer than a word cannot be a prefix of that word.

## Input

The first line contains two integers `n` and `q`.
The next `n` lines each contain one dictionary word.
The following `q` lines each contain one query string.

- `1 <= n, q <= 200000`.
- Every word and query is nonempty and contains only lowercase English
  letters (`a`-`z`).
- The total length of the `n` dictionary words is at most `200000`.
- The total length of the `q` query strings is at most `200000`.

## Output

Print `q` integers, one per line, in query order. Each integer is the number
of dictionary entries beginning with that query string. Print `0` if no word
matches.

## Sample

Input:

```text
4 4
apple
ape
bat
bar
ap
app
b
z
```

Output:

```text
2
1
2
0
```

`ap` matches `apple` and `ape`. `app` matches only `apple`. `b` matches
`bat` and `bar`. No dictionary word begins with `z`.
