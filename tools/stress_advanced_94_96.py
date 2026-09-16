"""Full-limit invariant tests for Sections 94--96."""
from __future__ import annotations

import argparse
import hashlib
import math
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

from stress_finale_round6 import run

ROOT = Path(__file__).resolve().parents[1]


@dataclass
class Case:
    section: int
    slug: str
    make: callable
    check: callable
    full_size: int


def hpi_case(n: int) -> str:
    lines = [(-1, -1, 1, -1), (1, -1, 1, 1), (1, 1, -1, 1), (-1, 1, -1, -1)]
    for i in range(n - 4):
        dx = i % 997 + 1
        dy = i // 997 + 1
        px, py = 100 * dy, -100 * dx
        lines.append((px, py, px + dx, py + dy))
    # The far half-planes contain [-1,1]^2; the four first lines make it exact.
    return f"{n}\n" + "".join(f"{a} {b} {c} {d}\n" for a, b, c, d in lines)


def regular_polygon(n: int) -> str:
    radius = 1000.0
    return f"{n}\n" + "".join(
        f"{radius * math.cos(2 * math.pi * i / n):.12f} {radius * math.sin(2 * math.pi * i / n):.12f}\n"
        for i in range(n)
    )


def parabola(n: int) -> str:
    return f"{n}\n" + "".join(f"{i} {i * i}\n" for i in range(1, n + 1))


def fixed(_: int, text: str) -> str:
    return text


def one_float(out: str) -> float:
    tokens = out.split()
    assert len(tokens) == 1
    value = float(tokens[0])
    assert math.isfinite(value)
    return value


def near(expected: float, rel: float = 1e-7, abs_tol: float = 1e-7):
    def check(out: str, _: int) -> None:
        assert math.isclose(one_float(out), expected, rel_tol=rel, abs_tol=abs_tol)
    return check


def inradius_check(out: str, n: int) -> None:
    assert math.isclose(one_float(out), 1000.0 * math.cos(math.pi / n), rel_tol=2e-8, abs_tol=2e-6)


def mec_check(out: str, _: int) -> None:
    values = list(map(float, out.split()))
    assert len(values) == 3 and all(map(math.isfinite, values))
    assert abs(values[0]) <= 2e-6 and abs(values[1]) <= 2e-6
    assert math.isclose(values[2], 1000.0, rel_tol=2e-8, abs_tol=2e-6)


def positive(out: str, _: int) -> None:
    assert one_float(out) > 0


def mst_check(out: str, n: int) -> None:
    expected = sum(math.hypot(1, 2 * i + 1) for i in range(1, n))
    assert math.isclose(one_float(out), expected, rel_tol=2e-8, abs_tol=1e-4)


CASES = [
    Case(94, "a_half_plane_region", hpi_case, near(4.0), 200_000),
    Case(94, "b_circle_overlap", lambda n: fixed(n, "0 0 1000000000\n1000000000 0 1000000000\n"), near(1.228369698608757e18, 2e-9, 1.0), 1),
    Case(94, "c_common_tangent_count", lambda n: fixed(n, "0 0 1000000000\n2000000000 0 1000000000\n"), lambda out, n: (_ for _ in ()).throw(AssertionError(out)) if out.strip() != "3" else None, 1),
    Case(94, "d_largest_inscribed_circle", regular_polygon, inradius_check, 200_000),
    Case(95, "a_minimum_enclosing_circle", regular_polygon, mec_check, 200_000),
    Case(95, "b_delaunay_radius_sum", parabola, positive, 2_500),
    Case(95, "c_euclidean_network", parabola, mst_check, 2_500),
    Case(95, "d_largest_empty_delaunay_circle", parabola, positive, 2_500),
]

INHERITED = {
    "b_round_table_clearance": (94, "d_largest_inscribed_circle"),
    "c_sensor_overlap": (94, "b_circle_overlap"),
    "d_emergency_broadcast_disk": (95, "a_minimum_enclosing_circle"),
    "f_low_cost_fiber": (95, "c_euclidean_network"),
}


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
    with tempfile.TemporaryDirectory(prefix="advanced-94-96-") as td:
        for case in selected:
            size = case.full_size if args.profile == "full" else max(4, case.full_size // 100)
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
                a, b = map(float, outputs["cpp"].split()), map(float, outputs["py"].split())
                assert all(math.isclose(x, y, rel_tol=2e-8, abs_tol=2e-6) for x, y in zip(a, b))
            digest = hashlib.sha256(next(iter(outputs.values())).encode()).hexdigest()[:12]
            print(f"  invariant OK, output sha256={digest}")
    if not sections or 96 in sections:
        for story, (section, source_slug) in INHERITED.items():
            for extension in ("cpp", "py"):
                assert solution(96, story, extension).read_bytes() == solution(section, source_slug, extension).read_bytes()
            print(f"96-{story}: byte-identical evidence inherited from {section}-{source_slug}")


if __name__ == "__main__":
    main()
