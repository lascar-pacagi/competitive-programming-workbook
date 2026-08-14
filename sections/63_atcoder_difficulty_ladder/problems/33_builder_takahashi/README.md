# Offline companion: ABC239_G -- Builder Takahashi

This is an original, locally judgeable companion for [ABC239_G -- Builder Takahashi](https://atcoder.jp/contests/abc239/tasks/abc239_g?lang=en). It is **not** a copied AtCoder statement. Solve this package offline to practise a nearby course technique, then solve the linked official task on AtCoder.


Given a lowercase string `s`, for every prefix length `L` from `1` to `|s|`,
print how many times `s[0..L-1]` occurs as a substring of `s`. Overlapping
occurrences count separately.

## Input
```text
s
```
`1 <= |s| <= 200000`; `s` contains lowercase English letters.

## Output
Print `|s|` integers. The `L`-th integer is the occurrence count of the
prefix of length `L`.

## Sample
```text
ababa
```
```text
3 2 2 1 1
```
