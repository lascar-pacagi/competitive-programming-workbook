from __future__ import annotations
import argparse, random, subprocess, sys
from pathlib import Path
KIND="deque_dp"; PROBLEM=Path(__file__).resolve().parents[1]
def expected(inp):
    return subprocess.run([sys.executable,str(PROBLEM/"solution.py")],input=inp,text=True,capture_output=True,check=True).stdout
def tree(n,rng):
    return [(rng.randint(1,v-1),v) for v in range(2,n+1)]
def case_tree(rng):
    n=rng.randint(1,70); return f"{n}\n"+"\n".join(f"{a} {b}" for a,b in tree(n,rng))+"\n"
def case_mitm_leq(rng):
    n=rng.randint(1,28); x=rng.randint(0,200); a=[rng.randint(0,40) for _ in range(n)]
    return f"{n} {x}\n"+" ".join(map(str,a))+"\n"
def case_mitm_target(rng):
    n=rng.randint(1,28); t=rng.randint(-50,200); a=[rng.randint(-30,50) for _ in range(n)]
    return f"{n} {t}\n"+" ".join(map(str,a))+"\n"
def case_partition(rng):
    n=rng.randint(1,55); k=rng.randint(1,min(8,n)); a=[rng.randint(0,15) for _ in range(n)]
    return f"{n} {k}\n"+" ".join(map(str,a))+"\n"
def case_deque_dp(rng):
    n=rng.randint(1,80); w=rng.randint(1,n); a=[rng.randint(-20,20) for _ in range(n)]
    return f"{n} {w}\n"+" ".join(map(str,a))+"\n"
def case_knuth(rng):
    n=rng.randint(1,35); a=[rng.randint(1,20) for _ in range(n)]
    return f"{n}\n"+" ".join(map(str,a))+"\n"
def case_lines(rng):
    q=rng.randint(1,90); lines=[str(q)]; added=False
    for _ in range(q):
        if not added or rng.random()<0.6:
            m=rng.randint(-20,20); b=rng.randint(-50,50); lines.append(f"1 {m} {b}"); added=True
        else:
            x=rng.randint(-30,30); lines.append(f"2 {x}")
    return "\n".join(lines)+"\n"
def case_cht_dp(rng):
    n=rng.randint(1,80); c=rng.randint(-20,50); xs=[]; cur=0
    for _ in range(n): cur+=rng.randint(0,8); xs.append(cur)
    return f"{n} {c}\n"+" ".join(map(str,xs))+"\n"
def case_grundy(rng):
    n=rng.randint(1,50); m=rng.randint(0,120); edges=set()
    for _ in range(m):
        a=rng.randint(1,n); b=rng.randint(a+1,n) if a<n else n
        if a<b: edges.add((a,b))
    q=rng.randint(1,40); starts=[rng.randint(1,n) for _ in range(q)]
    return f"{n} {len(edges)} {q}\n"+"\n".join(f"{a} {b}" for a,b in sorted(edges))+"\n"+" ".join(map(str,starts))+"\n"
def case_crt(rng):
    t=rng.randint(1,40); lines=[str(t)]
    for _ in range(t):
        m1=rng.randint(1,50); m2=rng.randint(1,50); a1=rng.randint(0,m1-1); a2=rng.randint(0,m2-1)
        lines.append(f"{a1} {m1} {a2} {m2}")
    return "\n".join(lines)+"\n"
def case_matrix(rng):
    t=rng.randint(1,40); return str(t)+"\n"+"\n".join(str(rng.randint(0,10**6)) for _ in range(t))+"\n"
BUILDERS={"tree_sum":case_tree,"tree_far":case_tree,"tree_pairs":case_tree,"mitm_leq":case_mitm_leq,"mitm_best":case_mitm_leq,"mitm_close":case_mitm_target,"partition":case_partition,"deque_dp":case_deque_dp,"knuth":case_knuth,"lines":case_lines,"cht_dp":case_cht_dp,"lines_max":case_lines,"grundy":case_grundy,"crt":case_crt,"matrix":case_matrix}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--count",type=int,required=True); ap.add_argument("--seed",type=int,required=True); ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args(); args.out_dir.mkdir(parents=True,exist_ok=True); rng=random.Random(args.seed); builder=BUILDERS[KIND]
    for i in range(args.count):
        inp=builder(rng); stem=f"case{i:03d}"; (args.out_dir/f"{stem}.in").write_text(inp); (args.out_dir/f"{stem}.out").write_text(expected(inp))
if __name__=="__main__": main()
