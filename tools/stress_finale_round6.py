"""Adversarial limit tests for the *published kernels* in finale Problems 51--65.

This is intentionally separate from random_cases.py.  It creates structured
large inputs with cheap exact invariants, compiles both references, measures
wall time, and compares their output.  It does not validate the synthesis
wrappers described only in COVERAGE.md; those wrappers are not implemented yet.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sections/100_grandmaster_finale/problems"


@dataclass
class Case:
    slug: str
    make: Callable[[int], str]
    check: Callable[[str, int], None]
    full_size: int


def repeated(expected: str, count: int) -> Callable[[str, int], None]:
    def check(output: str, _: int) -> None:
        tokens = output.split()
        assert len(tokens) == count, (len(tokens), count)
        assert all(token == expected for token in tokens)
    return check


def c51(size: int) -> str:
    n = size // 2
    q = size
    return f"{n} {q}\n" + "a\n" * n + "".join(
        f"+ {i}\n" for i in range(1, n + 1)
    ) + "? aaaa\n" * (q - n)


def k51(out: str, size: int) -> None:
    n = size // 2
    repeated(str(4 * n), size - n)(out, size)


def c52(size: int) -> str:
    half = size // 2
    return f"{half + 1} {size}\n" + "".join(
        f"+ {i} {i + 1} 0\n" for i in range(1, half + 1)
    ) + "?\n" * (size - half)


def k52(out: str, size: int) -> None:
    # The chain is connected and consistent: exactly two assignments.
    repeated("2", size - size // 2)(out, size)


def c53(size: int) -> str:
    n, m, q = 100, 1500, size
    edges = []
    for u in range(n):
        for step in range(1, 16):
            v = (u + step) % n
            if u < v:
                edges.append((u + 1, v + 1, 1 + (u * 97 + v * 31) % 10**6))
    while len(edges) < m:
        i = len(edges); u = i % n + 1; v = (i * 37 + 1) % n + 1
        if u == v: v = v % n + 1
        edges.append((u, v, i + 1))
    return f"{n} {m} {q}\n" + "".join(f"{u} {v} {w}\n" for u,v,w in edges[:m]) + "".join(f"{i % 1000000}\n" for i in range(q))


def line_count(count: int) -> Callable[[str, int], None]:
    def check(out: str, _: int) -> None:
        assert len(out.split()) == count
    return check


def size_line_count(out: str, size: int) -> None:
    assert len(out.split()) == size


def c54(_: int) -> str:
    rows = ["1 2 12 12 0 0\n" for _ in range(250)]
    rows += [f"2 1 0 12 {i % 11} 1\n" for i in range(250)]
    return "2 500\n" + "".join(rows)


def one_integer(out: str, _: int) -> None:
    assert len(out.split()) == 1 and out.strip() != "IMPOSSIBLE"


def tree_distance(size: int) -> str:
    return f"{size}\n" + "0 " * (size - 1) + "0\n" + "".join(
        f"{i} {i + 1}\n" for i in range(1, size)
    )


def k_tree_distance(out: str, size: int) -> None:
    values = list(map(int, out.split()))
    assert len(values) == size and values[0] == 0
    assert all(values[d] == size - d for d in range(1, size))


def c56(size: int) -> str:
    queries = []
    for i in range(size):
        p = "a" if i % 2 == 0 else "aa"
        queries.append(f"{p} {i + 1}\n")
    return "a" * size + f"\n{size}\n" + "".join(queries)


def k56(out: str, size: int) -> None:
    vals = list(map(int, out.split())); assert len(vals) == size
    for i, value in enumerate(vals):
        limit = size if i % 2 == 0 else size - 1
        assert value == (i + 1 if i + 1 <= limit else -1)


def c58(k: int) -> str:
    n = 1 << k; row = "1 " * (n - 1) + "1\n"
    return f"{k}\n{row}{row}"


def k58(out: str, k: int) -> None:
    vals = list(map(int, out.split())); assert len(vals) == 1 << k
    assert all(v == 1 << i.bit_count() for i, v in enumerate(vals))


def c59(size: int) -> str:
    p = "1 " * (size - 1) + "1\n"
    q = "1 998244352 " + "0 " * (size - 2) if size > 1 else "1"
    return f"{size}\n{p}{q.strip()}\n"


def k59(out: str, size: int) -> None:
    vals = list(map(int, out.split())); assert len(vals) == size
    assert all(v == i + 1 for i, v in enumerate(vals))


def c60(size: int) -> str:
    n, k, q = 60, 10, size
    edges = [(i, i + 1, 1) for i in range(1, n)]
    i = 0
    while len(edges) < 500:
        u = i % n + 1; v = (i * 17 + 23) % n + 1; i += 1
        if u != v: edges.append((u, v, 1000000 + i))
    masks = [1 + (i * 73) % ((1 << k) - 1) for i in range(q)]
    return f"{n} 500 {k} {q}\n" + "".join(f"{u} {v} {w}\n" for u,v,w in edges) + " ".join(map(str, range(1,k+1))) + "\n" + "\n".join(map(str,masks)) + "\n"


def k60(out: str, size: int) -> None:
    assert len(out.split()) == size


def c61(_: int) -> str:
    n, w = 1000, 300
    parents = "1 " * (n - 1)
    offers = []
    for i in range(w):
        extra = " ".join(f"{2 + (i * 17 + j) % (n - 1)} {10 + j}" for j in range(15))
        offers.append(f"16 1 1 {extra}\n")
    return f"{n} {w}\n{parents.strip()}\n" + "".join(offers)


def k61(out: str, _: int) -> None:
    assert out.strip() == "300"


def c62(size: int) -> str:
    return f"{size}\n" + "".join(f"{i} {i} 1\n" for i in range(1, size + 1))


def k62(out: str, size: int) -> None:
    assert out.split() == [str(size), "1"]


def c63(_: int) -> str:
    return "999999999999999999 5 5\n" + ".....\n" * 5


def k63(out: str, _: int) -> None:
    assert out.strip() == "0"


def c64(size: int) -> str:
    # One real vertex path, then many empty-bag joins. All joins have identical bags.
    target = size if size % 2 else size - 1
    rows = ["L\n", "I 1 1\n", "F 2 1\n"]
    current = 3
    while len(rows) + 2 <= target:
        rows.append("L\n"); leaf = len(rows)
        rows.append(f"J {current} {leaf}\n"); current = len(rows)
    return f"1 0\n5\n{len(rows)}\n" + "".join(rows)


def k64(out: str, _: int) -> None:
    assert out.strip() == "0"


def c65(size: int) -> str:
    n = size
    values = " ".join(map(str, range(n, 0, -1)))
    edges = "".join(f"{i} {i + 1} {i}\n" for i in range(1, n))
    queries = "".join(f"1 {n} {i % n + 1}\n" for i in range(n))
    return f"{n} {n - 1} {n}\n{values}\n{edges}{queries}"


def k65(out: str, size: int) -> None:
    vals = list(map(int, out.split())); assert vals == list(range(1, size + 1))


CASES = [
    Case("51_versioned_path_pattern_census", c51, k51, 100000),
    Case("52_temporal_geometric_alliances", c52, k52, 200000),
    Case("53_colored_cut_tree_summaries", c53, size_line_count, 200000),
    Case("54_exact_fleet_circulation", c54, one_integer, 1),
    Case("55_palindromic_paths_through_centroids", tree_distance, k_tree_distance, 100000),
    Case("56_congruent_substring_selection", c56, k56, 100000),
    Case("57_polynomial_tree_colorings", tree_distance, k_tree_distance, 100000),
    Case("58_multiplicative_set_partitions", c58, k58, 16),
    Case("59_factorized_recurrence_oracle", c59, k59, 200000),
    Case("60_delaunay_terminal_backbone", c60, k60, 1000),
    Case("61_moving_half_plane_assignment", c61, k61, 1),
    Case("62_historical_rectangle_quantiles", c62, k62, 100000),
    Case("63_periodic_forbidden_frontier", c63, k63, 1),
    Case("64_connected_cover_on_bags", c64, k64, 199999),
    Case("65_temporal_steiner_dictionary", c65, k65, 200000),
]


def run(command: list[str], data: str, timeout: int) -> tuple[str, float, int | None]:
    start = time.monotonic()
    wrapper = (
        "import json,resource,subprocess,sys;"
        "r=subprocess.run(json.loads(sys.argv[1]),input=sys.stdin.buffer.read(),capture_output=True);"
        "sys.stdout.buffer.write(r.stdout);sys.stderr.buffer.write(r.stderr);"
        "print('\\n__FINALE_STATS__',resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,file=sys.stderr);"
        "raise SystemExit(r.returncode)"
    )
    timed = ["python3", "-c", wrapper, json.dumps(command)]
    result = subprocess.run(timed, input=data, text=True, capture_output=True, timeout=timeout)
    elapsed = time.monotonic() - start
    if result.returncode:
        raise RuntimeError(f"{' '.join(command)} failed ({result.returncode}):\n{result.stderr[-2000:]}")
    match = re.search(r"__FINALE_STATS__ (\d+)", result.stderr)
    return result.stdout, elapsed, (int(match.group(1)) if match else None)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=("quick", "full"), default="quick")
    parser.add_argument("--problem", action="append", help="problem number, repeatable")
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--lang", choices=("cpp", "py", "both"), default="both")
    args = parser.parse_args()
    wanted = set(args.problem or [])
    cases = [c for c in CASES if not wanted or c.slug[:2] in wanted]
    scale = 1.0 if args.profile == "full" else 0.01
    with tempfile.TemporaryDirectory(prefix="finale-r6-") as tmp:
        temp = Path(tmp)
        for case in cases:
            size = case.full_size if args.profile == "full" else max(1, int(case.full_size * scale))
            if case.slug.startswith("58_"): size = 16 if args.profile == "full" else 10
            if case.slug.startswith(("54_", "61_", "63_")): size = 1
            data = case.make(size)
            outputs = {}
            if args.lang in ("cpp", "both"):
                binary = temp / case.slug
                subprocess.run(["g++", "-std=c++20", "-O2", "-pipe", str(BASE/case.slug/"solution.cpp"), "-o", str(binary)], check=True)
                outputs["cpp"], elapsed, rss = run([str(binary)], data, args.timeout)
                case.check(outputs["cpp"], size)
                memory = f", {rss / 1024:.1f} MiB" if rss is not None else ""
                print(f"{case.slug} cpp {elapsed:.3f}s{memory}")
            if args.lang in ("py", "both"):
                outputs["py"], elapsed, rss = run(["python3", str(BASE/case.slug/"solution.py")], data, args.timeout)
                case.check(outputs["py"], size)
                memory = f", {rss / 1024:.1f} MiB" if rss is not None else ""
                print(f"{case.slug} py  {elapsed:.3f}s{memory}")
            if len(outputs) == 2:
                assert outputs["cpp"].split() == outputs["py"].split()
            digest = hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12]
            print(f"  invariant OK, output sha256={digest}")


if __name__ == "__main__":
    main()
