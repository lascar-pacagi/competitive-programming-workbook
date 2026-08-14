# D. Unique Prefix Lengths

You are given `n` lowercase words. For each word, print the length of its
shortest prefix that is a prefix of exactly one input word.

If no such prefix exists, print `-1`. Equal words are separate input words, so
duplicates can make the answer impossible.

## Input

```text
n
s1
s2
...
sn
```

- `1 <= n <= 200,000`
- Every word contains lowercase English letters.
- The total length of all words is at most `200,000`.

## Output

Print one answer per input word, in input order.

## Sample

```text
5
cat
car
dog
do
cat
```

```text
-1
3
3
-1
-1
```

`car` needs all three letters because `ca` is also a prefix of `cat`. The two
copies of `cat` can never be distinguished by a prefix.
