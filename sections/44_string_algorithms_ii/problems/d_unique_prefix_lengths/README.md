# D. Unique Prefix Lengths

You are given `n` words. For each word, find the length of its shortest
nonempty prefix that is not a prefix of any other input word. If no such
prefix exists, report `-1` for that word.

A **prefix** consists of the first characters of a word. It may be the whole
word, but it cannot be empty in this problem. For example, the nonempty
prefixes of `car` are `c`, `ca`, and `car`.

Treat each input entry as a separate word, even when some entries have equal
text. A prefix is valid only if exactly one input entry begins with it.
Therefore, duplicate words cannot have a valid answer. A word that is a
prefix of another word also has no valid answer: every one of its prefixes
is shared with that longer word.

Choose the answer independently for each word using the entire original
list. Reporting an answer does not remove that word from the list.

## Input

The first line contains the integer `n`.
Each of the next `n` lines contains one word.

- `1 <= n <= 200000`.
- Every word is nonempty and contains only lowercase English letters
  (`a`-`z`).
- The total length of all input words is at most `200000`.

## Output

Print `n` integers, one per line, in input order. For each word, print the
length of its shortest valid prefix, or `-1` if none exists.

## Sample

Input:

```text
5
cat
car
dog
do
cat
```

Output:

```text
-1
3
3
-1
-1
```

Neither copy of `cat` can be distinguished from the other by a prefix.
For `car`, both `c` and `ca` are shared, but `car` is unique, giving `3`.
For `dog`, `d` and `do` are shared with `do`, but `dog` is unique, giving `3`.
The word `do` has no valid prefix because both `d` and `do` are also prefixes
of `dog`.
