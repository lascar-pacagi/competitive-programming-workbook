"""Full-limit invariant tests for Sections 85--87."""
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


def zero_matrix(n: int, forbidden: bool = False) -> str:
    rows = []
    for i in range(n):
        row = ["0"] * n
        if forbidden and i == 0:
            row[0] = "-1"
        rows.append(" ".join(row))
    return "\n".join(rows) + "\n"


def c85a(n: int) -> str:
    return f"{n}\n{zero_matrix(n)}"


def c85b(n: int) -> str:
    return f"{n} {n}\n{zero_matrix(n, True)}"


def zero(out: str, _: int) -> None:
    assert out.strip() == "0"


def dense_odd_edges(n: int, limit: int = 100_000) -> list[tuple[int, int]]:
    edges = []
    for u in range(1, n):
        for v in range(u + 1, n):
            edges.append((u, v))
            if len(edges) == limit:
                return edges
    return edges


def c85c(n: int) -> str:
    edges = dense_odd_edges(n)
    return f"{n} {len(edges)}\n" + "".join(f"{u} {v}\n" for u, v in edges)


def odd_clique_pairs(out: str, n: int) -> None:
    assert out.strip() == str((n - 1) // 2)


def c85d(n: int) -> str:
    k = 200_000 if n == 500 else 2_000
    skills = " ".join(map(str, range(n)))
    allowed = " ".join(map(str, range(1, k + 1)))
    return f"{n} {k}\n{skills}\n{allowed}\n"


def half(out: str, n: int) -> None:
    assert out.strip() == str(n // 2)


def star_edges(n: int, m: int) -> list[tuple[int, int, int]]:
    edges = [(1, v, 1) for v in range(2, n + 1)]
    edges.extend((1, 2, 1) for _ in range(m - len(edges)))
    return edges


def edge_rows(edges: list[tuple[int, ...]]) -> str:
    return "".join(" ".join(map(str, edge)) + "\n" for edge in edges)


def c86a(q: int) -> str:
    n, m = 80, 1000
    queries = "".join("3 4\n" if i % 2 == 0 else "1 2\n" for i in range(q))
    return f"{n} {m} {q}\n{edge_rows(star_edges(n, m))}{queries}"


def k86a(out: str, q: int) -> None:
    assert out.split() == ["1" if i % 2 == 0 else "922" for i in range(q)]


def c86b(_: int) -> str:
    n, m = 150, 70
    return f"{n} {m}\n" + "".join(f"{i} {i + 1} {i}\n" for i in range(1, m + 1))


def seventy(out: str, _: int) -> None:
    assert out.strip() == "70"


def c86c(_: int) -> str:
    n1 = n2 = 150
    m = 60
    return f"{n1} {n2} {m}\n" + "".join(f"{i} {i + 1} {i} {i + 1}\n" for i in range(1, m + 1))


def sixty(out: str, _: int) -> None:
    assert out.strip() == "60"


def arborescence_case(_: int) -> str:
    n, m = 500, 10_000
    edges = [(1, v, 1) for v in range(2, n + 1)]
    edges.extend((v, v + 1, 0) for v in range(2, n))
    edges.append((n, 2, 0))
    edges.extend((2 + i % (n - 1), 2 + i % (n - 1), -1_000_000_000) for i in range(m - len(edges)))
    return f"{n} {m} 1\n{edge_rows(edges)}"


def one(out: str, _: int) -> None:
    assert out.strip() == "1"


def c87a(n: int) -> str:
    boundary = n * (n - 1)
    rows = []
    for i in range(n):
        row = [str(i * (n - 1) + j) for j in range(n - 1)]
        row.append(str(boundary + i))
        rows.append(" ".join(row))
    return f"{n}\n" + "\n".join(rows) + "\n"


def k87a(out: str, n: int) -> None:
    assert out.strip() == str(n * (n - 1))


def c87b(n: int) -> str:
    edges = dense_odd_edges(n)
    return f"{n} {len(edges)}\n" + "".join(f"{u} {v}\n" for u, v in edges)


def two(out: str, _: int) -> None:
    assert out.strip() == "2"


def c87c(q: int) -> str:
    n, m = 80, 1000
    queries = "".join(f"{(0, 1, 921, 922)[i % 4]}\n" for i in range(q))
    return f"{n} {m} {q}\n{edge_rows(star_edges(n, m))}{queries}"


def k87c(out: str, q: int) -> None:
    expected = ("0", "3159", "3159", "3160")
    assert out.split() == [expected[i % 4] for i in range(q)]


def c87d(_: int) -> str:
    n, m = 150, 70
    return f"{n} {m}\n" + "".join(f"{i} {i + 1} {i}\n" for i in range(1, m + 1))


def no(out: str, _: int) -> None:
    assert out.strip() == "NO"


def c87f(_: int) -> str:
    n, m = 150, 60
    return f"{n} {m}\n" + "".join(f"{i} {i + 1} {i} {i + 1}\n" for i in range(1, m + 1))


CASES = [
    AdvancedCase(85, "a_assignment_cost", c85a, zero, 350),
    AdvancedCase(85, "b_forbidden_profit_assignment", c85b, zero, 350),
    AdvancedCase(85, "c_general_pairing", c85c, odd_clique_pairs, 500),
    AdvancedCase(85, "d_compatibility_pairing", c85d, half, 500),
    AdvancedCase(86, "a_all_pairs_cut_queries", c86a, k86a, 200_000),
    AdvancedCase(86, "b_rainbow_forest", c86b, seventy, 70),
    AdvancedCase(86, "c_dual_forest", c86c, sixty, 60),
    AdvancedCase(86, "d_directed_arborescence", arborescence_case, one, 10_000),
    AdvancedCase(87, "a_bottleneck_assignment", c87a, k87a, 500),
    AdvancedCase(87, "b_roommate_rescue", c87b, two, 500),
    AdvancedCase(87, "c_cut_threshold_pairs", c87c, k87c, 200_000),
    AdvancedCase(87, "d_rainbow_spanning_tree", c87d, no, 70),
    AdvancedCase(87, "e_broadcast_backbone", arborescence_case, one, 10_000),
    AdvancedCase(87, "f_two_map_forest", c87f, no, 60),
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
    with tempfile.TemporaryDirectory(prefix="advanced-85-87-") as td:
        for case in selected:
            size = case.full_size if args.profile == "full" else max(20, case.full_size // 10)
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
