"""Full-limit invariant tests for Section 64 (multiplicative number theory)."""
from __future__ import annotations

import argparse
import hashlib
import math
import subprocess
import tempfile
from pathlib import Path

from stress_finale_round6 import Case, run

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sections/64_multiplicative_number_theory/problems"


def c_a(n: int) -> str:
    return f"{n} 1000000000\n" + "1 " * (n - 1) + "200000\n"


def k_a(out: str, n: int) -> None:
    assert out.strip() == str(n * (n - 1) // 2 % 1_000_000_007)


def c_b(q: int) -> str:
    return f"{q}\n" + "".join("1000000000\n" if i % 2 == 0 else "999999999\n" for i in range(q))


def k_b(out: str, q: int) -> None:
    values = list(map(int, out.split()))
    assert len(values) == q
    # Phi(N)-Phi(N-1)=phi(N), and phi(10^9)=4*10^8.
    for i in range(0, q - 1, 2):
        assert (values[i] - values[i + 1]) % 1_000_000_007 == 400_000_000


def c_c(m: int) -> str:
    return f"{m} {m}\n" + " ".join(map(str, range(1, m + 1))) + "\n"


def k_c(out: str, m: int) -> None:
    values = list(map(int, out.split()))
    assert len(values) == m
    spf = list(range(m + 1))
    for p in range(2, math.isqrt(m) + 1):
        if spf[p] == p:
            for x in range(p * p, m + 1, p):
                if spf[x] == x:
                    spf[x] = p
    expected = []
    for x in range(1, m + 1):
        y = x
        ordered = 1
        while y > 1:
            p = spf[y]
            exponent = 0
            while y % p == 0:
                y //= p
                exponent += 1
            ordered *= 2 * exponent + 1
        expected.append((ordered - 1) // 2)
    assert values == expected


def mobius(limit: int) -> list[int]:
    mu = [0] * (limit + 1)
    composite = bytearray(limit + 1)
    primes = []
    mu[1] = 1
    for value in range(2, limit + 1):
        if not composite[value]:
            primes.append(value)
            mu[value] = -1
        for prime in primes:
            product = value * prime
            if product > limit:
                break
            composite[product] = 1
            if value % prime == 0:
                break
            mu[product] = -mu[value]
    return mu


def squarefree_count(x: int, mu: list[int]) -> int:
    return sum(mu[d] * (x // (d * d)) for d in range(1, math.isqrt(x) + 1))


def c_d(q: int) -> str:
    ranks = [100_000_000_000 - i * 3_000_000_000 for i in range(q)]
    return f"{q}\n" + "".join(f"{rank}\n" for rank in ranks)


def k_d(out: str, q: int) -> None:
    values = list(map(int, out.split()))
    ranks = [100_000_000_000 - i * 3_000_000_000 for i in range(q)]
    assert len(values) == q
    mu = mobius(math.isqrt(max(values)) + 1)
    for answer, rank in zip(values, ranks):
        assert squarefree_count(answer, mu) >= rank
        assert squarefree_count(answer - 1, mu) < rank


CASES = [
    Case("a_gcd_pair_energy", c_a, k_a, 200_000),
    Case("b_summatory_totient", c_b, k_b, 30),
    Case("c_lcm_pair_spectrum", c_c, k_c, 200_000),
    Case("d_squarefree_rank", c_d, k_d, 30),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=("quick", "full"), default="quick")
    parser.add_argument("--problem", action="append")
    parser.add_argument("--lang", choices=("cpp", "py", "both"), default="both")
    parser.add_argument("--timeout", type=int, default=120)
    args = parser.parse_args()
    wanted = set(args.problem or [])
    with tempfile.TemporaryDirectory(prefix="advanced-64-") as td:
        for case in [c for c in CASES if not wanted or c.slug[0] in wanted]:
            if args.profile == "full":
                size = case.full_size
            elif case.slug.startswith(("b_", "d_")):
                size = 4
            else:
                size = max(100, case.full_size // 100)
            data = case.make(size)
            outputs = {}
            binary = Path(td) / case.slug
            if args.lang in ("cpp", "both"):
                subprocess.run(["g++", "-std=c++20", "-O2", "-pipe", str(BASE / case.slug / "solution.cpp"), "-o", str(binary)], check=True)
                outputs["cpp"], elapsed, rss = run([str(binary)], data, args.timeout)
                case.check(outputs["cpp"], size)
                print(f"{case.slug} cpp {elapsed:.3f}s, {rss / 1024:.1f} MiB")
            if args.lang in ("py", "both"):
                outputs["py"], elapsed, rss = run(["python3", str(BASE / case.slug / "solution.py")], data, args.timeout)
                case.check(outputs["py"], size)
                print(f"{case.slug} py  {elapsed:.3f}s, {rss / 1024:.1f} MiB")
            if len(outputs) == 2:
                assert outputs["cpp"].split() == outputs["py"].split()
            digest = hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12]
            print(f"  invariant OK, output sha256={digest}")


if __name__ == "__main__":
    main()
