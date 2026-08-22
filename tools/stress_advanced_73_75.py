"""Full-limit invariant tests for Sections 73--75."""
from __future__ import annotations

import argparse
import hashlib
import math
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from stress_finale_round6 import run
from stress_finale_41_50 import primitive_polygon

ROOT = Path(__file__).resolve().parents[1]


@dataclass
class AdvancedCase:
    section: int
    slug: str
    make: callable
    check: callable
    full_size: int
    floating: bool = False


def polygon_area2(p: list[tuple[int, int]]) -> int:
    return abs(sum(p[i][0] * p[(i + 1) % len(p)][1] - p[i][1] * p[(i + 1) % len(p)][0] for i in range(len(p))))


def polygon_rows(p: list[tuple[int, int]]) -> str:
    return "".join(f"{x} {y}\n" for x, y in p)


def c73a(n: int) -> str:
    p = primitive_polygon(n - n % 2)
    return f"{len(p)}\n{polygon_rows(p)}"


def k73a(out: str, n: int) -> None:
    p = primitive_polygon(n - n % 2)
    assert out.split() == [str(len(p)), str(polygon_area2(p))]


def diameter_vector(p: list[tuple[int, int]]) -> tuple[int, int]:
    half = len(p) // 2
    return max(
        ((p[(i + half) % len(p)][0] - p[i][0], p[(i + half) % len(p)][1] - p[i][1]) for i in range(half)),
        key=lambda z: z[0] * z[0] + z[1] * z[1],
    )


def c73b(n: int) -> str:
    p = primitive_polygon(n - n % 2)
    return f"{len(p)}\n{polygon_rows(p)}"


def k73b(out: str, n: int) -> None:
    p = primitive_polygon(n - n % 2)
    dx, dy = diameter_vector(p)
    assert out.strip() == str(dx * dx + dy * dy)


def c73c(size: int) -> str:
    n = size // 2
    n -= n % 2
    p = primitive_polygon(n)
    rows = polygon_rows(p)
    queries = "".join("0 0\n" if i % 2 == 0 else "100000000 100000000\n" for i in range(size))
    return f"{n} {n} {size}\n{rows}{rows}{queries}"


def yes_no(out: str, size: int) -> None:
    assert out.split() == ["YES" if i % 2 == 0 else "NO" for i in range(size)]


def c73d(total: int) -> str:
    n = total // 2
    n -= n % 2
    p = primitive_polygon(n)
    dx, dy = diameter_vector(p)
    q = [(x + 2 * dx, y + 2 * dy) for x, y in p]
    return f"{n}\n{polygon_rows(p)}{n}\n{polygon_rows(q)}"


def k73d(out: str, total: int) -> None:
    p = primitive_polygon((total // 2) - (total // 2) % 2)
    dx, dy = diameter_vector(p)
    assert math.isclose(float(out), math.hypot(dx, dy), rel_tol=1e-9, abs_tol=1e-6)


def c74a(total: int) -> str:
    h = total // 2
    v = total - h
    horizontal = "".join(f"0 {v} {y}\n" for y in range(1, h + 1))
    vertical = "".join(f"{x} 1 {h}\n" for x in range(1, v + 1))
    return f"{h} {v}\n{horizontal}{vertical}"


def crossings(out: str, total: int) -> None:
    h = total // 2
    assert out.strip() == str(h * (total - h))


def c74b(n: int) -> str:
    return f"{n}\n" + "".join(f"{i} {-i} {i + 1} {i + 1}\n" for i in range(n))


def union_area(out: str, n: int) -> None:
    assert out.strip() == str(n * n)


def c74c(n: int) -> str:
    return f"{n}\n" + "".join(f"{i} {i}\n" for i in range(n))


def closest(out: str, _: int) -> None:
    assert out.strip() == "2"


def c74d(n: int) -> str:
    return f"{n}\n" + "".join(f"{2 * i} {-i} {2 * i + 1} {i + 1}\n" for i in range(n))


def union_area_perimeter(out: str, n: int) -> None:
    assert out.split() == [str(n * n), str(2 * n * n + 2 * n)]


def c75a(n: int) -> str:
    p = primitive_polygon(n - n % 2)
    return f"{len(p)}\n{polygon_rows(p)}"


def k75a(out: str, n: int) -> None:
    p = primitive_polygon(n - n % 2)
    assert out.split() == [str(polygon_area2(p)), str(len(p))]


def c75b(n: int) -> str:
    return f"{n}\n" + "".join(f"{i} {i * i}\n" for i in range(n))


def k75b(out: str, n: int) -> None:
    span = n - 1
    assert out.strip() == str(span * (span // 2) * (span - span // 2))


def c75c(size: int) -> str:
    n = size // 2
    n -= n % 2
    p = primitive_polygon(n)
    rows = polygon_rows(p)
    queries = "".join("0 0\n" if i % 2 == 0 else "100000000 100000000\n" for i in range(size))
    return f"{n} {n} {size}\n{rows}{rows}{queries}"


def c75d(total: int) -> str:
    h = total // 2
    v = total - h
    horizontal = "".join(f"0 {v} {y} 1000\n" for y in range(1, h + 1))
    vertical = "".join(f"{x} 1 {h} -1000\n" for x in range(1, v + 1))
    return f"{h} {v}\n{horizontal}{vertical}"


def weighted_crossings(out: str, total: int) -> None:
    h = total // 2
    assert out.strip() == str(-1_000_000 * h * (total - h))


def c75e(n: int) -> str:
    return f"{n}\n" + "".join(f"0 {-i} 1 {i}\n" for i in range(1, n + 1))


def twice_area(out: str, n: int) -> None:
    assert out.strip() == str(2 * (n - 1))


def c75f(size: int) -> str:
    n = size - size % 2
    p = primitive_polygon(n)
    x, y = p[0]
    queries = "".join(f"{x} {y}\n" if i % 2 == 0 else "100000000 100000000\n" for i in range(size))
    return f"{n} {size}\n{polygon_rows(p)}{queries}"


def fortress(out: str, size: int) -> None:
    assert out.split() == ["BOUNDARY" if i % 2 == 0 else "OUT" for i in range(size)]


CASES = [
    AdvancedCase(73, "a_hull_statistics", c73a, k73a, 200_000),
    AdvancedCase(73, "b_farthest_pair", c73b, k73b, 200_000),
    AdvancedCase(73, "c_sum_polygon_queries", c73c, yes_no, 200_000),
    AdvancedCase(73, "d_convex_polygon_distance", c73d, k73d, 400_000, True),
    AdvancedCase(74, "a_orthogonal_crossings", c74a, crossings, 200_000),
    AdvancedCase(74, "b_rectangle_union", c74b, union_area, 50_000),
    AdvancedCase(74, "c_closest_pair", c74c, closest, 200_000),
    AdvancedCase(74, "d_rectangle_union_perimeter", c74d, union_area_perimeter, 200_000),
    AdvancedCase(75, "a_convex_lattice_shield", c75a, k75a, 200_000),
    AdvancedCase(75, "b_maximum_triangle", c75b, k75b, 5_000),
    AdvancedCase(75, "c_robot_collision_translations", c75c, yes_no, 200_000),
    AdvancedCase(75, "d_weighted_crossings", c75d, weighted_crossings, 200_000),
    AdvancedCase(75, "e_double_painted_map", c75e, twice_area, 50_000),
    AdvancedCase(75, "f_fortress_queries", c75f, fortress, 200_000),
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
    selected = [c for c in CASES if (not sections or c.section in sections) and (not problems or c.slug[0] in problems)]
    with tempfile.TemporaryDirectory(prefix="advanced-73-75-") as td:
        for case in selected:
            size = case.full_size if args.profile == "full" else max(20, case.full_size // 100)
            size -= size % 2
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
                if case.floating:
                    assert math.isclose(float(outputs["cpp"]), float(outputs["py"]), rel_tol=1e-9, abs_tol=1e-6)
                else:
                    assert outputs["cpp"].split() == outputs["py"].split()
            digest = hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12]
            print(f"  invariant OK, output sha256={digest}")


if __name__ == "__main__":
    main()
