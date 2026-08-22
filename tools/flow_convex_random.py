"""Independent tiny brute-force generators for Sections 70--72."""

from __future__ import annotations

import argparse
import itertools
import random
from pathlib import Path


def circulation(rng):
    n = rng.randint(2, 5)
    m = rng.randint(1, 7)
    edges = []
    for _ in range(m):
        u = rng.randrange(n)
        v = rng.randrange(n - 1)
        if v >= u:
            v += 1
        low = rng.randint(0, 2)
        edges.append((u, v, low, rng.randint(low, 3)))
    ok = False
    for values in itertools.product(
        *(range(lo, hi + 1) for _, _, lo, hi in edges)
    ):
        balance = [0] * n
        for (u, v, _, _), value in zip(edges, values):
            balance[u] -= value
            balance[v] += value
        if not any(balance):
            ok = True
            break
    text = (
        f"{n} {m}\n"
        + "\n".join(f"{u+1} {v+1} {lo} {hi}" for u, v, lo, hi in edges)
        + "\n"
    )
    return text, ("YES\n" if ok else "NO\n")


def shipment(rng):
    n = rng.randint(2, 5)
    possible = [(u, v) for u in range(n) for v in range(u + 1, n)]
    rng.shuffle(possible)
    edges = []
    for u, v in possible[: rng.randint(1, min(7, len(possible)))]:
        edges.append((u, v, rng.randint(0, 2), rng.randint(-4, 7)))
    need = rng.randint(0, 3)
    best = None
    for values in itertools.product(
        *(range(cap + 1) for _, _, cap, _ in edges)
    ):
        balance = [0] * n
        cost = 0
        for (u, v, _, price), value in zip(edges, values):
            balance[u] -= value
            balance[v] += value
            cost += value * price
        if (
            balance[0] == -need
            and balance[-1] == need
            and not any(balance[1:-1])
        ):
            best = cost if best is None else min(best, cost)
    text = (
        f"{n} {len(edges)} {need}\n1 {n}\n"
        + "\n".join(f"{u+1} {v+1} {cap} {cost}" for u, v, cap, cost in edges)
        + ("\n" if edges else "")
    )
    return text, ("IMPOSSIBLE\n" if best is None else f"{best}\n")


def quota(rng, convex=False):
    n = rng.randint(1, 6)
    p = rng.randint(1, 4)
    bounds = []
    for _ in range(p):
        lo = rng.randint(0, min(2, n))
        bounds.append((lo, rng.randint(lo, n), rng.randint(0, 3)))
    eligible = []
    choices = [[] for _ in range(n)]
    for w in range(n):
        for j in range(p):
            if rng.random() < 0.7:
                profit = rng.randint(0, 12)
                eligible.append((w, j, profit))
                choices[w].append((j, profit))
    best = None
    if all(choices):
        for assignment in itertools.product(*choices):
            count = [0] * p
            profit = 0
            for j, value in assignment:
                count[j] += 1
                profit += value
            if all(
                bounds[j][0] <= count[j] <= bounds[j][1] for j in range(p)
            ):
                value = profit
                if convex:
                    value -= sum(
                        bounds[j][2] * count[j] ** 2 for j in range(p)
                    )
                best = value if best is None else max(best, value)
    head = f"{n} {p} {len(eligible)}\n"
    if convex:
        head += "\n".join(f"{lo} {hi} {a}" for lo, hi, a in bounds) + "\n"
    else:
        head += "\n".join(f"{lo} {hi}" for lo, hi, _ in bounds) + "\n"
    head += "\n".join(f"{w+1} {j+1} {value}" for w, j, value in eligible)
    if eligible:
        head += "\n"
    return head, ("IMPOSSIBLE\n" if best is None else f"{best}\n")


def monotone(rng):
    n = rng.randint(1, 8)
    values = [rng.randint(-4, 6) for _ in range(n)]
    candidates = range(min(values), max(values) + 1)
    best = min(
        sum(abs(x - y) for x, y in zip(values, chosen))
        for chosen in itertools.combinations_with_replacement(candidates, n)
    )
    return f"{n}\n" + " ".join(map(str, values)) + "\n", f"{best}\n"


def mst(rng):
    n = rng.randint(2, 6)
    pairs = list(itertools.combinations(range(n), 2))
    rng.shuffle(pairs)
    edges = []
    for u, v in pairs[: rng.randint(n - 1, min(len(pairs), 9))]:
        edges.append((u, v, rng.randint(-5, 12), rng.randrange(2)))
    wanted = rng.randrange(n)
    best = None
    for chosen in itertools.combinations(range(len(edges)), n - 1):
        parent = list(range(n))

        def find(x):
            while x != parent[x]:
                x = parent[x]
            return x

        cost = red = 0
        ok = True
        for index in chosen:
            u, v, w, color = edges[index]
            a, b = find(u), find(v)
            if a == b:
                ok = False
                break
            parent[b] = a
            cost += w
            red += color
        if ok and red == wanted:
            best = cost if best is None else min(best, cost)
    text = (
        f"{n} {len(edges)} {wanted}\n"
        + "\n".join(
            f"{u+1} {v+1} {w} {'R' if red else 'B'}" for u, v, w, red in edges
        )
        + "\n"
    )
    return text, ("IMPOSSIBLE\n" if best is None else f"{best}\n")


def allocation(rng):
    n = rng.randint(1, 5)
    machines = [
        (rng.randint(1, 4), rng.randint(-5, 5), rng.randint(0, 5))
        for _ in range(n)
    ]
    k = rng.randint(0, 10)
    best = None
    for values in itertools.product(
        *(range(cap + 1) for _, _, cap in machines)
    ):
        if sum(values) == k:
            cost = sum(
                a * x * x + b * x for (a, b, _), x in zip(machines, values)
            )
            best = cost if best is None else min(best, cost)
    text = (
        f"{n} {k}\n"
        + "\n".join(f"{a} {b} {cap}" for a, b, cap in machines)
        + "\n"
    )
    return text, ("IMPOSSIBLE\n" if best is None else f"{best}\n")


def matrix(rng):
    rows = rng.randint(1, 4)
    cols = rng.randint(1, 4)
    allowed = [
        (r, c) for r in range(rows) for c in range(cols) if rng.random() < 0.7
    ]
    need = [rng.randint(0, cols) for _ in range(rows)]
    bounds = []
    for _ in range(cols):
        lo = rng.randint(0, rows)
        bounds.append((lo, rng.randint(lo, rows)))
    ok = False
    for mask in range(1 << len(allowed)):
        rc = [0] * rows
        cc = [0] * cols
        for i, (r, c) in enumerate(allowed):
            if mask >> i & 1:
                rc[r] += 1
                cc[c] += 1
        if rc == need and all(
            lo <= cc[c] <= hi for c, (lo, hi) in enumerate(bounds)
        ):
            ok = True
            break
    text = f"{rows} {cols} {len(allowed)}\n" + " ".join(map(str, need)) + "\n"
    text += "\n".join(f"{lo} {hi}" for lo, hi in bounds) + "\n"
    text += "\n".join(f"{r+1} {c+1}" for r, c in allowed) + (
        "\n" if allowed else ""
    )
    return text, ("YES\n" if ok else "NO\n")


GENERATORS = {
    "circulation": circulation,
    "shipment": shipment,
    "quota": quota,
    "monotone": monotone,
    "mst": mst,
    "allocation": allocation,
    "matrix": matrix,
    "convex_quota": lambda rng: quota(rng, True),
}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("kind", choices=GENERATORS)
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    for case in range(args.count):
        inp, out = GENERATORS[args.kind](rng)
        stem = args.out_dir / f"case{case:03d}"
        stem.with_suffix(".in").write_text(inp)
        stem.with_suffix(".out").write_text(out)


if __name__ == "__main__":
    main()
