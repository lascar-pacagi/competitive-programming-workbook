"""Adversarial full-limit tests for the published kernels in Problems 41--50."""
from __future__ import annotations

import argparse
import hashlib
import math
import subprocess
import tempfile
from pathlib import Path

from stress_finale_round6 import Case, run

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sections/100_grandmaster_finale/problems"


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


def c41(size: int) -> str:
    vertices = max(4, size // 2)
    vertices -= vertices % 2
    polygon = primitive_polygon(vertices)
    q = size
    rows = "".join(f"{x} {y}\n" for x, y in polygon)
    queries = "".join("0 0\n" if i % 2 == 0 else "100000000 100000000\n" for i in range(q))
    return f"{vertices} {vertices} {q}\n{rows}{rows}{queries}"


def k41(out: str, size: int) -> None:
    assert out.split() == ["YES" if i % 2 == 0 else "NO" for i in range(size)]


RADIUS = 900_000.0


def c42(n: int) -> str:
    rows = []
    for i in range(n):
        angle = 2.0 * math.pi * i / n
        rows.append(f"{RADIUS * math.cos(angle):.9f} {RADIUS * math.sin(angle):.9f}\n")
    return f"{n}\n" + "".join(rows)


def k42(out: str, n: int) -> None:
    expected = RADIUS * math.cos(math.pi / n)
    assert abs(float(out) - expected) <= 2e-3, (out, expected)


def c43(n: int) -> str:
    return f"{n}\n" + "".join(f"{i} {i * i}\n" for i in range(n))


def k43(out: str, n: int) -> None:
    # Consecutive parabola points are the unique lightest edges across prefix cuts.
    expected = sum(math.hypot(1, 2 * i + 1) for i in range(n - 1))
    assert abs(float(out) - expected) <= 1e-6 * max(1.0, expected), (out, expected)


def c44(n: int) -> str:
    return f"{n}\n" + "".join(f"0 {-i} 1 {i}\n" for i in range(1, n + 1))


def k44(out: str, n: int) -> None:
    assert out.strip() == str(2 * (n - 1))


def c45(size: int) -> str:
    n = size if size % 2 == 0 else size - 1
    polygon = primitive_polygon(n)
    rows = "".join(f"{x} {y}\n" for x, y in polygon)
    x, y = polygon[0]
    queries = "".join(f"{x} {y}\n" if i % 2 == 0 else "100000000 100000000\n" for i in range(size))
    return f"{n} {size}\n{rows}{queries}"


def k45(out: str, size: int) -> None:
    assert out.split() == ["BOUNDARY" if i % 2 == 0 else "OUT" for i in range(size)]


def c46(q: int) -> str:
    return f"{q}\n" + "1000000000000000000 012345678901234567\n" * q


def k46(out: str, q: int) -> None:
    assert out.split() == ["1000000000000000001"] * q


def c47(_: int) -> str:
    # The dense 32-state transfer is exponentiated for 60 bits. The board has
    # odd area, so the exact answer is zero without reproducing the algorithm.
    return "999999999999999999 5 5\n" + ".....\n" * 5


def k47(out: str, _: int) -> None:
    assert out.strip() == "0"


def c48(q: int) -> str:
    edges = []
    for u in range(1, 33):
        for v in range(u + 1, 33):
            edges.append((u, v, 1))
    edges += [(33, i, 1) for i in range(1, 5)]
    assert len(edges) == 500
    masks = [1 + i % 1023 for i in range(q)]
    return (f"60 500 10 {q}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in edges)
            + "1 2 3 4 5 6 7 8 9 10\n" + "".join(f"{m}\n" for m in masks))


def k48(out: str, q: int) -> None:
    masks = [1 + i % 1023 for i in range(q)]
    assert out.split() == [str(m.bit_count() - 1) for m in masks]


def c49(target: int) -> str:
    # One width-15 branch forces all 2^15 states; empty-bag joins then force
    # the maximum decomposition-node count without creating unsafe huge output.
    rows = ["L\n"]
    child = 1
    for v in range(1, 16):
        rows.append(f"I {child} {v}\n")
        child = len(rows)
    for v in range(1, 16):
        rows.append(f"F {child} {v}\n")
        child = len(rows)
    while len(rows) + 2 <= target:
        rows.append("L\n")
        leaf = len(rows)
        rows.append(f"J {child} {leaf}\n")
        child = len(rows)
    return "15 0\n" + "1 " * 14 + f"1\n{len(rows)}\n" + "".join(rows)


def k49(out: str, _: int) -> None:
    assert out.strip() == "0"


def c50(size: int) -> str:
    n = size
    u = min(n, 65_535)
    v = min(n, 87_381)
    edges = "".join(f"{i // 2} {i}\n" for i in range(2, n + 1))
    queries = f"{u} {v} {u} {v}\n" * size
    return f"{n} {size}\n" + "a" * n + f"\n{edges}{queries}"


def depth(x: int) -> int:
    return x.bit_length() - 1


def k50(out: str, size: int) -> None:
    u = min(size, 65_535)
    v = min(size, 87_381)
    a, b = u, v
    while a != b:
        if a > b:
            a //= 2
        else:
            b //= 2
    length = depth(u) + depth(v) - 2 * depth(a) + 1
    assert out.split() == [token for _ in range(size) for token in (str(length), "0")]


CASES = [
    Case("41_moving_convex_robots", c41, k41, 200_000),
    Case("42_safe_radius_region", c42, k42, 200_000),
    Case("43_circle_network_bottleneck", c43, k43, 2_500),
    Case("44_rectangle_coverage_moments", c44, k44, 50_000),
    Case("45_offline_dynamic_hull_queries", c45, k45, 200_000),
    Case("46_digit_language_arithmetic", c46, k46, 1_000),
    Case("47_periodic_connected_tiling", c47, k47, 1),
    Case("48_prize_steiner_frontier", c48, k48, 1_000),
    Case("49_treewidth_connected_cover", c49, k49, 199_999),
    Case("50_chronicle_path_dictionary", c50, k50, 100_000),
]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=("quick", "full"), default="quick")
    parser.add_argument("--problem", action="append")
    parser.add_argument("--lang", choices=("cpp", "py", "both"), default="both")
    parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args()
    wanted = set(args.problem or [])
    with tempfile.TemporaryDirectory(prefix="finale-r5-") as td:
        for case in [c for c in CASES if not wanted or c.slug[:2] in wanted]:
            if args.profile == "full" or case.slug.startswith("47_"):
                size = case.full_size
            else:
                size = max(4, int(case.full_size * .01))
                if case.slug.startswith(("41_", "45_")):
                    size += size % 2
            data = case.make(size)
            outputs: dict[str, str] = {}
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
                if case.slug.startswith(("42_", "43_")):
                    assert math.isclose(float(outputs["cpp"]), float(outputs["py"]), rel_tol=1e-8, abs_tol=2e-3)
                else:
                    assert outputs["cpp"].split() == outputs["py"].split()
            digest = hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12]
            print(f"  invariant OK, output sha256={digest}")


if __name__ == "__main__":
    main()
