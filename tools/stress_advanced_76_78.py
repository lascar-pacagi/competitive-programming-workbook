"""Full-limit invariant tests for Sections 76--78."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from stress_finale_round6 import run

ROOT = Path(__file__).resolve().parents[1]


@dataclass
class AdvancedCase:
    section: int
    slug: str
    make: callable
    check: callable
    full_size: int


def pseudorandom_letters(n: int) -> str:
    state = 1
    chars = ["a"]
    for _ in range(1, n):
        state = (state * 1103515245 + 12345) & 0x7FFFFFFF
        chars.append(chr(97 + state % 26))
    return "".join(chars)


def unary(n: int) -> str:
    return "a" * n + "\n"


def c76a(n: int) -> str:
    return unary(n)


def k76a(out: str, n: int) -> None:
    lines = out.splitlines()
    assert len(lines) == 2
    assert list(map(int, lines[0].split())) == list(range(n, 0, -1))
    assert list(map(int, lines[1].split())) == list(range(1, n))


def c76b(n: int) -> str:
    k = n // 2
    return f"{'a' * n} {k}\n"


def k76b(out: str, n: int) -> None:
    assert out.strip() == str(n - n // 2 + 1)


def c76c(n: int) -> str:
    patterns = "".join("a\n" if i % 2 == 0 else "z\n" for i in range(n))
    return f"{'a' * n}\n{n}\n{patterns}"


def k76c(out: str, n: int) -> None:
    values = out.split()
    assert len(values) == n
    assert all(value == (str(n) if i % 2 == 0 else "0") for i, value in enumerate(values))


def k_half(out: str, n: int) -> None:
    assert out.strip() == str(n // 2)


def c77a(n: int) -> str:
    return f"{pseudorandom_letters(n)} {10**18}\n"


def impossible(out: str, _: int) -> None:
    assert out.strip() == "IMPOSSIBLE"


def c77b(total: int) -> str:
    s = pseudorandom_letters(total // 2)
    return f"{s} {s}\n"


def half_length(out: str, total: int) -> None:
    assert out.strip() == str(total // 2)


def k77c(out: str, n: int) -> None:
    lines = out.splitlines()
    assert len(lines) == n
    assert all(line == f"{i} {i}" for i, line in enumerate(lines, 1))


def de_bruijn(alphabet: int, order: int) -> str:
    a = [0] * (alphabet * order)
    sequence: list[int] = []

    def db(t: int, p: int) -> None:
        if t > order:
            if order % p == 0:
                sequence.extend(a[1 : p + 1])
            return
        a[t] = a[t - p]
        db(t + 1, p)
        for value in range(a[t - p] + 1, alphabet):
            a[t] = value
            db(t + 1, t)

    db(1, 1)
    return "".join(chr(97 + value) for value in sequence)


DEBRUIJN_3 = de_bruijn(26, 3)


def c77d(n: int) -> str:
    repeated = (DEBRUIJN_3 * ((n + len(DEBRUIJN_3) - 1) // len(DEBRUIJN_3)))[:n]
    return repeated + "\n"


def k77d(out: str, n: int) -> None:
    s = c77d(n).strip()
    for length in range(1, 5):
        present = {s[i : i + length] for i in range(len(s) - length + 1)}
        for word in map("".join, itertools.product("abcdefghijklmnopqrstuvwxyz", repeat=length)):
            if word not in present:
                assert out.strip() == word
                return
    raise AssertionError("a length-four absent word must exist")


def c78a(n: int) -> str:
    return unary(n)


def k78a(out: str, n: int) -> None:
    lines = out.splitlines()
    assert lines == ["a" * n, "1"]


def k78b(out: str, n: int) -> None:
    assert list(map(int, out.split())) == list(range(n, 0, -1))


def c78c(n: int) -> str:
    return f"{'a' * n} {n * (n + 1) // 2}\n"


def k78c(out: str, n: int) -> None:
    assert out.strip() == "a" * n


def c78d(total: int) -> str:
    n = total // 2
    return f"{'a' * n} {'a' * n}\n"


def k78d(out: str, total: int) -> None:
    assert out.strip() == str(total // 2)


def k78e(out: str, n: int) -> None:
    assert out.strip() == str(((n + 1) * (n + 1)) // 4)


def c78f(total: int) -> str:
    m = 20
    first = pseudorandom_letters(total - (m - 1))
    return f"{m} {m}\n{first}\n" + "a\n" * (m - 1)


def one(out: str, _: int) -> None:
    assert out.strip() == "1"


CASES = [
    AdvancedCase(76, "a_suffix_order_lcp", c76a, k76a, 200_000),
    AdvancedCase(76, "b_repeated_at_least_k", c76b, k76b, 200_000),
    AdvancedCase(76, "c_pattern_occurrence_queries", c76c, k76c, 200_000),
    AdvancedCase(76, "d_disjoint_repeated_substring", unary, k_half, 200_000),
    AdvancedCase(77, "a_kth_distinct_substring", c77a, impossible, 200_000),
    AdvancedCase(77, "b_longest_common_substring", c77b, half_length, 400_000),
    AdvancedCase(77, "c_palindrome_prefix_profile", unary, k77c, 200_000),
    AdvancedCase(77, "d_shortest_absent_word", c77d, k77d, 200_000),
    AdvancedCase(78, "a_minimum_rotation", c78a, k78a, 1_000_000),
    AdvancedCase(78, "b_repetition_spectrum", unary, k78b, 200_000),
    AdvancedCase(78, "c_kth_substring_with_multiplicity", c78c, k78c, 200_000),
    AdvancedCase(78, "d_common_distinct_substrings", c78d, k78d, 400_000),
    AdvancedCase(78, "e_palindrome_frequency_value", unary, k78e, 200_000),
    AdvancedCase(78, "f_multi_archive_commonality", c78f, one, 200_000),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=("quick", "full"), default="quick")
    parser.add_argument("--section", action="append")
    parser.add_argument("--problem", action="append")
    parser.add_argument("--lang", choices=("cpp", "py", "both"), default="both")
    parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args()
    sections = set(map(int, args.section or []))
    problems = set(args.problem or [])
    selected = [case for case in CASES if (not sections or case.section in sections) and (not problems or case.slug[0] in problems)]
    with tempfile.TemporaryDirectory(prefix="advanced-76-78-") as td:
        for case in selected:
            size = case.full_size if args.profile == "full" else max(20, case.full_size // 100)
            base = next(ROOT.glob(f"sections/{case.section:02d}_*/problems"))
            data = case.make(size)
            outputs = {}
            binary = Path(td) / f"{case.section}_{case.slug}"
            if args.lang in ("cpp", "both"):
                subprocess.run(["g++", "-std=c++20", "-O2", "-pipe", str(base / case.slug / "solution.cpp"), "-o", str(binary)], check=True)
                outputs["cpp"], elapsed, rss = run([str(binary)], data, args.timeout)
                case.check(outputs["cpp"], size)
                print(f"{case.section}-{case.slug} cpp {elapsed:.3f}s, {rss / 1024:.1f} MiB")
            if args.lang in ("py", "both"):
                outputs["py"], elapsed, rss = run(["python3", str(base / case.slug / "solution.py")], data, args.timeout)
                case.check(outputs["py"], size)
                print(f"{case.section}-{case.slug} py  {elapsed:.3f}s, {rss / 1024:.1f} MiB")
            if len(outputs) == 2:
                assert outputs["cpp"].split() == outputs["py"].split()
            digest = hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12]
            print(f"  invariant OK, output sha256={digest}")


if __name__ == "__main__":
    main()
