"""Tiny exhaustive oracles for Sections 76--78."""

from __future__ import annotations

import argparse
import collections
import random
from pathlib import Path


def substrings(s: str) -> list[str]:
    return [s[left:right] for left in range(len(s)) for right in range(left + 1, len(s) + 1)]


def lcp(a: str, b: str) -> int:
    size = 0
    while size < min(len(a), len(b)) and a[size] == b[size]:
        size += 1
    return size


def palindrome_profile(s: str) -> str:
    lines = []
    for end in range(1, len(s) + 1):
        prefix = s[:end]
        pals = {piece for piece in substrings(prefix) if piece == piece[::-1]}
        longest_suffix = max(
            length
            for length in range(1, end + 1)
            if prefix[-length:] == prefix[-length:][::-1]
        )
        lines.append(f"{len(pals)} {longest_suffix}")
    return "\n".join(lines)


def make_case(kind: str, rng: random.Random) -> tuple[str, str]:
    n = rng.randint(1, 9)
    s = "".join(rng.choice("abc") for _ in range(n))
    pieces = substrings(s)
    counts = collections.Counter(pieces)
    if kind == "suffix_dump":
        sa = sorted(range(n), key=lambda start: s[start:])
        first = " ".join(str(start + 1) for start in sa)
        second = " ".join(str(lcp(s[sa[i - 1] :], s[sa[i] :])) for i in range(1, n))
        return s + "\n", first + "\n" + second + "\n"
    if kind == "repeat_k":
        k = rng.randint(1, n)
        answer = max((len(piece) for piece, count in counts.items() if count >= k), default=0)
        return f"{s} {k}\n", f"{answer}\n"
    if kind == "pattern_queries":
        patterns = ["".join(rng.choice("abcd") for _ in range(rng.randint(1, 5))) for _ in range(8)]
        answers = [sum(s.startswith(pattern, start) for start in range(n)) for pattern in patterns]
        return f"{s}\n{len(patterns)}\n" + "\n".join(patterns) + "\n", "\n".join(map(str, answers)) + "\n"
    if kind == "disjoint_repeat":
        answer = 0
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                if any(s[left:left + length] == s[right:right + length] and abs(left - right) >= length for right in range(n - length + 1)):
                    answer = length
        return s + "\n", f"{answer}\n"
    if kind == "kth_distinct":
        ordered = sorted(set(pieces))
        k = rng.randint(1, len(ordered) + 2)
        answer = ordered[k - 1] if k <= len(ordered) else "IMPOSSIBLE"
        return f"{s} {k}\n", answer + "\n"
    if kind == "lcs":
        other = "".join(rng.choice("abcd") for _ in range(rng.randint(1, 9)))
        answer = max(map(len, set(pieces) & set(substrings(other))), default=0)
        return f"{s} {other}\n", f"{answer}\n"
    if kind == "pal_profile":
        return s + "\n", palindrome_profile(s) + "\n"
    if kind == "absent_word":
        present = set(pieces)
        length = 1
        frontier = [""]
        while True:
            words = [prefix + char for prefix in frontier for char in "abcdefghijklmnopqrstuvwxyz"]
            for word in words:
                if word not in present:
                    return s + "\n", word + "\n"
            frontier = words
            length += 1
    if kind == "rotation":
        rotations = [(s[start:] + s[:start], start) for start in range(n)]
        answer, start = min(rotations)
        return s + "\n", f"{answer}\n{start + 1}\n"
    if kind == "spectrum":
        answer = [max((len(piece) for piece, count in counts.items() if count >= k), default=0) for k in range(1, n + 1)]
        return s + "\n", " ".join(map(str, answer)) + "\n"
    if kind == "kth_multi":
        ordered = sorted(pieces)
        k = rng.randint(1, len(ordered) + 2)
        answer = ordered[k - 1] if k <= len(ordered) else "IMPOSSIBLE"
        return f"{s} {k}\n", answer + "\n"
    if kind == "common_count":
        other = "".join(rng.choice("abcd") for _ in range(rng.randint(1, 9)))
        answer = len(set(pieces) & set(substrings(other)))
        return f"{s} {other}\n", f"{answer}\n"
    if kind == "pal_value":
        answer = max((len(piece) * count for piece, count in counts.items() if piece == piece[::-1]), default=0)
        return s + "\n", f"{answer}\n"
    if kind == "multi_lcs":
        m = rng.randint(2, 5)
        archives = [s] + ["".join(rng.choice("abcd") for _ in range(rng.randint(1, 9))) for _ in range(m - 1)]
        k = rng.randint(1, m)
        answer = max((len(piece) for piece in set(pieces) if sum(piece in archive for archive in archives) >= k), default=0)
        return f"{m} {k}\n" + "\n".join(archives) + "\n", f"{answer}\n"
    raise ValueError(kind)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("kind")
    parser.add_argument("--count", type=int, default=20)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        input_text, output_text = make_case(args.kind, rng)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(input_text, encoding="utf-8")
        stem.with_suffix(".out").write_text(output_text, encoding="utf-8")


if __name__ == "__main__":
    main()
