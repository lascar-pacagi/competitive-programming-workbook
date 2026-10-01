"""Adversarial limit tests for finale Problems 31--49.

Every case is built at the published maximum (``--profile full``) or a small
fraction of it (``--profile quick``).  Both references run with timing and
peak RSS, their outputs are compared token by token (with the float
tolerance for geometry), and closed-form invariants are checked where
available.  Small-oracle testing lives in each problem's random_cases.py.

    python3 tools/stress_finale_31_49.py --profile quick
    python3 tools/stress_finale_31_49.py --profile full --problem 47
"""
from __future__ import annotations

import argparse
import json
import math
import random
import subprocess
import tempfile
from pathlib import Path
from typing import Callable, Iterator, Optional

from stress_finale_round6 import primitive_polygon, run

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "sections/100_grandmaster_finale/problems"
P998 = 998244353
P107 = 1_000_000_007
Checker = Optional[Callable[[str], None]]


def expect(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def gen31(scale: float) -> Iterator[tuple[str, str, Checker]]:
    N = 200_000 if scale >= 1 else 3000
    yield "maximum", f"{N}\n", lambda out: expect(out.split()[:6] == "1 1 3 19 195 3031".split(), "A001832 prefix")


def gen32(scale: float) -> Iterator[tuple[str, str, Checker]]:
    d = 500_000 if scale >= 1 else 5000
    n = 10**18
    yield "r=3", f"{n} 3 {d}\n", None
    yield "r=-1", f"{n} {P998 - 1} {d}\n", None
    yield "r=1,d=1", f"{n} 1 1\n", lambda out: expect(int(out) == n * (n - 1) // 2 % P998, "sum of i")
    yield "r=2,d=0", f"{n} 2 0\n", lambda out: expect(int(out) == (pow(2, n, P998) - 1) % P998, "geometric")


def gen33(scale: float) -> Iterator[tuple[str, str, Checker]]:
    N = 100_000 if scale >= 1 else 3000
    rng = random.Random(33)
    yield "random-D8", f"{N} 8\n" + " ".join(str(rng.randrange(1, P998)) for _ in range(9)) + "\n", None
    M = [1, 1]
    for k in range(2, N):
        M.append(((2 * k + 1) * M[-1] + (3 * k - 3) * M[-2]) * pow(k + 2, P998 - 2, P998) % P998)
    want = [str(M[n - 1]) for n in range(1, N + 1)]
    yield "motzkin", f"{N} 2\n1 1 1\n", lambda out: expect(out.split() == want, "Motzkin numbers")


def gen34(scale: float) -> Iterator[tuple[str, str, Checker]]:
    n = S = 200_000 if scale >= 1 else 3000
    rng = random.Random(34)
    yield "random", f"{n} {S}\n" + " ".join(str(rng.randint(1, S)) for _ in range(n)) + "\n", None
    k = 1000
    fact = [1] * (S + k + 1)
    for i in range(1, S + k + 1):
        fact[i] = fact[i - 1] * i % P998
    inv = pow(fact[k - 1], P998 - 2, P998)
    want = [str(fact[s + k - 1] * pow(fact[s], P998 - 2, P998) % P998 * inv % P998) for s in range(1, min(S, 2000) + 1)]
    yield "identical-coins", f"{k} {S}\n" + " ".join(["1"] * k) + "\n", lambda out: expect(out.split()[:len(want)] == want, "binomials")


def gen35(scale: float) -> Iterator[tuple[str, str, Checker]]:
    T = 100_000 if scale >= 1 else 2000
    rng = random.Random(35)
    rows = []
    a, b = 1, 1
    for i in range(T):
        if i % 2:
            rows.append(f"{10**18} {a} {rng.randint(0, 10**18)} {b}")
            a, b = b, a + b
            if b > 10**18:
                a, b = 1, 1
        else:
            rows.append(f"{rng.randint(0, 10**18)} {rng.randint(0, 10**18)} {rng.randint(0, 10**18)} {rng.randint(1, 10**18)}")
    yield "fibonacci-and-random", f"{T}\n" + "\n".join(rows) + "\n", None
    n = 10**18
    s1, s2 = n * (n + 1) // 2 % P998, n * (n + 1) * (2 * n + 1) // 6 % P998
    yield "identity", f"1\n{n} 7 0 7\n", lambda out: expect(out.split() == [str(s1), str(s2), str(s2)], "q = x")


def gen36(scale: float) -> Iterator[tuple[str, str, Checker]]:
    q = 100_000 if scale >= 1 else 2000
    rng = random.Random(36)
    for m, p in ((524288, 2), (531441, 3), (510510, None)):
        if p:
            t = 1
            while t * p <= 10**18:
                t *= p
            n = t - 1  # no carries: every query does the full work
            rows = [(n, rng.randint(0, n)) for _ in range(q)]
        else:
            rows = []
            for _ in range(q):
                nn = rng.randint(0, 10**18)
                rows.append((nn, rng.randint(0, nn)))
        yield f"m={m}", f"{m} {q}\n" + "".join(f"{a} {b}\n" for a, b in rows), None
    p = 999983
    fact = [1] * p
    for i in range(1, p):
        fact[i] = fact[i - 1] * i % p

    def lucas(n, k):
        r = 1
        while n or k:
            a, b = n % p, k % p
            if b > a:
                return 0
            r = r * fact[a] % p * pow(fact[b] * fact[a - b] % p, p - 2, p) % p
            n //= p
            k //= p
        return r
    rows = []
    for _ in range(min(q, 5000)):
        nn = rng.randint(0, 10**18)
        rows.append((nn, rng.randint(0, nn)))
    want = [str(lucas(a, b)) for a, b in rows]
    yield "prime-lucas", f"{p} {len(rows)}\n" + "".join(f"{a} {b}\n" for a, b in rows), lambda out: expect(out.split() == want, "Lucas")


def gen37(scale: float) -> Iterator[tuple[str, str, Checker]]:
    q = 1000 if scale >= 1 else 50
    rng = random.Random(37)

    def is_prime(n):
        if n < 2:
            return False
        for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
            if n % a == 0:
                return n == a
        d, s = n - 1, 0
        while d % 2 == 0:
            d //= 2
            s += 1
        for a in (2, 325, 9375, 28178, 450775, 9780504, 1795265022):
            x = pow(a, d, n)
            if x in (0, 1, n - 1):
                continue
            for _ in range(s - 1):
                x = x * x % n
                if x == n - 1:
                    break
            else:
                return False
        return True

    def prime_below(x):
        while not is_prime(x):
            x -= 1
        return x
    known = [(10**18, 15 * 10**17), (2**59, 3 * 2**58), (3**37, 8 * 3**36), (5**25, 4 * 5**25)]
    ms = [m for m, _ in known]
    for _ in range(q - len(ms)):
        ms.append(prime_below(rng.randint(9 * 10**8, 10**9)) * prime_below(rng.randint(9 * 10**8, 10**9)))
    want = [str(v) for _, v in known]
    yield "semiprimes", f"{len(ms)}\n" + "".join(f"{m}\n" for m in ms), lambda out: expect(out.split()[:4] == want, "closed forms")


def gen38(scale: float) -> Iterator[tuple[str, str, Checker]]:
    n = q = 300_000 if scale >= 1 else 5000
    rng = random.Random(38)
    a = [rng.randint(0, 2**30 - 1) for _ in range(n)]
    rows = []
    for _ in range(q):
        l = rng.randint(1, n)
        rows.append((l, rng.randint(l, n), rng.choice([0, rng.randint(0, 2**30 - 1)])))
    yield "random", f"{n} {q}\n{' '.join(map(str, a))}\n" + "".join(f"{l} {r} {x}\n" for l, r, x in rows), None
    a = [(1 << (i % 30 + 1)) - 1 for i in range(n)]
    rows = [(1, n, 0)] * 10 + [(rng.randint(1, 40), n, 2**30 - 1) for _ in range(q - 10)]
    want = pow(2, n - 30, P107)
    yield "full-rank", f"{n} {q}\n{' '.join(map(str, a))}\n" + "".join(f"{l} {r} {x}\n" for l, r, x in rows), \
        lambda out: expect(out.split()[:10] == [str(want)] * 10, "2^(n-30)")


def gen39(scale: float) -> Iterator[tuple[str, str, Checker]]:
    N = 500_000 if scale >= 1 else 20000
    rng = random.Random(39)
    yield "random", f"{N} {10**18 - 3}\n" + " ".join(["1"] + [str(rng.randrange(P998)) for _ in range(N - 1)]) + "\n", None
    mu = [1] * (N + 1)
    is_p = bytearray([1]) * (N + 1)
    for p in range(2, N + 1):
        if is_p[p]:
            for j in range(p, N + 1, p):
                if j > p:
                    is_p[j] = 0
                mu[j] = -mu[j]
            for j in range(p * p, N + 1, p * p):
                mu[j] = 0
    want = [str(x % P998) for x in mu[1:]]
    yield "mobius", f"{N} {P998 - 1}\n" + " ".join(["1"] * N) + "\n", lambda out: expect(out.split() == want, "Mobius")


def gen40(scale: float) -> Iterator[tuple[str, str, Checker]]:
    d = 3000 if scale >= 1 else 300
    p = 999999999999999989
    rng = random.Random(40)
    yield "random", f"{p} {d}\n" + " ".join(str(rng.randrange(p)) for _ in range(d)) + " 1\n", None
    roots = rng.sample(range(p), d // 4)
    f = [1]
    for x in roots + roots[: d // 8]:
        g = [0] * (len(f) + 1)
        for i, c in enumerate(f):
            g[i] = (g[i] - x * c) % p
            g[i + 1] = (g[i + 1] + c) % p
        f = g
    yield "planted", f"{p} {len(f) - 1}\n" + " ".join(map(str, f)) + "\n", lambda out: expect(int(out) == len(roots), "planted roots")


def gen41(scale: float) -> Iterator[tuple[str, str, Checker]]:
    n = 2000 if scale >= 1 else 200
    rng = random.Random(41)
    pts = set()
    while len(pts) < n:
        pts.add((rng.randint(0, 2000), rng.randint(0, 2000)))
    yield "dense-equal-radii", f"{n}\n" + "".join(f"{x} {y} 1500\n" for x, y in pts), None
    yield "nested", f"{n}\n" + "".join(f"0 0 {10000 - i}\n" for i in range(n)), \
        lambda out: expect(abs(float(out) - math.pi * 1e8) <= 1e-7 * math.pi * 1e8, "outer disc")


def gen42(scale: float) -> Iterator[tuple[str, str, Checker]]:
    n = 2000 if scale >= 1 else 200
    yield "moment-curve-sorted", f"{n}\n" + "".join(f"{t * 1000} {t * t} {t ** 3}\n" for t in range(-n // 2, n - n // 2)), None
    rng = random.Random(42)
    ts = rng.sample(range(-500, 501), n // 2)
    P = [(4 * t * 1000, 4 * t * t, 4 * t ** 3) for t in ts]
    for _ in range(n - len(P)):
        quad = rng.sample(P[: len(ts)], 4)
        P.append(tuple(sum(c[k] for c in quad) // 4 for k in range(3)))
    rng.shuffle(P)
    yield "curve-plus-interior", f"{len(P)}\n" + "".join(f"{x} {y} {z}\n" for x, y, z in P), None
    s = 10**9
    yield "tetrahedron", f"4\n0 0 0\n{s} 0 0\n0 {s} 0\n0 0 {s}\n", \
        lambda out: expect(abs(float(out) - (1.5 + math.sqrt(3) / 2) * 1e18) <= 1e-7 * 3e18, "tetrahedron")


def gen43(scale: float) -> Iterator[tuple[str, str, Checker]]:
    n = 2000 if scale >= 1 else 200
    q = 500_000 if scale >= 1 else 5000
    rng = random.Random(43)
    prime = 1000003
    xs = rng.sample(range(prime), n)
    pts = [(x * 997 - 5 * 10**8, (x * x % prime) * 991 - 5 * 10**8) for x in xs]  # no three collinear
    qs = [tuple(rng.sample(range(n), 3)) for _ in range(q)]

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    def inside(i, j, k):
        a, b, c = pts[i], pts[j], pts[k]
        s = 1 if cross(a, b, c) > 0 else -1
        return sum(1 for t, p in enumerate(pts) if t not in (i, j, k) and s * cross(a, b, p) > 0
                   and s * cross(b, c, p) > 0 and s * cross(c, a, p) > 0)
    want = [str(inside(*t)) for t in qs[:100]]
    yield "parabola-mod-p", f"{n} {q}\n" + "".join(f"{x} {y}\n" for x, y in pts) + "".join(f"{a + 1} {b + 1} {c + 1}\n" for a, b, c in qs), \
        lambda out: expect(out.split()[:100] == want, "direct counts")


def gen44(scale: float) -> Iterator[tuple[str, str, Checker]]:
    n = 300 if scale >= 1 else 60
    convex = [(round(math.cos(2 * math.pi * i / n) * 1e9), round(math.sin(2 * math.pi * i / n) * 1e9)) for i in range(n)]
    cat = math.comb(2 * (n - 2), n - 2) // (n - 1) % P107
    yield "convex", f"{n}\n" + "".join(f"{x} {y}\n" for x, y in convex), lambda out: expect(int(out) == cat, "Catalan")
    rng = random.Random(44)

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    while True:
        pts = list({(round(math.cos(t) * r), round(math.sin(t) * r)) for t, r in
                    ((rng.uniform(0, 2 * math.pi), rng.uniform(1e8, 1e9)) for _ in range(n))})
        pts.sort(key=lambda p: math.atan2(p[1], p[0]))
        ok = len(pts) == n and all(
            not ((cross(pts[i], pts[(i + 1) % n], pts[j]) > 0) != (cross(pts[i], pts[(i + 1) % n], pts[(j + 1) % n]) > 0)
                 and (cross(pts[j], pts[(j + 1) % n], pts[i]) > 0) != (cross(pts[j], pts[(j + 1) % n], pts[(i + 1) % n]) > 0))
            for i in range(n) for j in range(i + 2, n) if not (i == 0 and j == n - 1))
        if ok:
            break
    yield "star", f"{n}\n" + "".join(f"{x} {y}\n" for x, y in pts), lambda out: expect(int(out) > 0, "nonzero")


def gen45(scale: float) -> Iterator[tuple[str, str, Checker]]:
    side = 10 if scale >= 1 else 4
    rng = random.Random(45)

    def square(cx, cy, r, phase):
        out = []
        for i in range(4):
            t = phase + math.pi / 2 * i
            p = (cx + round(r * math.cos(t)), cy + round(r * math.sin(t)))
            if p not in out:
                out.append(p)
        return out
    polys = [square(i * 3000 + rng.randint(-200, 200), j * 3000 + rng.randint(-200, 200), 1000, rng.uniform(0, 1.5))
             for i in range(side) for j in range(side)]
    body = f"{len(polys)}\n" + "".join(f"{len(p)}\n" + "".join(f"{x} {y}\n" for x, y in p) for p in polys)
    yield "grid-of-squares", f"-3000 -3000 {3000 * side} {3000 * side + 1}\n" + body, None
    yield "clear-line", f"-3000 -3000 -3000 {3000 * side}\n" + body, \
        lambda out: expect(abs(float(out) - (3000 * side + 3000)) <= 1e-6, "straight segment")


def gen46(scale: float) -> Iterator[tuple[str, str, Checker]]:
    n = m = 1000 if scale >= 1 else 120
    rng = random.Random(46)
    yield "random", f"{n} {m}\n" + "\n".join("".join(rng.choice("01") for _ in range(m)) for _ in range(n)) + "\n", None
    press = [[rng.random() < 0.5 for _ in range(m)] for _ in range(n)]
    g = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if press[i][j]:
                for di, dj in ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)):
                    if 0 <= i + di < n and 0 <= j + dj < m:
                        g[i + di][j + dj] ^= 1
    yield "planted-solvable", f"{n} {m}\n" + "\n".join("".join(map(str, row)) for row in g) + "\n", \
        lambda out: expect(int(out) != 0, "planted solution exists")


def gen47(scale: float) -> Iterator[tuple[str, str, Checker]]:
    n = 600 if scale >= 1 else 80
    rng = random.Random(47)
    pts = [(rng.randint(-10**4, 10**4), rng.randint(-10**4, 10**4)) for _ in range(n)]
    yield "random-half", f"{n} {n // 2}\n" + "".join(f"{x} {y}\n" for x, y in pts), None
    yield "random-all-but-one", f"{n} {n - 1}\n" + "".join(f"{x} {y}\n" for x, y in pts), None
    pts = [(0, 0)] * (n // 3) + [(rng.randint(-10**4, 10**4), rng.randint(-10**4, 10**4)) for _ in range(n - n // 3)]
    yield "stacked-point", f"{n} {n // 3}\n" + "".join(f"{x} {y}\n" for x, y in pts), lambda out: expect(float(out) <= 1e-7, "zero radius")


def gen48(scale: float) -> Iterator[tuple[str, str, Checker]]:
    n = 40 if scale >= 1 else 24
    yield "all-ties", f"{n} 0\n" + " ".join(["0"] * n) + "\n", lambda out: expect(out.split() == ["0", str(pow(2, n, P107))], "2^n")
    rng = random.Random(48)
    edges = [(u, v) for u in range(1, n + 1) for v in range(u + 1, n + 1) if rng.random() < 0.15]
    yield "random", f"{n} {len(edges)}\n" + " ".join(str(rng.randint(0, 3)) for _ in range(n)) + "\n" + "".join(f"{u} {v}\n" for u, v in edges), None


def gen49(scale: float) -> Iterator[tuple[str, str, Checker]]:
    poly = primitive_polygon(12000 if scale >= 1 else 600)
    q = 200_000 if scale >= 1 else 5000
    rng = random.Random(49)
    n = len(poly)
    total = abs(sum(poly[i][0] * poly[(i + 1) % n][1] - poly[(i + 1) % n][0] * poly[i][1] for i in range(n))) / 2
    rows = []
    for i in range(q):
        if i % 4 == 0:  # along an edge, counterclockwise: the whole shelf is on the left
            k = rng.randrange(n)
            a, b = poly[k], poly[(k + 1) % n]
        else:
            a = (rng.randint(-10**5, 10**5), rng.randint(-10**5, 10**5))
            b = a
            while b == a:
                b = (rng.randint(-10**5, 10**5), rng.randint(-10**5, 10**5))
        rows.append((a, b))

    def check(out):
        vals = out.split()
        for i in range(0, min(len(vals), 400), 4):
            expect(abs(float(vals[i]) - total) <= 1e-7 * total + 1e-7, "edge line keeps the whole polygon")
    yield "primitive-polygon", f"{n} {q}\n" + "".join(f"{x} {y}\n" for x, y in poly) + "".join(f"{a[0]} {a[1]} {b[0]} {b[1]}\n" for a, b in rows), check


GENERATORS = {
    "31": ("31_two_faction_networks", gen31),
    "32": ("32_exponential_polynomial_ledger", gen32),
    "33": ("33_branching_family_census", gen33),
    "34": ("34_coin_bag_census", gen34),
    "35": ("35_staircase_moments", gen35),
    "36": ("36_binomial_ledger", gen36),
    "37": ("37_rabbit_cycle", gen37),
    "38": ("38_exclusive_range_ledger", gen38),
    "39": ("39_divisor_echo_power", gen39),
    "40": ("40_root_census_modulo_p", gen40),
    "41": ("41_sprinkler_coverage_area", gen41),
    "42": ("42_crystal_hull_surface", gen42),
    "43": ("43_triangle_census_queries", gen43),
    "44": ("44_polygon_triangulation_count", gen44),
    "45": ("45_obstacle_shortcut", gen45),
    "46": ("46_lantern_grid", gen46),
    "47": ("47_quorum_circle", gen47),
    "48": ("48_quiet_committee_census", gen48),
    "49": ("49_glacier_cut", gen49),
}


def same_output(a: str, b: str, checker: str) -> bool:
    x, y = a.split(), b.split()
    if checker != "float":
        return x == y
    return len(x) == len(y) and all(abs(float(s) - float(t)) <= 1e-7 + 1e-7 * abs(float(t)) for s, t in zip(x, y))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", choices=("quick", "full"), default="quick")
    parser.add_argument("--problem", action="append", help="problem number, repeatable")
    parser.add_argument("--lang", choices=("cpp", "py", "both"), default="both")
    parser.add_argument("--timeout", type=int, default=300)
    args = parser.parse_args()
    scale = 1.0 if args.profile == "full" else 0.02
    failures = 0
    with tempfile.TemporaryDirectory(prefix="finale-31-49-") as tmp:
        for number in args.problem or sorted(GENERATORS):
            slug, generator = GENERATORS[number]
            problem = BASE / slug
            manifest = json.loads((problem / "manifest.json").read_text())
            limit = manifest["time_limit_seconds"]
            binary = Path(tmp) / slug
            if args.lang in ("cpp", "both"):
                subprocess.run(["g++", "-std=c++23", "-O2", "-pipe", str(problem / "solution.cpp"), "-o", str(binary)], check=True)
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
                    print(f"{slug:34s} {name:22s} {lang:3s} {elapsed:7.2f}s {memory}  {verdict}", flush=True)
                if len(outputs) == 2 and not same_output(outputs["cpp"], outputs["py"], manifest.get("checker", "tokens")):
                    failures += 1
                    print(f"{slug} {name}: C++ and Python outputs differ")
    print("all cases passed" if not failures else f"{failures} failure(s)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
