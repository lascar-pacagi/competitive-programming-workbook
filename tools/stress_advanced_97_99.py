"""Full-limit invariant tests for Sections 97--99."""
from __future__ import annotations

import argparse
import hashlib
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from stress_finale_round6 import run

ROOT = Path(__file__).resolve().parents[1]
MOD = 1_000_000_007


@dataclass
class Case:
    section: int
    slug: str
    make: callable
    check: callable
    full_size: int


def digit_sum_count(length: int, target: int) -> int:
    dp = [0] * (target + 1)
    dp[0] = 1
    for _ in range(length):
        dp = [sum(dp[total - digit] for digit in range(10) if digit <= total) for total in range(target + 1)]
    return dp[target]


DIGIT_SUM_18_81 = digit_sum_count(18, 81)


def repeated_query(q: int, line: str) -> str:
    return f"{q}\n" + line * q


def c97a(q: int) -> str:
    return repeated_query(q, "0 999999999999999999 81\n")


def c97b(q: int) -> str:
    return f"{q}\n" + "".join(f"1000000000000000000 2{i:017d}\n" for i in range(q))


def empty_board(size: int, width: int | None = None) -> str:
    width = width or size
    return f"{size} {width}\n" + ("." * width + "\n") * size


def steiner_graph(queries: int | None = None) -> str:
    n, k = 60, 10
    edges = []
    for u in range(1, n + 1):
        for v in range(u + 1, n + 1):
            edges.append((u, v, 1))
            if len(edges) == 500:
                break
        if len(edges) == 500:
            break
    first = f"{n} 500 {k}" + (f" {queries}" if queries is not None else "") + "\n"
    data = first + "".join(f"{u} {v} {w}\n" for u, v, w in edges) + "1 2 3 4 5 6 7 8 9 10\n"
    if queries is not None:
        data += "1023\n" * queries
    return data


def nice_decomposition(limit: int) -> str:
    # Nine width-15 branches plus their full-bag joins and the empty filler
    # use about 1.97 million potential states: close to the stated 2M budget
    # while t is also close to 200K.
    nodes = []
    roots = []
    branches = 9 if limit > 10_000 else 2
    for _ in range(branches):
        nodes.append("L")
        child = len(nodes)
        for vertex in range(1, 17):
            nodes.append(f"I {child} {vertex}")
            child = len(nodes)
        roots.append(child)
    child = roots[0]
    for root in roots[1:]:
        nodes.append(f"J {child} {root}")
        child = len(nodes)
    for vertex in range(1, 17):
        nodes.append(f"F {child} {vertex}")
        child = len(nodes)
    for vertex in range(17, 61):
        nodes.append(f"I {child} {vertex}")
        child = len(nodes)
        nodes.append(f"F {child} {vertex}")
        child = len(nodes)
    target = max(len(nodes), limit)
    if (target - len(nodes)) & 1:
        target -= 1
    while len(nodes) < target:
        nodes.append("L")
        leaf = len(nodes)
        nodes.append(f"J {child} {leaf}")
        child = len(nodes)
    return "60 0\n" + "1 " * 59 + "1\n" + f"{len(nodes)}\n" + "\n".join(nodes) + "\n"


def c99a(q: int) -> str:
    return f"{q}\n" + "".join(f"0 999999999999999999 171 {i % 50 + 1}\n" for i in range(q))


def c99b(q: int) -> str:
    return f"{q}\n" + "".join(f"1000000000000000000 2{i:017d} 171\n" for i in range(q))


def c99c(_: int) -> str:
    return "1000000000000000000 5 5\n" + ".....\n" * 5


def c99d(height: int) -> str:
    rows = [list(".......") for _ in range(height)]
    rows[height // 2][3] = "T"
    return f"{height} 7\n" + "".join("".join(row) + "\n" for row in rows)


def repeated(expected: str):
    def check(out: str, size: int) -> None:
        tokens = out.split()
        assert len(tokens) == size and all(token == expected for token in tokens)
    return check


def one_mod_integer(out: str, _: int) -> None:
    tokens = out.split()
    assert len(tokens) == 1
    assert 0 <= int(tokens[0]) < MOD


def one_exact(expected: int):
    def check(out: str, _: int) -> None:
        assert out.strip() == str(expected)
    return check


CASES = [
    Case(97, "a_digit_sum_range", c97a, repeated(str(DIGIT_SUM_18_81)), 10_000),
    Case(97, "b_forbidden_decimal_pattern", c97b, repeated("1000000000000000000"), 1_000),
    Case(97, "c_obstacle_domino_tilings", empty_board, one_mod_integer, 12),
    Case(97, "d_grid_independent_sets", empty_board, one_mod_integer, 14),
    Case(98, "a_tower_domino_tilings", lambda _: "1000000000000000000 6\n", one_mod_integer, 1),
    Case(98, "b_connected_cell_sets", lambda h: empty_board(h, 7), one_mod_integer, 30),
    Case(98, "c_terminal_steiner_network", lambda _: steiner_graph(), one_exact(9), 1),
    Case(98, "d_nice_decomposition_independent_set", nice_decomposition, one_exact(60), 199_999),
    Case(99, "a_checksum_digit_sum", c99a, repeated("0"), 1_000),
    Case(99, "b_serial_filter", c99b, repeated("0"), 500),
    Case(99, "c_repeating_domino_tower", c99c, one_mod_integer, 1),
    Case(99, "d_connected_reserve", c99d, one_mod_integer, 30),
    Case(99, "e_terminal_backbone", lambda q: steiner_graph(q), repeated("9"), 1_000),
    Case(99, "f_decomposition_profit", nice_decomposition, one_exact(0), 199_999),
]


def solution(section: int, slug: str, extension: str) -> Path:
    problems = next(ROOT.glob(f"sections/{section:02d}_*/problems"))
    return problems / slug / f"solution.{extension}"


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
    with tempfile.TemporaryDirectory(prefix="advanced-97-99-") as td:
        for case in selected:
            size = case.full_size if args.profile == "full" else max(2, case.full_size // 100)
            data = case.make(size)
            outputs = {}
            binary = Path(td) / f"{case.section}_{case.slug}"
            if args.lang in ("cpp", "both"):
                subprocess.run(["g++", "-std=c++20", "-O2", "-pipe", str(solution(case.section, case.slug, "cpp")), "-o", str(binary)], check=True)
                outputs["cpp"], elapsed, rss = run([str(binary)], data, args.timeout)
                case.check(outputs["cpp"], size)
                print(f"{case.section}-{case.slug} cpp {elapsed:.3f}s, {rss / 1024:.1f} MiB")
            if args.lang in ("py", "both"):
                outputs["py"], elapsed, rss = run(["python3", str(solution(case.section, case.slug, "py"))], data, args.timeout)
                case.check(outputs["py"], size)
                print(f"{case.section}-{case.slug} py  {elapsed:.3f}s, {rss / 1024:.1f} MiB")
            if len(outputs) == 2:
                assert outputs["cpp"].split() == outputs["py"].split()
            digest = hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12]
            print(f"  invariant OK, output sha256={digest}")


if __name__ == "__main__":
    main()
