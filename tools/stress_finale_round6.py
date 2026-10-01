"""Shared limit-test helpers for the finale stress tools.

This module once drove limit tests for the original Problems 51--65, which were
copies of earlier kernels.  Those packages were replaced by new problems whose
limit tests live in ``stress_finale_50_65.py``.  The generators and the
``run`` timing wrapper below are still imported by the other stress tools.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
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


def primitive_polygon(n: int) -> list[tuple[int, int]]:
    """Return an n-vertex strictly convex integer polygon with sum-zero edges."""
    assert n >= 4 and n % 2 == 0
    need = n // 2
    bound = max(2, math.ceil(math.sqrt(need * math.pi / 3)))
    upper: list[tuple[int, int]] = []
    while len(upper) < need:
        upper.clear()
        for x in range(-bound, bound + 1):
            for y in range(0, bound + 1):
                if (y > 0 or x > 0) and math.gcd(abs(x), y) == 1:
                    upper.append((x, y))
        bound += 1
    # Taking the shortest primitive vectors keeps the coordinate span small.
    upper.sort(key=lambda z: (z[0] * z[0] + z[1] * z[1], math.atan2(z[1], z[0])))
    edges = upper[:need]
    edges += [(-x, -y) for x, y in edges]
    edges.sort(key=lambda z: math.atan2(z[1], z[0]))
    points = []
    x = y = 0
    for dx, dy in edges:
        points.append((x, y))
        x += dx
        y += dy
    assert (x, y) == (0, 0)
    minx = min(x for x, _ in points)
    maxx = max(x for x, _ in points)
    miny = min(y for _, y in points)
    maxy = max(y for _, y in points)
    sx = -(minx + maxx) // 2
    sy = -(miny + maxy) // 2
    points = [(x + sx, y + sy) for x, y in points]
    assert max(max(abs(x), abs(y)) for x, y in points) < 40_000_000
    return points


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
    raise SystemExit("Use tools/stress_finale_50_65.py for Problems 50--65.")


if __name__ == "__main__":
    main()
