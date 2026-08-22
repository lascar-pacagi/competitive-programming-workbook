"""Full-limit invariant tests for Sections 88--90."""
from __future__ import annotations

import argparse
import hashlib
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from stress_finale_round6 import run

ROOT = Path(__file__).resolve().parents[1]
MOD = 998244353


@dataclass
class AdvancedCase:
    section: int
    slug: str
    make: callable
    check: callable
    full_size: int


def coefficients(values: list[int] | range) -> str:
    return " ".join(map(str, values))


def repeated_tokens(out: str, count: int, token: str) -> None:
    expected = ((token + " ") * count).rstrip()
    assert out.strip() == expected


def c88a(n: int) -> str:
    a = [1, MOD - 1] + [0] * (n - 2)
    return f"{n}\n{coefficients(a)}\n"


def all_ones(out: str, n: int) -> None:
    repeated_tokens(out, n, "1")


def c88b(n: int) -> str:
    return c88a(n)


def k88b(out: str, n: int) -> None:
    expected = [0] + [(-pow(i, MOD - 2, MOD)) % MOD for i in range(1, n)]
    assert list(map(int, out.split())) == expected


def c88c(n: int) -> str:
    a = [0, 1] + [0] * (n - 2)
    return f"{n}\n{coefficients(a)}\n"


def k88c(out: str, n: int) -> None:
    expected = [1]
    for i in range(1, n):
        expected.append(expected[-1] * pow(i, MOD - 2, MOD) % MOD)
    assert list(map(int, out.split())) == expected


def c88d(n: int) -> str:
    a = [1, 2, 1] + [0] * (n - 3)
    return f"{n}\n{coefficients(a)}\n"


def k88d(out: str, n: int) -> None:
    assert list(map(int, out.split())) == [1, 1] + [0] * (n - 2)


def c89a(n: int) -> str:
    poly = [1] + [0] * (n - 1)
    return f"{n} {n}\n{coefficients(poly)}\n{coefficients(range(n))}\n"


def c89b(n: int) -> str:
    points = "".join(f"{i} 1\n" for i in range(n))
    return f"{n}\n{points}"


def constant_poly(out: str, n: int) -> None:
    assert list(map(int, out.split())) == [1] + [0] * (n - 1)


def transform_input(k: int) -> str:
    size = 1 << k
    first = "1 " + "0 " * (size - 1)
    second = "1 " * size
    return f"{k}\n{first}\n{second}\n"


def transform_ones(out: str, k: int) -> None:
    repeated_tokens(out, 1 << k, "1")


def c90a(n: int) -> str:
    p = [1] + [0] * (n - 1)
    q = [1, MOD - 1] + [0] * (n - 2)
    return f"{n}\n{coefficients(p)}\n{coefficients(q)}\n"


def c90c(n: int) -> str:
    poly = [1] + [0] * (n - 1)
    return f"{n} {n}\n{coefficients(poly)}\n" + "7 " * n + "\n"


def c90d(n: int) -> str:
    points = "".join(f"{i} 1\n" for i in range(n - 1, -1, -1))
    return f"{n}\n{points}"


CASES = [
    AdvancedCase(88, "a_series_inverse", c88a, all_ones, 200_000),
    AdvancedCase(88, "b_series_logarithm", c88b, k88b, 200_000),
    AdvancedCase(88, "c_series_exponential", c88c, k88c, 200_000),
    AdvancedCase(88, "d_series_square_root", c88d, k88d, 200_000),
    AdvancedCase(89, "a_multipoint_evaluation", c89a, all_ones, 50_000),
    AdvancedCase(89, "b_polynomial_interpolation", c89b, constant_poly, 50_000),
    AdvancedCase(89, "c_xor_convolution", transform_input, transform_ones, 20),
    AdvancedCase(89, "d_subset_convolution", transform_input, transform_ones, 16),
    AdvancedCase(90, "a_rational_series", c90a, all_ones, 200_000),
    AdvancedCase(90, "b_connected_series", c88b, k88b, 200_000),
    AdvancedCase(90, "c_archive_evaluation", c90c, all_ones, 50_000),
    AdvancedCase(90, "d_recover_polynomial", c90d, constant_poly, 50_000),
    AdvancedCase(90, "e_or_convolution", transform_input, transform_ones, 22),
    AdvancedCase(90, "f_disjoint_cover_counts", transform_input, transform_ones, 16),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=("quick", "full"), default="quick")
    parser.add_argument("--section", action="append")
    parser.add_argument("--problem", action="append")
    parser.add_argument("--lang", choices=("cpp", "py", "both"), default="both")
    parser.add_argument("--timeout", type=int, default=600)
    args = parser.parse_args()
    sections = set(map(int, args.section or []))
    problems = set(args.problem or [])
    selected = [case for case in CASES if (not sections or case.section in sections) and (not problems or case.slug[0] in problems)]
    with tempfile.TemporaryDirectory(prefix="advanced-88-90-") as td:
        for case in selected:
            if args.profile == "full":
                size = case.full_size
            elif case.full_size <= 22:
                size = max(4, case.full_size - 6)
            else:
                size = max(20, case.full_size // 100)
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
