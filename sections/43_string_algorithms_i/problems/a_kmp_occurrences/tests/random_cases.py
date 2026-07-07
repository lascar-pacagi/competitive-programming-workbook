from __future__ import annotations

import argparse
import random
import string
import subprocess
import sys
from pathlib import Path


KIND = "kmp"
PROBLEM = Path(__file__).resolve().parents[1]


def expected(inp: str) -> str:
    result = subprocess.run([sys.executable, str(PROBLEM / "solution.py")], input=inp, text=True, capture_output=True, check=True)
    return result.stdout


def tree(n, rng, weighted=False):
    lines = []
    for v in range(2, n + 1):
        p = rng.randint(1, v - 1)
        if weighted:
            lines.append(f"{p} {rng.randint(1, 30)}")
        else:
            lines.append(str(p))
    return lines


def case_lca_distance(rng):
    n = rng.randint(1, 50); q = rng.randint(1, 70)
    lines = [f"{n} {q}"] + tree(n, rng, False)
    lines += [f"{rng.randint(1,n)} {rng.randint(1,n)}" for _ in range(q)]
    return "\n".join(lines) + "\n"


def case_lca_max(rng):
    n = rng.randint(1, 50); q = rng.randint(1, 70)
    lines = [f"{n} {q}"] + tree(n, rng, True)
    lines += [f"{rng.randint(1,n)} {rng.randint(1,n)}" for _ in range(q)]
    return "\n".join(lines) + "\n"


def case_kth_path(rng):
    n = rng.randint(1, 45); q = rng.randint(1, 70)
    parents = [0, 0]
    lines = [f"{n} {q}"]
    for v in range(2, n + 1):
        p = rng.randint(1, v - 1); parents.append(p); lines.append(str(p))
    depth = [0] * (n + 1)
    for v in range(2, n + 1): depth[v] = depth[parents[v]] + 1
    for _ in range(q):
        u = rng.randint(1, n); v = rng.randint(1, n)
        k = rng.randint(1, n + 3)
        lines.append(f"{u} {v} {k}")
    return "\n".join(lines) + "\n"


def case_order_stat(rng):
    m = rng.randint(5, 80); q = rng.randint(1, 120); counts = [0]*(m+1); lines=[f"{m} {q}"]
    for _ in range(q):
        typ = rng.choices([1,2,3,4], [4,3,3,3])[0]
        if typ == 1:
            x = rng.randint(1,m); counts[x]+=1; lines.append(f"1 {x}")
        elif typ == 2:
            x = rng.randint(1,m); counts[x]=max(0,counts[x]-1); lines.append(f"2 {x}")
        elif typ == 3:
            lines.append(f"3 {rng.randint(1, max(1, sum(counts)+3))}")
        else:
            lines.append(f"4 {rng.randint(1,m)}")
    return "\n".join(lines)+"\n"


def case_range_add_sum(rng):
    n = rng.randint(1,40); q = rng.randint(1,80); a=[rng.randint(-20,20) for _ in range(n)]
    lines=[f"{n} {q}", " ".join(map(str,a))]
    for _ in range(q):
        if rng.random()<0.6:
            l=rng.randint(1,n); r=rng.randint(l,n); x=rng.randint(-10,10); lines.append(f"1 {l} {r} {x}")
        else:
            l=rng.randint(1,n); r=rng.randint(l,n); lines.append(f"2 {l} {r}")
    return "\n".join(lines)+"\n"


def case_rect_count(rng):
    n=rng.randint(1,60); q=rng.randint(1,70)
    pts=[(rng.randint(1,50), rng.randint(1,50)) for _ in range(n)]
    lines=[f"{n} {q}"]+[f"{x} {y}" for x,y in pts]
    for _ in range(q):
        x1=rng.randint(1,50); x2=rng.randint(x1,50); y1=rng.randint(1,50); y2=rng.randint(y1,50)
        lines.append(f"{x1} {y1} {x2} {y2}")
    return "\n".join(lines)+"\n"


def randstr(rng, n):
    return "".join(rng.choice("abac") for _ in range(n))


def case_kmp(rng):
    p=randstr(rng,rng.randint(1,8)); t=randstr(rng,rng.randint(1,50))
    return p+"\n"+t+"\n"


def case_borders(rng):
    return randstr(rng,rng.randint(1,60))+"\n"


def case_period(rng):
    base=randstr(rng,rng.randint(1,8)); reps=rng.randint(1,8)
    s=base*reps if rng.random()<0.6 else randstr(rng,rng.randint(1,60))
    return s+"\n"


def case_trie(rng):
    n=rng.randint(1,40); q=rng.randint(1,40)
    words=["".join(rng.choice(string.ascii_lowercase[:5]) for _ in range(rng.randint(1,8))) for _ in range(n)]
    prefs=["".join(rng.choice(string.ascii_lowercase[:5]) for _ in range(rng.randint(1,5))) for _ in range(q)]
    return f"{n} {q}\n"+"\n".join(words+prefs)+"\n"


def case_pal_hash(rng):
    n=rng.randint(1,70); q=rng.randint(1,80); s=randstr(rng,n); lines=[s, str(q)]
    for _ in range(q):
        l=rng.randint(1,n); r=rng.randint(l,n); lines.append(f"{l} {r}")
    return "\n".join(lines)+"\n"


def case_distinct_substrings(rng):
    return randstr(rng,rng.randint(1,60))+"\n"


def case_flow(rng):
    n=rng.randint(2,12); m=rng.randint(1,35); lines=[f"{n} {m}"]
    for _ in range(m):
        u=rng.randint(1,n-1); v=rng.randint(u+1,n); c=rng.randint(1,20); lines.append(f"{u} {v} {c}")
    return "\n".join(lines)+"\n"


def case_matching(rng):
    n=rng.randint(1,12); m=rng.randint(1,12); e=rng.randint(0,n*m); edges=set()
    while len(edges)<e: edges.add((rng.randint(1,n), rng.randint(1,m)))
    return f"{n} {m} {len(edges)}\n"+"\n".join(f"{a} {b}" for a,b in sorted(edges))+"\n"


BUILDERS = {
    "lca_distance": case_lca_distance, "lca_max": case_lca_max, "kth_path": case_kth_path,
    "order_stat": case_order_stat, "range_add_sum": case_range_add_sum, "rect_count": case_rect_count,
    "kmp": case_kmp, "borders": case_borders, "period": case_period,
    "trie": case_trie, "pal_hash": case_pal_hash, "distinct_substrings": case_distinct_substrings,
    "flow": case_flow, "matching": case_matching, "mincut": case_flow,
}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--count",type=int,required=True); ap.add_argument("--seed",type=int,required=True); ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args(); args.out_dir.mkdir(parents=True,exist_ok=True); rng=random.Random(args.seed); builder=BUILDERS[KIND]
    for i in range(args.count):
        inp=builder(rng); stem=f"case{i:03d}"
        (args.out_dir/f"{stem}.in").write_text(inp,encoding="utf-8")
        (args.out_dir/f"{stem}.out").write_text(expected(inp),encoding="utf-8")


if __name__ == "__main__":
    main()
