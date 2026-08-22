# Suffix Order And LCP

A nonempty lowercase string `s` is given. Print the starting positions of all suffixes in lexicographic order, using 1-based positions. On the next line print the LCP lengths of every adjacent pair in that order.

Input: one string `s`, with `1 <= |s| <= 200000`.

Output: the suffix positions, then `|s|-1` LCP values (an empty second line when `|s|=1`).

Sample input
```text
banana
```
Sample output
```text
6 4 2 1 5 3
1 3 0 0 2
```
