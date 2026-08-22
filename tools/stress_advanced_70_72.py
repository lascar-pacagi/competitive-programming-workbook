"""Full-limit invariant tests for Sections 70--72."""
from __future__ import annotations

import argparse
import hashlib
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


def c70a(n: int) -> str:
    h = n // 2
    target = 10 * n
    edges = [(i, h + i, 1, 1) for i in range(1, h + 1)]
    edges += [(h + i, i, 0, 1) for i in range(1, h + 1)]
    cursor = 0
    while len(edges) < target:
        i = cursor % h + 1
        j = cursor // h % h + 1
        edges.append((h + i, j, 0, 1))
        cursor += 1
    return f"{n} {len(edges)}\n" + "".join(f"{u} {v} {lo} {hi}\n" for u, v, lo, hi in edges)


def yes(out: str, _: int) -> None:
    assert out.strip() == "YES"


def c70b(n: int) -> str:
    m = 10 * n
    return f"{n} {m} {n}\n1 {n}\n" + "".join(f"1 {n} 1 {cost}\n" for cost in range(1, m + 1))


def arithmetic_cost(out: str, n: int) -> None:
    assert out.strip() == str(n * (n + 1) // 2)


def quota_input(size: int, congestion: bool = False) -> str:
    eligible = size // 2
    bounds = (f"0 {size} 0\n" if congestion else f"0 {size}\n") * size
    choices = "".join(f"{worker} {project} {project}\n" for worker in range(1, size + 1) for project in range(1, eligible + 1))
    return f"{size} {size} {size * eligible}\n{bounds}{choices}"


def c70c(size: int) -> str:
    return quota_input(size)


def quota_check(out: str, size: int) -> None:
    assert out.strip() == str(size * (size // 2))


def c70d(n: int) -> str:
    m = 10 * n
    edges = [(1, 2, n, n, 0)]
    edges += [(2, 1, 0, 1, cost) for cost in range(1, n + 1)]
    edges += [(2, 1, 0, 0, 0)] * (m - len(edges))
    return f"{n} {m}\n" + "".join(f"{u} {v} {lo} {hi} {cost}\n" for u, v, lo, hi, cost in edges)


def c71a(n: int) -> str:
    return f"{n}\n" + " ".join(map(str, range(n, 0, -1))) + "\n"


def monotone_check(out: str, n: int) -> None:
    assert out.strip() == str(n * n // 4)


def c71b(n: int) -> str:
    wanted = n // 2
    edges = []
    for i in range(1, n):
        edges.append((i, i + 1, 0, "R"))
        edges.append((i, i + 1, 0, "B"))
    target = 25 * n
    i = 0
    while len(edges) < target:
        u = i % (n - 1) + 1
        v = u + 1
        edges.append((u, v, 1_000_000_000, "R" if i & 1 else "B"))
        i += 1
    return f"{n} {len(edges)} {wanted}\n" + "".join(f"{u} {v} {w} {c}\n" for u, v, w, c in edges)


def zero(out: str, _: int) -> None:
    assert out.strip() == "0"


def c71c(n: int) -> str:
    allocation = 500_000_000
    target = n * allocation
    return f"{n} {target}\n" + f"1 0 {target}\n" * n


def k71c(out: str, n: int) -> None:
    allocation = 500_000_000
    assert out.strip() == str(n * allocation * allocation)


def c71d(n: int) -> str:
    return f"{n} -1000000000 1000000000\n" + "".join(f"{x} 1\n" for x in range(n, 0, -1))


def c72a(size: int) -> str:
    half = size // 2
    needs = (f"{half} " * (size - 1)) + f"{half}\n"
    bounds = f"{half} {half}\n" * size
    allowed = "".join(f"{r} {(r + offset - 1) % size + 1}\n" for r in range(1, size + 1) for offset in range(half))
    return f"{size} {size} {size * half}\n{needs}{bounds}{allowed}"


def c72f(size: int) -> str:
    return quota_input(size, True)


CASES = [
    AdvancedCase(70, "a_bounded_circulation", c70a, yes, 200),
    AdvancedCase(70, "b_exact_cost_shipment", c70b, arithmetic_cost, 200),
    AdvancedCase(70, "c_quota_assignment", c70c, quota_check, 200),
    AdvancedCase(70, "d_min_cost_bounded_circulation", c70d, arithmetic_cost, 200),
    AdvancedCase(71, "a_monotone_l1", c71a, monotone_check, 200_000),
    AdvancedCase(71, "b_exact_red_mst", c71b, zero, 200),
    AdvancedCase(71, "c_convex_allocation", c71c, k71c, 200_000),
    AdvancedCase(71, "d_weighted_bounded_isotonic", c71d, monotone_check, 200_000),
    AdvancedCase(72, "a_exam_room_bounds", c72a, yes, 200),
    AdvancedCase(72, "b_night_delivery", c70b, arithmetic_cost, 200),
    AdvancedCase(72, "c_team_quota_profit", c70c, quota_check, 200),
    AdvancedCase(72, "d_monotone_signal", c71a, monotone_check, 200_000),
    AdvancedCase(72, "e_exact_discount_tree", c71b, zero, 200),
    AdvancedCase(72, "f_congested_team_assignment", c72f, quota_check, 250),
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
    with tempfile.TemporaryDirectory(prefix="advanced-70-72-") as td:
        for case in selected:
            size = case.full_size if args.profile == "full" else max(10, case.full_size // 100)
            if case.slug.startswith(("b_exact_red", "e_exact_discount")):
                size = max(20, size)
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
