"""Full-limit invariant tests for Sections 82--84."""
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


def increasing(n: int) -> str:
    return " ".join(map(str, range(1, n + 1)))


def c82a(n: int) -> str:
    queries = "".join(f"1 {n} {i % n + 1}\n" for i in range(n))
    return f"{n} {n}\n{increasing(n)}\n{queries}"


def k82a(out: str, n: int) -> None:
    assert list(map(int, out.split())) == list(range(1, n + 1))


def c82b(n: int) -> str:
    queries = "".join(f"1 {n} {i}\n" for i in range(n))
    return f"{n} {n}\n{increasing(n)}\n{queries}"


def k82b(out: str, n: int) -> None:
    assert list(map(int, out.split())) == list(range(n))


def c82c(n: int) -> str:
    operations = []
    for j in range(n // 2):
        operations.append(f"CAP 1 {n} {n - 1 - j}\n")
        operations.append(f"SUM 1 {n}\n")
    return f"{n} {len(operations)}\n{increasing(n)}\n" + "".join(operations)


def k82c(out: str, n: int) -> None:
    expected = []
    for j in range(n // 2):
        x = n - 1 - j
        expected.append(x * (x + 1) // 2 + (n - x) * x)
    assert list(map(int, out.split())) == expected


def c82d(n: int) -> str:
    current = 1_000_000_000
    operations = []
    while current and len(operations) + 2 <= n:
        modulus = current // 2 + 1
        operations.append(f"MOD 1 {n} {modulus}\n")
        current %= modulus
        operations.append(f"SUM 1 {n}\n")
    operations.extend(f"SUM 1 {n}\n" for _ in range(n - len(operations)))
    return f"{n} {n}\n" + ("1000000000 " * n) + "\n" + "".join(operations)


def k82d(out: str, n: int) -> None:
    current = 1_000_000_000
    expected = []
    used = 0
    while current and used + 2 <= n:
        current %= current // 2 + 1
        expected.append(current * n)
        used += 2
    expected.extend([current * n] * (n - used))
    assert list(map(int, out.split())) == expected


def c83a(n: int) -> str:
    return f"{n} {n}\n" + f"CUT 1 1 {n}\n" * n


def k83a(out: str, n: int) -> None:
    assert list(map(int, out.split())) == list(range(1, n + 1))


def c83b(n: int) -> str:
    operations = []
    for i in range(n):
        kind = i % 3
        operations.append((f"ADD 1 {n} 1\n", f"REV 1 {n}\n", f"SUM 1 {n}\n")[kind])
    return f"{n} {n}\n" + ("0 " * n) + "\n" + "".join(operations)


def k83b(out: str, n: int) -> None:
    adds = 0
    expected = []
    for i in range(n):
        if i % 3 == 0:
            adds += 1
        elif i % 3 == 2:
            expected.append(adds * n)
    assert list(map(int, out.split())) == expected


def forest_input(n: int, aggregate: str) -> tuple[str, int]:
    path = n // 2
    operations = [f"LINK {i} {i + 1}\n" for i in range(1, path)]
    operations.extend(f"{aggregate} 1 {path}\n" for _ in range(n - len(operations)))
    return f"{n} {n}\n" + ("1 " * n) + "\n" + "".join(operations), path


def c83c(n: int) -> str:
    return forest_input(n, "XOR")[0]


def k83c(out: str, n: int) -> None:
    path = n // 2
    assert out.split() == [str(path & 1)] * (n - path + 1)


def c83d(n: int) -> str:
    edges = "".join(f"{i} {i + 1} {i}\n" for i in range(1, n)) + "1 2 1\n"
    queries = "".join(f"1 {i}\n" for i in range(n))
    return f"{n} {n} {n}\n{edges}{queries}"


def k83d(out: str, n: int) -> None:
    assert list(map(int, out.split())) == list(range(1, n + 1))


def c84a(n: int) -> str:
    queries = "".join(f"1 {n} {i % n + 1}\n" for i in range(n))
    return f"{n} {n}\n{increasing(n)}\n{queries}"


def k84a(out: str, n: int) -> None:
    assert list(map(int, out.split())) == [k * (k + 1) // 2 for k in range(1, n + 1)]


def clamp_sum(n: int, low: int, high: int) -> int:
    middle = (low + 1 + high) * max(0, high - low) // 2
    return low * low + middle + (n - high) * high


def c84b(n: int) -> str:
    operations = []
    cycles = n // 3
    for j in range(cycles):
        operations.append(f"UPPER 1 {n} {n - 1 - j}\n")
        operations.append(f"LOWER 1 {n} {j + 2}\n")
        operations.append(f"SUM 1 {n}\n")
    operations.extend(f"SUM 1 {n}\n" for _ in range(n - len(operations)))
    return f"{n} {n}\n{increasing(n)}\n" + "".join(operations)


def k84b(out: str, n: int) -> None:
    expected = [clamp_sum(n, j + 2, n - 1 - j) for j in range(n // 3)]
    expected.extend([expected[-1]] * (n - 3 * (n // 3)))
    assert list(map(int, out.split())) == expected


def c84c(n: int) -> str:
    operations = []
    for i in range(n):
        kind = i % 3
        operations.append((f"REV 1 {n}\n", f"SET {i % n + 1} a\n", f"PAL 1 {n}\n")[kind])
    return f"{n} {n}\n{'a' * n}\n" + "".join(operations)


def k84c(out: str, n: int) -> None:
    assert out.split() == ["YES"] * (n // 3)


def c84d(n: int) -> str:
    return forest_input(n, "SUM")[0]


def k84d(out: str, n: int) -> None:
    path = n // 2
    assert out.split() == [str(path)] * (n - path + 1)


def c84e(n: int) -> str:
    edges = "".join(f"{i} {i + 1}\n" for i in range(1, n)) + "1 2\n"
    queries = "".join(f"1 {i}\n" for i in range(1, n + 1))
    return f"{n} {n} {n}\n{edges}{queries}"


def k84e(out: str, n: int) -> None:
    assert list(map(int, out.split())) == list(range(n))


def c84f(n: int) -> str:
    path = n // 2
    operations = [f"LINK {i} {i + 1}\n" for i in range(1, path)]
    adds = 0
    while len(operations) < n:
        if (len(operations) - (path - 1)) % 2 == 0:
            operations.append(f"AFFINE 1 {path} 1 1\n")
            adds += 1
        else:
            operations.append(f"SUM 1 {path}\n")
    return f"{n} {n}\n" + ("0 " * n) + "\n" + "".join(operations)


def k84f(out: str, n: int) -> None:
    path = n // 2
    queries = (n - (path - 1)) // 2
    assert list(map(int, out.split())) == [(i * path) % MOD for i in range(1, queries + 1)]


CASES = [
    AdvancedCase(82, "a_range_kth", c82a, k82a, 200_000),
    AdvancedCase(82, "b_range_frequency", c82b, k82b, 200_000),
    AdvancedCase(82, "c_range_cap_sum", c82c, k82c, 200_000),
    AdvancedCase(82, "d_range_modulo_sum", c82d, k82d, 200_000),
    AdvancedCase(83, "a_sequence_cut_paste", c83a, k83a, 200_000),
    AdvancedCase(83, "b_reversible_range_ledger", c83b, k83b, 200_000),
    AdvancedCase(83, "c_dynamic_forest_xor", c83c, k83c, 200_000),
    AdvancedCase(83, "d_threshold_component_size", c83d, k83d, 200_000),
    AdvancedCase(84, "a_quantile_prefix_sum", c84a, k84a, 200_000),
    AdvancedCase(84, "b_clamped_terrain", c84b, k84b, 200_000),
    AdvancedCase(84, "c_reversible_string_hash", c84c, k84c, 200_000),
    AdvancedCase(84, "d_dynamic_forest_sum", c84d, k84d, 200_000),
    AdvancedCase(84, "e_earliest_connection", c84e, k84e, 200_000),
    AdvancedCase(84, "f_affine_forest_paths", c84f, k84f, 200_000),
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
    with tempfile.TemporaryDirectory(prefix="advanced-82-84-") as td:
        for case in selected:
            size = case.full_size if args.profile == "full" else max(30, case.full_size // 100)
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
