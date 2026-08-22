"""Full-limit invariant tests for Sections 91--93."""
from __future__ import annotations

import argparse
import hashlib
import math
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from stress_finale_round6 import run

ROOT = Path(__file__).resolve().parents[1]
PRIME64 = 18_446_744_073_709_551_557
FACTOR1 = 4_294_967_291
FACTOR2 = 4_294_967_279
SEMIPRIME = FACTOR1 * FACTOR2
PRIME12 = 999_999_999_989
PRIME63 = 9_223_372_036_854_775_783
TONELLI_PRIME = 9_223_372_036_836_950_017


@dataclass
class AdvancedCase:
    section: int
    slug: str
    make: callable
    check: callable
    full_size: int


def scalar_queries(q: int, value: int) -> str:
    return f"{q}\n" + (f"{value}\n" * q)


def repeated_lines(out: str, q: int, line: str) -> None:
    assert out.strip() == ((line + "\n") * q).strip()


def c91a(q: int) -> str:
    return scalar_queries(q, PRIME64)


def k91a(out: str, q: int) -> None:
    repeated_lines(out, q, "PRIME")


def c91factor(q: int) -> str:
    return scalar_queries(q, SEMIPRIME)


def k91b(out: str, q: int) -> None:
    repeated_lines(out, q, f"{FACTOR2} {FACTOR1}")


def k91c(out: str, q: int) -> None:
    repeated_lines(out, q, str((FACTOR1 - 1) * (FACTOR2 - 1)))


def k91d(out: str, q: int) -> None:
    total = (1 + FACTOR1) * (1 + FACTOR2) % 1_000_000_007
    repeated_lines(out, q, f"4 {total}")


def c92a(q: int) -> str:
    return scalar_queries(q, PRIME63)


def k92a(out: str, q: int) -> None:
    repeated_lines(out, q, "3")


def c92b(q: int) -> str:
    return f"{q}\n" + "".join(f"{PRIME12} 2 {pow(2, i, PRIME12)}\n" for i in range(1, q + 1))


def k_one(out: str, q: int) -> None:
    repeated_lines(out, q, "1")


def ascending(out: str, q: int) -> None:
    assert list(map(int, out.split())) == list(range(1, q + 1))


def c92c(q: int) -> str:
    return f"{q}\n" + "".join(f"2 {pow(2, i, PRIME12)} {PRIME12}\n" for i in range(1, q + 1))


def c92d(q: int) -> str:
    return f"{q}\n" + (f"{TONELLI_PRIME} 1\n" * q)


def k92d(out: str, q: int) -> None:
    repeated_lines(out, q, f"1 {TONELLI_PRIME - 1}")


def k93a(out: str, q: int) -> None:
    repeated_lines(out, q, str(FACTOR1))


def k93b(out: str, q: int) -> None:
    value = math.lcm(FACTOR1 - 1, FACTOR2 - 1)
    repeated_lines(out, q, str(value))


def c93c(q: int) -> str:
    return f"{q}\n" + (f"{SEMIPRIME - 1} {SEMIPRIME}\n" * q)


def k_two(out: str, q: int) -> None:
    repeated_lines(out, q, "2")


def c93d(q: int) -> str:
    return f"{q}\n" + "".join(f"{PRIME12} 1 {pow(2, i, PRIME12)}\n" for i in range(1, q + 1))


def c93e(q: int) -> str:
    return f"{TONELLI_PRIME} {q}\n" + ("1\n" * q)


def c93f(q: int) -> str:
    return f"{q}\n" + "".join(f"{PRIME12} 2 {pow(2, i, PRIME12)} 1 0\n" for i in range(1, q + 1))


CASES = [
    AdvancedCase(91, "a_prime_or_composite", c91a, k91a, 100_000),
    AdvancedCase(91, "b_complete_factorization", c91factor, k91b, 200),
    AdvancedCase(91, "c_large_totient", c91factor, k91c, 200),
    AdvancedCase(91, "d_large_divisor_statistics", c91factor, k91d, 200),
    AdvancedCase(92, "a_smallest_primitive_root", c92a, k92a, 100),
    AdvancedCase(92, "b_prime_discrete_log", c92b, ascending, 100),
    AdvancedCase(92, "c_general_discrete_log", c92c, ascending, 100),
    AdvancedCase(92, "d_modular_square_roots", c92d, k92d, 1_000),
    AdvancedCase(93, "a_largest_prime_fragment", c91factor, k93a, 200),
    AdvancedCase(93, "b_carmichael_clock", c91factor, k93b, 200),
    AdvancedCase(93, "c_multiplicative_order", c93c, k_two, 100),
    AdvancedCase(93, "d_power_congruence", c93d, ascending, 50),
    AdvancedCase(93, "e_quadratic_residue_archive", c93e, k_one, 100_000),
    AdvancedCase(93, "f_affine_exponent_meeting", c93f, ascending, 50),
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
    with tempfile.TemporaryDirectory(prefix="advanced-91-93-") as td:
        for case in selected:
            size = case.full_size if args.profile == "full" else max(2, case.full_size // 100)
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
