"""Adversarial limit tests for finale Problems 50--65.

Every case is built at the published maximum (``--profile full``) or at a small
fraction of it (``--profile quick``).  Both references are run, timed with
their peak RSS, cross-checked token by token, and, where a closed form exists,
checked against it.  Randomized small-oracle testing lives in each problem's
``tests/random_cases.py``; this tool covers complexity and scale.

    python3 tools/stress_finale_50_65.py --profile quick
    python3 tools/stress_finale_50_65.py --profile full --problem 55
"""
from __future__ import annotations

import argparse
import json
import random
import subprocess
import tempfile
from pathlib import Path
from typing import Callable, Iterator, Optional

from stress_finale_round6 import run

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sections/100_grandmaster_finale/problems"
Checker = Optional[Callable[[str], None]]
MOD998 = 998244353


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rand_queries(rng: random.Random, n: int, q: int) -> list[tuple[int, int]]:
    out = []
    for _ in range(q):
        l = rng.randint(1, n)
        out.append((l, rng.randint(l, n)))
    return out


# 50 -- pattern occurrences on tree paths ------------------------------------
def gen50(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(50)
    n = q = max(10, int(100_000 * scale))

    def fmt(labels, edges, qs):
        return (f"{len(labels)} {len(qs)}\n{labels}\n" + "".join(f"{a} {b}\n" for a, b in edges)
                + "".join(f"{u} {v} {p}\n" for u, v, p in qs))

    path = [(i, i + 1) for i in range(1, n)]
    qs = [(rng.randint(1, n), rng.randint(1, n), "a" * rng.randint(1, 2)) for _ in range(q)]

    def unary(out: str) -> None:
        got = list(map(int, out.split()))
        expect(got == [max(0, abs(u - v) + 2 - len(p)) for u, v, p in qs], "unary path counts")

    yield "unary-path", fmt("a" * n, path, qs), unary
    long_len = max(2, min(4000, n // 4))
    qs = [(rng.randint(1, n // 2), rng.randint(n // 2, n), "a" * long_len) for _ in range(50)]
    qs += [(rng.randint(1, n), rng.randint(1, n), "a") for _ in range(q - 50)]
    yield "long-unary-patterns", fmt("a" * n, path, qs), None
    labels = "".join(rng.choice("ab") for _ in range(n))
    edges = [(rng.randint(1, v - 1), v) for v in range(2, n + 1)]
    qs = [(rng.randint(1, n), rng.randint(1, n), "".join(rng.choice("ab") for _ in range(rng.randint(1, 3))))
          for _ in range(q)]
    yield "random-tree", fmt(labels, edges, qs), None
    edges = [(1, 2), (1, 3)] + [(i, i + 2) for i in range(2, n - 1)]
    crossing = max(1, min(1000, n // 10))
    qs = [(rng.randrange(2, n + 1, 2), rng.randrange(3, n + 1, 2),
           "".join(rng.choice("ab") for _ in range(crossing if i < 150 else 1))) for i in range(q)]
    yield "v-shape-crossing", fmt(labels, edges, qs), None


# 51 -- distinct squares ---------------------------------------------------------
def gen51(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(51)
    n = max(10, int(200_000 * scale))

    def below_n(out: str) -> None:
        expect(int(out) < n, "distinct squares must be fewer than n")

    yield "unary", "a" * n + "\n", lambda out: expect(int(out) == n // 2, "a^n has n/2 squares")
    yield "b-then-unary", "b" + "a" * (n - 1) + "\n", below_n
    a, b = "a", "ab"
    while len(b) < n:
        a, b = b, b + a
    yield "fibonacci", b[:n] + "\n", below_n
    yield "thue-morse", "".join("ab"[bin(i).count("1") & 1] for i in range(n)) + "\n", below_n
    yield "random-ab", "".join(rng.choice("ab") for _ in range(n)) + "\n", below_n
    parts = []
    while sum(map(len, parts)) < n:
        unit = "".join(rng.choice("ab") for _ in range(rng.randint(1, 30)))
        parts.append(unit * rng.randint(2, 40))
    yield "run-soup", "".join(parts)[:n] + "\n", below_n


# 52 -- offline dynamic MST ------------------------------------------------------
def gen52(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(52)
    size = max(10, int(200_000 * scale))

    def build(n, m, q, hot=None, wmax=10**9):
        edges = [(rng.randrange(v) + 1, v + 1) for v in range(1, n)]
        while len(edges) < m:
            edges.append((rng.randint(1, n), rng.randint(1, n)))
        lines = [f"{n} {m} {q}"] + [f"{u} {v} {rng.randint(1, wmax)}" for u, v in edges]
        lines += [f"{rng.randint(1, m) if hot is None else rng.choice(hot)} {rng.randint(1, wmax)}" for _ in range(q)]
        return "\n".join(lines) + "\n"

    yield "sparse-random", build(size, size, size), None
    yield "small-weights", build(size, size, size, wmax=5), None
    yield "hot-edges", build(size, size, size, hot=list(range(1, min(size, 200)))), None
    yield "dense-n/10", build(max(2, size // 10), size, size), None


# 53 -- spanning tree weight distribution ----------------------------------------
def gen53(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(53)
    n = 70 if scale >= 1 else 12
    K = 12 if scale >= 1 else 4
    m = 3000 if scale >= 1 else 60

    def fmt(edges):
        return f"{n} {len(edges)} {K}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in edges)

    complete = [(u, v, K) for u in range(1, n + 1) for v in range(u + 1, n + 1)]

    def cayley(out: str) -> None:
        got = list(map(int, out.split()))
        expect(len(got) == (n - 1) * K + 1, "length")
        expect(got[-1] == pow(n, n - 2, MOD998) and not any(got[:-1]), "Cayley's formula")

    yield "complete-max-weight", fmt(complete), cayley
    yield "random", fmt([(rng.randint(1, n), rng.randint(1, n), rng.randint(0, K)) for _ in range(m)]), None
    yield "extreme-weights", fmt([(rng.randint(1, n), rng.randint(1, n), rng.choice([0, K])) for _ in range(m)]), None


# 54 -- maximum weight general matching ------------------------------------------
def gen54(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(54)
    n = 500 if scale >= 1 else 40
    m = 50_000 if scale >= 1 else 400
    pairs = set()
    while len(pairs) < m:
        u, v = rng.randint(1, n), rng.randint(1, n)
        if u != v:
            pairs.add((min(u, v), max(u, v)))
    pairs = sorted(pairs)

    def fmt(edges):
        return f"{n} {len(edges)}\n" + "".join(f"{u} {v} {w}\n" for u, v, w in edges)

    yield "random", fmt([(u, v, rng.randint(1, 10**6)) for u, v in pairs]), None
    yield "distance-weights", fmt([(u, v, abs(u - v) * 1000 + rng.randint(0, 999)) for u, v in pairs]), None
    yield "structured", fmt([(u, v, (u % 17) * (v % 13) + 1) for u, v in pairs]), None
    # Equal weights with a planted perfect matching hidden among random pairs.
    planted = {(2 * i - 1, 2 * i) for i in range(1, n // 2 + 1)}
    equal = [(u, v, 1000) for u, v in sorted(planted | set(pairs[: m - len(planted)]))]
    yield "all-equal", fmt(equal), lambda out: expect(int(out) == 1000 * (n // 2), "perfect matching")


# 55 -- kinetic tree diameter ----------------------------------------------------
def gen55(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(55)
    n = max(10, int(100_000 * scale))
    m = max(10, int(1_000_000 * scale))

    def fmt(edges):
        return f"{n} {m}\n" + "".join(f"{u} {v} {a} {b}\n" for u, v, a, b in edges)

    def path_check(out: str) -> None:
        got = out.split()
        expect(len(got) == m, "count")
        for t in (0, 1, m // 2, m - 1):
            expect(int(got[t]) == (n - 1) * (100000 * t + 10**9), "path diameter")

    yield "path-max", fmt([(i, i + 1, 100000, 10**9) for i in range(1, n)]), path_check
    R = lambda: (rng.randint(0, 100000), rng.randint(0, 10**9))
    yield "random", fmt([(rng.randint(1, v - 1), v, *R()) for v in range(2, n + 1)]), None
    yield "star", fmt([(1, v, *R()) for v in range(2, n + 1)]), None
    yield "convex-star", fmt([(1, v, v - 1, 10**9 - (v - 1) ** 2 // 11) for v in range(2, n + 1)]), None


# 56 -- distinct substrings of windows -------------------------------------------
def gen56(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(56)
    n = q = max(10, int(200_000 * scale))

    def fmt(s, qs):
        return f"{s}\n{len(qs)}\n" + "".join(f"{l} {r}\n" for l, r in qs)

    qs = rand_queries(rng, n, q)
    yield "unary", fmt("a" * n, qs), lambda out: expect(
        list(map(int, out.split())) == [r - l + 1 for l, r in qs], "a^k has k substrings")
    yield "random-ab", fmt("".join(rng.choice("ab") for _ in range(n)), rand_queries(rng, n, q)), None
    a, b = "a", "ab"
    while len(b) < n:
        a, b = b, b + a
    yield "fibonacci", fmt(b[:n], rand_queries(rng, n, q)), None
    blocks = []
    while sum(map(len, blocks)) < n:
        blocks.append("a" * rng.randint(1, 50) + "b")
    yield "blocks", fmt("".join(blocks)[:n], rand_queries(rng, n, q)), None


# 57 -- Min_25 sieve -------------------------------------------------------------
def gen57(scale: float) -> Iterator[tuple[str, str, Checker]]:
    big = 10**10 if scale >= 1 else 10**7
    yield "maximum", f"{big}\n", None
    yield "prime-below-max", f"{9999999967 if scale >= 1 else 9999991}\n", None
    # 10^8 was verified against an independent linear sieve.
    yield "sieve-checked", "100000000\n", lambda out: expect(int(out) == 213827063, "sieve value")


# 58 -- dominator-based link criticality -----------------------------------------
def gen58(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(58)
    n = m = max(10, int(200_000 * scale))

    def fmt(links):
        return f"{n} {len(links)}\n" + "".join(f"{u} {v}\n" for u, v in links)

    path = [(i, i + 1) for i in range(1, n)] + [(n, 1)]
    yield "cycle", fmt(path), lambda out: expect(
        list(map(int, out.split())) == [n - i for i in range(1, n)] + [0], "cycle losses")
    links = [(max(1, v - rng.randint(1, 3)), v) for v in range(2, n + 1)]
    links += [(rng.randint(1, n), rng.randint(1, n)) for _ in range(m - len(links))]
    yield "local-plus-random", fmt(links[:m]), None
    links = [(v // 2, v) for v in range(2, n + 1)][: m // 2]
    links += [(rng.randint(n // 2, n), rng.randint(1, 20)) for _ in range(m - len(links))]
    yield "tree-backedges", fmt(links), None


# 59 -- walk counting ------------------------------------------------------------
def gen59(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(59)
    n = 1000 if scale >= 1 else 60
    m = 10_000 if scale >= 1 else 600

    def fmt(N, s, t, edges):
        return f"{n} {len(edges)} {N} {s} {t}\n" + "".join(f"{u} {v}\n" for u, v in edges)

    yield "random", fmt(10**18, 1, 2, [(rng.randint(1, n), rng.randint(1, n)) for _ in range(m)]), None
    cycle = [(i, i % n + 1) for i in range(1, n + 1)]
    N = 10**18 - 7
    hit = 1 if (N - 32) % n == 0 else 0
    yield "cycle", fmt(N, 5, 37, cycle), lambda out: expect(int(out) == hit, "cycle walks")
    dag = [(u, v) for u in range(1, n + 1) for v in range(u + 1, min(n, u + 20) + 1)][:m]
    yield "dag", fmt(10**18, 1, n, dag), lambda out: expect(int(out) == 0, "nilpotent")
    edges = [(rng.randint(1, n), rng.randint(1, n)) for _ in range(m)]
    steps = 2 * n + 700
    cur = [0] * (n + 1)
    cur[3] = 1
    for _ in range(steps):
        nxt = [0] * (n + 1)
        for u, v in edges:
            nxt[v] += cur[u]
        cur = [x % MOD998 for x in nxt]
    want = cur[4]
    yield "simulation", fmt(steps, 3, 4, edges), lambda out: expect(int(out) == want, "direct simulation")


# 60 -- Manhattan bottleneck ---------------------------------------------------------
def gen60(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(60)
    n = q = max(10, int(200_000 * scale))

    def fmt(points, queries):
        return (f"{len(points)} {len(queries)}\n" + "".join(f"{a} {b}\n" for a, b in points)
                + "".join(f"{a} {b}\n" for a, b in queries))

    qs = [(rng.randint(1, n), rng.randint(1, n)) for _ in range(q)]
    pts = [(rng.randint(-10**9, 10**9), rng.randint(-10**9, 10**9)) for _ in range(n)]
    yield "random", fmt(pts, qs), None
    perm = list(range(n))
    rng.shuffle(perm)
    yield "line-step3", fmt([(3 * p - 10**9, 0) for p in perm], qs), lambda out: expect(
        list(map(int, out.split())) == [0 if a == b else 3 for a, b in qs], "line")
    yield "all-equal", fmt([(7, -7)] * n, qs), lambda out: expect(set(out.split()) == {"0"}, "equal points")
    yield "antidiagonal", fmt([(v, -v) for v in (rng.randint(-10**9, 10**9) for _ in range(n))], qs), None


# 61 -- Li Chao merging DP -----------------------------------------------------------
def gen61(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(61)
    n = max(10, int(200_000 * scale))

    def fmt(a, b, edges):
        return f"{n}\n{' '.join(map(str, a))}\n{' '.join(map(str, b))}\n" + "".join(f"{u} {v}\n" for u, v in edges)

    path = [(i, i + 1) for i in range(1, n)]
    yield "path-negative", fmt([-100000] * n, [100000] * n, path), lambda out: expect(
        list(map(int, out.split())) == [-(n - v) * 10**10 for v in range(1, n + 1)], "path")
    R = lambda: [rng.randint(-100000, 100000) for _ in range(n)]
    yield "random-tree", fmt(R(), R(), [(rng.randint(1, v - 1), v) for v in range(2, n + 1)]), None
    yield "caterpillar", fmt(R(), R(), [(v - 1 if v % 2 else max(1, v - 2), v) for v in range(2, n + 1)]), None
    yield "star", fmt(R(), R(), [(1, v) for v in range(2, n + 1)]), None


# 62 -- components of edge windows -----------------------------------------------
def gen62(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(62)
    n = m = q = max(10, int(200_000 * scale))

    def fmt(nv, edges, qs):
        return (f"{nv} {len(edges)} {len(qs)}\n" + "".join(f"{u} {v}\n" for u, v in edges)
                + "".join(f"{l} {r}\n" for l, r in qs))

    yield "random", fmt(n, [(rng.randint(1, n), rng.randint(1, n)) for _ in range(m)], rand_queries(rng, m, q)), None
    cycle = [(i, i + 1) for i in range(1, n)] + [(n, 1)]
    qs = rand_queries(rng, m, q)
    yield "cycle-once", fmt(n, cycle, qs), lambda out: expect(
        list(map(int, out.split())) == [1 if r - l + 1 == n else n - (r - l + 1) for l, r in qs], "cycle windows")
    small = max(2, n // 200)
    yield "cycle-repeated", fmt(small, [((i % small) + 1, ((i + 1) % small) + 1) for i in range(m)],
                                rand_queries(rng, m, q)), None


# 63 -- Hamiltonian cycles on W x N grids ------------------------------------------
def gen63(scale: float) -> Iterator[tuple[str, str, Checker]]:
    top = 10 if scale >= 1 else 8
    yield f"width-{top}-huge", f"{top} 1000000000000000000\n", None
    yield "width-9-huge", "9 999999999999999999\n", None
    # 10 x 10 = 467260456608 cycles (OEIS A003763).
    yield "square-10", "10 10\n", lambda out: expect(int(out) == 467260456608 % MOD998, "10x10 count")


# 64 -- binary search + 2-SAT ----------------------------------------------------
def gen64(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(64)
    n = max(10, int(30_000 * scale))

    def fmt(pairs):
        return f"{len(pairs)}\n" + "".join(f"{a} {b}\n" for a, b in pairs)

    yield "random", fmt([(rng.randint(0, 10**9), rng.randint(0, 10**9)) for _ in range(n)]), None
    gap = 50_000
    yield "near-duplicates", fmt([(2 * i * gap, 2 * i * gap + 1) for i in range(n)]), lambda out: expect(
        int(out) == 2 * gap, "spread choice")
    yield "dense-small-range", fmt([(rng.randint(0, 3 * n), rng.randint(0, 3 * n)) for _ in range(n)]), None
    yield "all-same", fmt([(5, 5)] * n), lambda out: expect(int(out) == 0, "coincident")


# 65 -- Steiner length of label ranges -------------------------------------------
def gen65(scale: float) -> Iterator[tuple[str, str, Checker]]:
    rng = random.Random(65)
    n = q = max(10, int(200_000 * scale))

    def fmt(edges, qs):
        return f"{n} {len(qs)}\n" + "".join(f"{a} {b} {w}\n" for a, b, w in edges) + "".join(f"{l} {r}\n" for l, r in qs)

    def relabel(edges):
        perm = list(range(1, n + 1))
        rng.shuffle(perm)
        return [(perm[a - 1], perm[b - 1], w) for a, b, w in edges]

    qs = rand_queries(rng, n, q)
    yield "path", fmt([(i, i + 1, 1) for i in range(1, n)], qs), lambda out: expect(
        list(map(int, out.split())) == [r - l for l, r in qs], "path span")
    W = lambda: rng.randint(1, 10**9)
    yield "random-shuffled", fmt(relabel([(rng.randint(1, v - 1), v, W()) for v in range(2, n + 1)]),
                                 rand_queries(rng, n, q)), None
    yield "binary-shuffled", fmt(relabel([(v // 2, v, W()) for v in range(2, n + 1)]), rand_queries(rng, n, q)), None
    yield "binary-bfs-labels", fmt([(v // 2, v, W()) for v in range(2, n + 1)], rand_queries(rng, n, q)), None


GENERATORS = {
    "50": ("50_chronicle_path_dictionary", gen50),
    "51": ("51_echo_census", gen51),
    "52": ("52_tariff_revision_network", gen52),
    "53": ("53_spanning_weight_spectrum", gen53),
    "54": ("54_fleet_pairing", gen54),
    "55": ("55_monsoon_diameter", gen55),
    "56": ("56_window_substring_census", gen56),
    "57": ("57_prime_power_xor_sum", gen57),
    "58": ("58_critical_link_audit", gen58),
    "59": ("59_walk_count_oracle", gen59),
    "60": ("60_taxicab_backbone", gen60),
    "61": ("61_cavern_descent", gen61),
    "62": ("62_window_component_census", gen62),
    "63": ("63_periodic_loop_frontier", gen63),
    "64": ("64_beacon_placement", gen64),
    "65": ("65_temporal_steiner_span", gen65),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=("quick", "full"), default="quick")
    parser.add_argument("--problem", action="append", help="problem number, repeatable")
    parser.add_argument("--lang", choices=("cpp", "py", "both"), default="both")
    parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args()
    scale = 1.0 if args.profile == "full" else 0.02
    wanted = args.problem or sorted(GENERATORS)
    failures = 0
    with tempfile.TemporaryDirectory(prefix="finale-50-65-") as tmp:
        for number in wanted:
            slug, generator = GENERATORS[number]
            problem = BASE / slug
            limit = json.loads((problem / "manifest.json").read_text())["time_limit_seconds"]
            binary = Path(tmp) / slug
            if args.lang in ("cpp", "both"):
                subprocess.run(["g++", "-std=c++23", "-O2", "-pipe", str(problem / "solution.cpp"), "-o", str(binary)],
                               check=True)
            for name, data, check in generator(scale):
                outputs = {}
                for lang in ("cpp", "py"):
                    if args.lang not in (lang, "both"):
                        continue
                    command = [str(binary)] if lang == "cpp" else ["python3", str(problem / "solution.py")]
                    try:
                        outputs[lang], elapsed, rss = run(command, data, args.timeout)
                        verdict = "ok"
                        if check is not None:
                            check(outputs[lang])
                            verdict = "invariant ok"
                        if elapsed > limit:
                            verdict += f"  OVER {limit}s LIMIT"
                            failures += 1
                    except (AssertionError, RuntimeError, subprocess.TimeoutExpired) as exc:
                        failures += 1
                        print(f"{slug} {name} {lang}: FAILED {exc}")
                        continue
                    memory = f"{rss / 1024:7.1f} MiB" if rss is not None else ""
                    print(f"{slug:32s} {name:22s} {lang:3s} {elapsed:7.2f}s {memory}  {verdict}", flush=True)
                if len(outputs) == 2 and outputs["cpp"].split() != outputs["py"].split():
                    failures += 1
                    print(f"{slug} {name}: C++ and Python outputs differ")
    print("all cases passed" if not failures else f"{failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
