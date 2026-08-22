"""Full-limit invariant tests for Sections 79--81."""
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


def rows(edges: list[tuple[int, int]]) -> str:
    return "".join(f"{u} {v}\n" for u, v in edges)


def directed_path_edges(n: int, m: int) -> list[tuple[int, int]]:
    edges = [(i, i + 1) for i in range(1, n)]
    edges.extend([(1, 2)] * (m - len(edges)))
    return edges


def undirected_path_edges(n: int, m: int) -> list[tuple[int, int]]:
    return directed_path_edges(n, m)


def reverse_chain_edges(n: int, m: int) -> list[tuple[int, int]]:
    edges = [(1, n)] + [(i, i - 1) for i in range(n, 2, -1)]
    edges.extend([(1, n)] * (m - len(edges)))
    return edges


def c79a(n: int) -> str:
    edges = directed_path_edges(n, n)
    return f"{n} {len(edges)}\n{rows(edges)}"


def k79a(out: str, n: int) -> None:
    assert out.split() == [str(n), "1", "1"]


def c79b(n: int) -> str:
    clauses = [(1, 1), (-1, -1)]
    clauses.extend((i, i) for i in range(2, n))
    assert len(clauses) == n
    return f"{n} {n}\n{rows(clauses)}"


def no(out: str, _: int) -> None:
    assert out.strip() == "NO"


def c79c(n: int) -> str:
    return f"{n} {n}\n" + "1 1\n" * n


def k79c(out: str, n: int) -> None:
    assert out.split() == ["1"] * (n + 1)


def c79d(n: int) -> str:
    edges = reverse_chain_edges(n, 10_000 if n == 1_500 else max(n, 100))
    return f"{n} {len(edges)}\n{rows(edges)}"


def zero_list(out: str, _: int) -> None:
    assert out.split() == ["0"]


def c80a(n: int) -> str:
    edges = undirected_path_edges(n, n)
    queries = "".join(f"1 {n}\n" if i % 2 == 0 else "1 2\n" for i in range(n))
    return f"{n} {len(edges)} {n}\n{rows(edges)}{queries}"


def k80a(out: str, n: int) -> None:
    expected = str(n - 2)
    assert out.split() == [expected if i % 2 == 0 else "0" for i in range(n)]


def c80b(n: int) -> str:
    edges = undirected_path_edges(n, n)
    return f"{n} {len(edges)}\n{rows(edges)}"


def k80b(out: str, n: int) -> None:
    assert list(map(int, out.split())) == [(v - 1) * (n - v) for v in range(1, n + 1)]


def c80c(n: int) -> str:
    edges = undirected_path_edges(n, n)
    middle = n // 2
    queries = "".join(f"1 {n} {middle}\n" if i % 2 == 0 else f"1 2 {n}\n" for i in range(n))
    return f"{n} {len(edges)} {n}\n{rows(edges)}{queries}"


def alternating_yes_no(out: str, n: int) -> None:
    assert out.split() == ["YES" if i % 2 == 0 else "NO" for i in range(n)]


def c80d(n: int) -> str:
    edges = undirected_path_edges(n, n)
    return f"{n} {len(edges)}\n{rows(edges)}"


def one(out: str, _: int) -> None:
    assert out.strip() == "1"


def c81a(n: int) -> str:
    edges = directed_path_edges(n, n)
    return f"{n} {len(edges)}\n{rows(edges)}"


def c81b(n: int) -> str:
    edges = directed_path_edges(n, n)
    return f"{n} {len(edges)}\n{rows(edges)}"


def base26(value: int, width: int) -> str:
    chars = ["a"] * width
    for i in range(width - 1, -1, -1):
        chars[i] = chr(97 + value % 26)
        value //= 26
    return "".join(chars)


def archive_words(total: int) -> list[str]:
    return ["a" + base26(i, 6) + "a" for i in range(total // 8)]


def c81c(total: int) -> str:
    words = archive_words(total)
    return f"{len(words)}\n" + "\n".join(words) + "\n"


def k81c(out: str, total: int) -> None:
    assert out.split() == archive_words(total)


def c81d(n: int) -> str:
    edges = [(i, i + 1) for i in range(1, n)] + [(n, 1)]
    return f"{n} {n}\n{rows(edges)}"


def yes(out: str, _: int) -> None:
    assert out.strip() == "YES"


def c81e(n: int) -> str:
    edges = undirected_path_edges(n, n)
    middle = n // 2
    queries = "".join(f"1 {n} {middle}\n" if i % 2 == 0 else f"1 2 {n}\n" for i in range(n))
    return f"{n} {len(edges)} {n}\n{rows(edges)}{queries}"


def k81e(out: str, n: int) -> None:
    assert out.split() == ["NO" if i % 2 == 0 else "YES" for i in range(n)]


def c81f(n: int) -> str:
    m = 10_000 if n == 1_500 else max(n, 100)
    q = 200_000 if n == 1_500 else 2_000
    edges = reverse_chain_edges(n, m)
    queries = "".join(f"{i % n + 1}\n" for i in range(q))
    return f"{n} {m} {q}\n{rows(edges)}{queries}"


def k81f(out: str, n: int) -> None:
    q = 200_000 if n == 1_500 else 2_000
    expected = [str(n if i % n == 0 else i % n) for i in range(q)]
    assert out.split() == expected


CASES = [
    AdvancedCase(79, "a_condensation_profile", c79a, k79a, 200_000),
    AdvancedCase(79, "b_clause_satisfiability", c79b, no, 200_000),
    AdvancedCase(79, "c_lexicographic_euler_trail", c79c, k79c, 200_000),
    AdvancedCase(79, "d_unavoidable_checkpoints", c79d, zero_list, 1_500),
    AdvancedCase(80, "a_bridge_distance_queries", c80a, k80a, 200_000),
    AdvancedCase(80, "b_articulation_pair_damage", c80b, k80b, 200_000),
    AdvancedCase(80, "c_mandatory_station_queries", c80c, alternating_yes_no, 200_000),
    AdvancedCase(80, "d_two_edge_completion", c80d, one, 200_000),
    AdvancedCase(81, "a_unique_sink_population", c81a, one, 200_000),
    AdvancedCase(81, "b_strong_connectivity_repairs", c81b, one, 200_000),
    AdvancedCase(81, "c_eulerian_word_chain", c81c, k81c, 200_000),
    AdvancedCase(81, "d_robbins_orientation", c81d, yes, 200_000),
    AdvancedCase(81, "e_failed_vertex_routes", c81e, k81e, 200_000),
    AdvancedCase(81, "f_dominator_subtree_queries", c81f, k81f, 1_500),
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
    with tempfile.TemporaryDirectory(prefix="advanced-79-81-") as td:
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
