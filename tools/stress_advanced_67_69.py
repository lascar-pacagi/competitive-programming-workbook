"""Full-limit invariant tests for Sections 67--69."""
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
    full_size: int = 200_000


def chain_edges(n: int, weighted: bool = False) -> str:
    if weighted:
        return "".join(f"{i} {i + 1} 1\n" for i in range(1, n))
    return "".join(f"{i} {i + 1}\n" for i in range(1, n))


def heap_edges(n: int) -> str:
    return "".join(f"{i // 2} {i}\n" for i in range(2, n + 1))


def distance(u: int, v: int) -> int:
    answer = 0
    while u != v:
        if u > v:
            u //= 2
        else:
            v //= 2
        answer += 1
    return answer


def hard_endpoints(n: int) -> tuple[int, int]:
    u = (1 << (n.bit_length() - 1)) - 1
    return max(1, u), max(1, min(n, u + u // 3))


def c67a(q: int) -> str:
    h = q // 2
    updates = "".join(f"I {i - 1} {i}\n" for i in range(1, h + 1))
    queries = "".join(
        f"K {h} {i}\n" if i & 1 else f"C {h} {i}\n" for i in range(1, q - h + 1)
    )
    return f"200000 {q}\n{updates}{queries}"


def k67a(out: str, q: int) -> None:
    assert list(map(int, out.split())) == list(range(1, q - q // 2 + 1))


def c67b(size: int) -> str:
    h = size // 2
    updates = "".join(f"A 0 {i} {i} 1\n" for i in range(1, h + 1))
    queries = "".join(f"Q {i} {i} {i}\n" for i in range(1, size - h + 1))
    return f"{size} {size}\n" + "0 " * (size - 1) + f"0\n{updates}{queries}"


def k_ones(out: str, size: int) -> None:
    assert out.split() == ["1"] * (size - size // 2)


def connectivity_ops(size: int, component_queries: bool) -> str:
    h = size // 4
    add = "".join(f"+ {i} {i + 1}\n" for i in range(1, h + 1))
    middle = (f"S 1\n" if component_queries else f"? 1 {h + 1}\n") * h
    remove = "".join(f"- {i} {i + 1}\n" for i in range(1, h + 1))
    tail = ("S 1\n" if component_queries else "? 1 1\n") * (size - 3 * h)
    return add + middle + remove + tail


def c67c(size: int) -> str:
    return f"{size} {size}\n" + connectivity_ops(size, False)


def k67c(out: str, size: int) -> None:
    assert out.split() == ["YES"] * (size - size // 2)


def c67d(n: int) -> str:
    values = " ".join(map(str, range(1, n + 1)))
    queries = "".join(f"1 {n} {i % n + 1}\n" for i in range(n))
    return f"{n} {n}\n{values}\n{chain_edges(n)}{queries}"


def k67d(out: str, n: int) -> None:
    assert list(map(int, out.split())) == list(range(1, n + 1))


def c68a(n: int) -> str:
    u, v = hard_endpoints(n)
    functions = "1 1\n" * n
    queries = f"Q {u} {v} 0\n" * n
    return f"{n} {n}\n{functions}{heap_edges(n)}{queries}"


def k68a(out: str, n: int) -> None:
    u, v = hard_endpoints(n)
    assert out.split() == [str(distance(u, v) + 1)] * n


def c68b(n: int) -> str:
    operations = "".join("T 1\n" if i % 2 == 0 else f"Q {n}\n" for i in range(n))
    return f"{n} {n}\n{chain_edges(n)}{operations}"


def k68b(out: str, n: int) -> None:
    assert out.split() == [str(n - 1) if i % 2 == 0 else "-1" for i in range(n // 2)]


def c68c(n: int) -> str:
    big = n // 2
    q = n - big + 1
    first = f"{big} " + " ".join(map(str, range(1, big + 1))) + "\n"
    return f"{n} {q}\n{chain_edges(n, True)}{first}" + "1 1\n" * (q - 1)


def k68c(out: str, n: int) -> None:
    big = n // 2
    expected = big * (big * big - 1) // 6
    assert out.split() == [str(expected)] + ["0"] * (n - big)


def subtree_data(n: int) -> tuple[list[int], list[int]]:
    sizes = [0] * (n + 1)
    sums = [0] * (n + 1)
    for u in range(n, 0, -1):
        sizes[u] += 1
        sums[u] += u
        if u > 1:
            sizes[u // 2] += sizes[u]
            sums[u // 2] += sums[u]
    return sizes, sums


def c68d(n: int) -> str:
    return f"{n}\n" + " ".join(map(str, range(1, n + 1))) + f"\n{heap_edges(n)}"


def k68d(out: str, n: int) -> None:
    _, sums = subtree_data(n)
    assert list(map(int, out.split())) == sums[1:]


def c69a(q: int) -> str:
    h = q // 2
    updates = "".join(f"A {i - 1} {i}\n" for i in range(1, h + 1))
    queries = "".join(f"Q {h} 1 {h} {i}\n" for i in range(1, q - h + 1))
    return f"200000 {q}\n{updates}{queries}"


def k69a(out: str, q: int) -> None:
    assert list(map(int, out.split())) == list(range(1, q - q // 2 + 1))


def c69b(size: int) -> str:
    return f"{size} {size}\n" + connectivity_ops(size, True)


def k69b(out: str, size: int) -> None:
    h = size // 4
    assert out.split() == [str(h + 1)] * h + ["1"] * (size - 3 * h)


def c69c(n: int) -> str:
    u, v = hard_endpoints(n)
    matrices = "1 1 0 1\n" * n
    return f"{n} {n}\n{matrices}{heap_edges(n)}" + f"Q {u} {v}\n" * n


def k69c(out: str, n: int) -> None:
    u, v = hard_endpoints(n)
    row = ["1", str(distance(u, v) + 1), "0", "1"]
    assert out.split() == row * n


def c69d(n: int) -> str:
    operations = "".join("T 1\n" if i % 2 == 0 else f"Q {n}\n" for i in range(n))
    return f"{n} {n}\n{chain_edges(n)}{operations}"


def k69d(out: str, n: int) -> None:
    assert out.split() == [str(n - 1) if i % 2 == 0 else "0" for i in range(n // 2)]


def c69e(n: int) -> str:
    big = n // 2
    q = n - big + 1
    first = f"{big} " + " ".join(f"{i} 1" for i in range(1, big + 1)) + "\n"
    return f"{n} {q}\n{chain_edges(n, True)}{first}" + "1 1 1\n" * (q - 1)


def k69e(out: str, n: int) -> None:
    big = n // 2
    expected = big * (big * big - 1) // 6
    assert out.split() == [str(expected)] + ["0"] * (n - big)


def c69f(n: int) -> str:
    return f"{n}\n" + " ".join(map(str, range(1, n + 1))) + f"\n{heap_edges(n)}"


def k69f(out: str, n: int) -> None:
    sizes, _ = subtree_data(n)
    expected = [token for u in range(1, n + 1) for token in ("1", str(sizes[u]))]
    assert out.split() == expected


CASES = [
    AdvancedCase(67, "a_branching_multiset", c67a, k67a),
    AdvancedCase(67, "b_versioned_range_add", c67b, k_ones),
    AdvancedCase(67, "c_dynamic_connectivity", c67c, k67c),
    AdvancedCase(67, "d_tree_path_kth", c67d, k67d),
    AdvancedCase(68, "a_path_affine_composition", c68a, k68a),
    AdvancedCase(68, "b_toggle_nearest_beacon", c68b, k68b),
    AdvancedCase(68, "c_marked_pair_distances", c68c, k68c),
    AdvancedCase(68, "d_subtree_mode_sum", c68d, k68d),
    AdvancedCase(69, "a_snapshot_rank", c69a, k69a),
    AdvancedCase(69, "b_seasonal_component_size", c69b, k69b),
    AdvancedCase(69, "c_route_matrices", c69c, k69c),
    AdvancedCase(69, "d_beacon_distance_sum", c69d, k69d),
    AdvancedCase(69, "e_weighted_marked_pairs", c69e, k69e),
    AdvancedCase(69, "f_subtree_frequency_profile", c69f, k69f),
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
    with tempfile.TemporaryDirectory(prefix="advanced-67-69-") as td:
        for case in selected:
            size = case.full_size if args.profile == "full" else case.full_size // 100
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
