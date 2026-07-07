from __future__ import annotations

import argparse
import random
import subprocess
import sys
from pathlib import Path


KIND = "mo_distinct"
PROBLEM = Path(__file__).resolve().parents[1]


def expected(inp: str) -> str:
    result = subprocess.run(
        [sys.executable, str(PROBLEM / "solution.py")],
        input=inp,
        text=True,
        capture_output=True,
        check=True,
    )
    return result.stdout


def case_fenwick_sum(rng: random.Random) -> str:
    n = rng.randint(1, 30)
    q = rng.randint(1, 60)
    a = [rng.randint(-20, 20) for _ in range(n)]
    ops = []
    for _ in range(q):
        if rng.random() < 0.55:
            i = rng.randint(1, n)
            x = rng.randint(-15, 15)
            ops.append(f"1 {i} {x}")
        else:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            ops.append(f"2 {l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(ops) + "\n"


def case_inversions(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    a = [rng.randint(-30, 30) for _ in range(n)]
    return f"{n}\n" + " ".join(map(str, a)) + "\n"


def case_range_add_point(rng: random.Random) -> str:
    n = rng.randint(1, 35)
    q = rng.randint(1, 70)
    a = [rng.randint(-20, 20) for _ in range(n)]
    ops = []
    for _ in range(q):
        if rng.random() < 0.65:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            x = rng.randint(-10, 10)
            ops.append(f"1 {l} {r} {x}")
        else:
            i = rng.randint(1, n)
            ops.append(f"2 {i}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(ops) + "\n"


def case_seg_min(rng: random.Random) -> str:
    n = rng.randint(1, 32)
    q = rng.randint(1, 70)
    a = [rng.randint(-50, 50) for _ in range(n)]
    ops = []
    for _ in range(q):
        if rng.random() < 0.5:
            i = rng.randint(1, n)
            x = rng.randint(-50, 50)
            ops.append(f"1 {i} {x}")
        else:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            ops.append(f"2 {l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(ops) + "\n"


def case_max_subarray(rng: random.Random) -> str:
    n = rng.randint(1, 30)
    q = rng.randint(1, 60)
    a = [rng.randint(-20, 20) for _ in range(n)]
    ops = [f"{rng.randint(1, n)} {rng.randint(-20, 20)}" for _ in range(q)]
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(ops) + "\n"


def case_lazy_sum(rng: random.Random) -> str:
    n = rng.randint(1, 35)
    q = rng.randint(1, 70)
    a = [rng.randint(-20, 20) for _ in range(n)]
    ops = []
    for _ in range(q):
        if rng.random() < 0.6:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            x = rng.randint(-15, 15)
            ops.append(f"1 {l} {r} {x}")
        else:
            l = rng.randint(1, n)
            r = rng.randint(l, n)
            ops.append(f"2 {l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(ops) + "\n"


def case_static_min(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    q = rng.randint(1, 80)
    a = [rng.randint(-100, 100) for _ in range(n)]
    queries = []
    for _ in range(q):
        l = rng.randint(1, n)
        r = rng.randint(l, n)
        queries.append(f"{l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(queries) + "\n"


def case_static_gcd(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    q = rng.randint(1, 80)
    a = [rng.randint(1, 200) for _ in range(n)]
    queries = []
    for _ in range(q):
        l = rng.randint(1, n)
        r = rng.randint(l, n)
        queries.append(f"{l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(queries) + "\n"


def case_kth_ancestor(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    q = rng.randint(1, 80)
    parents = [rng.randint(1, v - 1) for v in range(2, n + 1)]
    queries = [f"{rng.randint(1, n)} {rng.randint(0, n + 5)}" for _ in range(q)]
    return f"{n} {q}\n" + (" ".join(map(str, parents)) if parents else "") + "\n" + "\n".join(queries) + "\n"


def case_running_median(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    a = [rng.randint(-100, 100) for _ in range(n)]
    return f"{n}\n" + " ".join(map(str, a)) + "\n"


def case_course_rooms(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    intervals = []
    for _ in range(n):
        l = rng.randint(0, 200)
        r = l + rng.randint(1, 40)
        intervals.append(f"{l} {r}")
    return f"{n}\n" + "\n".join(intervals) + "\n"


def case_pair_sums(rng: random.Random) -> str:
    n = rng.randint(1, 25)
    m = rng.randint(1, 25)
    k = rng.randint(1, min(80, n * m))
    a = sorted(rng.randint(-30, 30) for _ in range(n))
    b = sorted(rng.randint(-30, 30) for _ in range(m))
    return f"{n} {m} {k}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, b)) + "\n"


def case_hotel(rng: random.Random) -> str:
    n = rng.randint(1, 50)
    q = rng.randint(1, 80)
    a = [rng.randint(1, 30) for _ in range(n)]
    req = [rng.randint(1, 40) for _ in range(q)]
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, req)) + "\n"


def case_list_removals(rng: random.Random) -> str:
    n = rng.randint(1, 60)
    a = [rng.randint(-100, 100) for _ in range(n)]
    alive = n
    pos = []
    for _ in range(n):
        p = rng.randint(1, alive)
        pos.append(p)
        alive -= 1
    return f"{n}\n" + " ".join(map(str, a)) + "\n" + " ".join(map(str, pos)) + "\n"


def case_mo_distinct(rng: random.Random) -> str:
    n = rng.randint(1, 80)
    q = rng.randint(1, 80)
    a = [rng.randint(1, 25) for _ in range(n)]
    queries = []
    for _ in range(q):
        l = rng.randint(1, n)
        r = rng.randint(l, n)
        queries.append(f"{l} {r}")
    return f"{n} {q}\n" + " ".join(map(str, a)) + "\n" + "\n".join(queries) + "\n"


BUILDERS = {
    "fenwick_sum": case_fenwick_sum,
    "inversions": case_inversions,
    "range_add_point": case_range_add_point,
    "seg_min": case_seg_min,
    "max_subarray": case_max_subarray,
    "lazy_sum": case_lazy_sum,
    "static_min": case_static_min,
    "static_gcd": case_static_gcd,
    "kth_ancestor": case_kth_ancestor,
    "running_median": case_running_median,
    "course_rooms": case_course_rooms,
    "pair_sums": case_pair_sums,
    "hotel": case_hotel,
    "list_removals": case_list_removals,
    "mo_distinct": case_mo_distinct,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", type=int, required=True)
    parser.add_argument("--seed", type=int, required=True)
    parser.add_argument("--out-dir", type=Path, required=True)
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(args.seed)
    builder = BUILDERS[KIND]
    for i in range(args.count):
        inp = builder(rng)
        stem = f"case{i:03d}"
        (args.out_dir / f"{stem}.in").write_text(inp, encoding="utf-8")
        (args.out_dir / f"{stem}.out").write_text(expected(inp), encoding="utf-8")


if __name__ == "__main__":
    main()
