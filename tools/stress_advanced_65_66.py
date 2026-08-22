"""Full-limit invariant tests for Sections 65--66."""
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
MOD = 998_244_353


@dataclass
class AdvancedCase:
    section: int
    slug: str
    make: callable
    check: callable
    full_size: int


def c65a(n: int) -> str:
    return f"{n}\n" + "A" * n + "\n" + "A" * n + "\n"


def k65a(out: str, n: int) -> None:
    assert out.split() == [str(n), "0"]


def bounded_coefficient(n: int, target: int, width: int) -> int:
    limit = n + target
    factorial = [1] * (limit + 1)
    for i in range(1, limit + 1):
        factorial[i] = factorial[i - 1] * i % MOD
    inverse_factorial = [1] * (limit + 1)
    inverse_factorial[-1] = pow(factorial[-1], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inverse_factorial[i - 1] = inverse_factorial[i] * i % MOD

    def choose(total: int, picked: int) -> int:
        if picked < 0 or picked > total:
            return 0
        return factorial[total] * inverse_factorial[picked] % MOD * inverse_factorial[total - picked] % MOD

    answer = 0
    for used in range(target // width + 1):
        term = choose(n, used) * choose(target - width * used + n - 1, n - 1) % MOD
        answer += -term if used & 1 else term
    return answer % MOD


def c65b(n: int) -> str:
    return f"{n} 50000\n" + "39 " * (n - 1) + "39\n"


def k65b(out: str, n: int) -> None:
    assert out.strip() == str(bounded_coefficient(n, 50_000, 40))


def c65c(k: int) -> str:
    initial = "7 " * (k - 1) + "7\n"
    coefficient = "1 " + "0 " * (k - 2) + ("0\n" if k > 1 else "\n")
    return f"{k} 1000000000000000000\n{initial}{coefficient}"


def k65c(out: str, _: int) -> None:
    assert out.strip() == "7"


def c65d(order: int) -> str:
    sequence = ([1] + [0] * (order - 1)) * 2
    return f"{2 * order} 1000000000000000000\n" + " ".join(map(str, sequence)) + "\n"


def k65d(out: str, order: int) -> None:
    assert out.split() == [str(order), "1"]


def c66a(q: int) -> str:
    return f"{q}\n" + "".join(f"{1_000_000 - i} 1\n" for i in range(q))


def k66a(out: str, q: int) -> None:
    assert out.split() == ["0"] * q


def phi(n: int) -> int:
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            result -= result // p
            while n % p == 0:
                n //= p
        p += 1
    if n > 1:
        result -= result // n
    return result


def c66b(q: int) -> str:
    return f"{q}\n" + "".join(f"{1_000_000_000 - i} {1_000_000_000 - i}\n" for i in range(q))


def k66b(out: str, q: int) -> None:
    assert list(map(int, out.split())) == [phi(1_000_000_000 - i) for i in range(q)]


def c66c(n: int) -> str:
    return f"{n}\n" + "?" * n + "\n" + "ACGT" * (n // 4) + "ACGT"[: n % 4] + "\n"


def k66c(out: str, n: int) -> None:
    assert out.split() == [str(n), "0"]


def c66d(n: int) -> str:
    return f"{n} 50000\n" + "1 39\n" * n


def k66d(out: str, n: int) -> None:
    assert out.strip() == str(bounded_coefficient(n, 50_000, 40))


def c66e(n: int) -> str:
    edges = [(i, i % n + 1, 1) for i in range(1, n + 1)]
    i = 0
    while len(edges) < 5000:
        edges.append((i % n + 1, (i * 37 + 11) % n + 1, 0))
        i += 1
    return f"{n} 5000 1000000000000000000 1 1\n" + "".join(
        f"{u} {v} {w}\n" for u, v, w in edges
    )


def k66e(out: str, _: int) -> None:
    assert out.strip() == "1"


def c66f(n: int) -> str:
    return f"{n}\n" + "1 " * (n - 1) + "200000\n"


def k66f(out: str, n: int) -> None:
    values = list(map(int, out.split()))
    assert len(values) == n and values[0] == n - 1
    choose = 1
    for size in range(1, n + 1):
        choose = choose * (n - size + 1) % MOD * pow(size, MOD - 2, MOD) % MOD
        expected = n - 1 if size == 1 else choose
        assert values[size - 1] == expected


CASES = [
    AdvancedCase(65, "a_cyclic_agreement", c65a, k65a, 100_000),
    AdvancedCase(65, "b_bounded_sum_product", c65b, k65b, 5_000),
    AdvancedCase(65, "c_huge_linear_recurrence", c65c, k65c, 400),
    AdvancedCase(65, "d_recurrence_recovery", c65d, k65d, 1_000),
    AdvancedCase(66, "a_primitive_necklaces", c66a, k66a, 50),
    AdvancedCase(66, "b_totient_interval", c66b, k66b, 30),
    AdvancedCase(66, "c_wildcard_rotation", c66c, k66c, 60_000),
    AdvancedCase(66, "d_weighted_compositions", c66d, k66d, 5_000),
    AdvancedCase(66, "e_black_box_walks", c66e, k66e, 80),
    AdvancedCase(66, "f_gcd_one_size_spectrum", c66f, k66f, 200_000),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=("quick", "full"), default="quick")
    parser.add_argument("--section", action="append")
    parser.add_argument("--problem", action="append")
    parser.add_argument("--lang", choices=("cpp", "py", "both"), default="both")
    parser.add_argument("--timeout", type=int, default=180)
    args = parser.parse_args()
    sections = set(map(int, args.section or []))
    problems = set(args.problem or [])
    selected = [c for c in CASES if (not sections or c.section in sections) and (not problems or c.slug[0] in problems)]
    with tempfile.TemporaryDirectory(prefix="advanced-65-66-") as td:
        for case in selected:
            if args.profile == "full":
                size = case.full_size
            elif case.slug.startswith(("a_primitive", "b_totient")):
                size = 4
            else:
                size = max(4, case.full_size // 100)
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
