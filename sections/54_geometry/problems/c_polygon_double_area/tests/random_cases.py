from __future__ import annotations
import argparse, random, string, subprocess, sys
from pathlib import Path
KIND="polygon"; PROBLEM=Path(__file__).resolve().parents[1]
def expected(inp):
    return subprocess.run([sys.executable,str(PROBLEM/"solution.py")],input=inp,text=True,capture_output=True,check=True).stdout
def case_array(rng):
    n=rng.randint(1,80); a=[rng.randint(-50,50) for _ in range(n)]
    return f"{n}\n"+" ".join(map(str,a))+"\n"
def case_mod(rng):
    n=rng.randint(1,80); k=rng.randint(1,20); a=[rng.randint(-50,50) for _ in range(n)]
    return f"{n} {k}\n"+" ".join(map(str,a))+"\n"
def case_nim(rng):
    t=rng.randint(1,60); lines=[str(t)]
    for _ in range(t):
        n=rng.randint(1,20); a=[rng.randint(0,100) for _ in range(n)]; lines += [str(n), " ".join(map(str,a))]
    return "\n".join(lines)+"\n"
def case_subtract(rng):
    n=rng.randint(1,300); m=rng.randint(1,8); moves=sorted(set(rng.randint(1,20) for _ in range(m)))
    return f"{n} {len(moves)}\n"+" ".join(map(str,moves))+"\n"
def case_grundy(rng):
    n=rng.randint(1,45); e=set()
    for _ in range(rng.randint(0,90)):
        a=rng.randint(1,n); b=rng.randint(a+1,n) if a<n else n
        if a<b: e.add((a,b))
    q=rng.randint(1,35); starts=[rng.randint(1,n) for _ in range(q)]
    return f"{n} {len(e)} {q}\n"+"\n".join(f"{a} {b}" for a,b in sorted(e))+"\n"+" ".join(map(str,starts))+"\n"
def case_comb(rng):
    t=rng.randint(1,60); return str(t)+"\n"+"\n".join(str(rng.randint(0,300)) for _ in range(t))+"\n"
def case_necklace(rng):
    t=rng.randint(1,50); lines=[str(t)]
    for _ in range(t): lines.append(f"{rng.randint(1,80)} {rng.randint(1,20)}")
    return "\n".join(lines)+"\n"
def case_points(rng):
    t=rng.randint(1,80); lines=[str(t)]
    for _ in range(t): lines.append(" ".join(str(rng.randint(-20,20)) for _ in range(6)))
    return "\n".join(lines)+"\n"
def case_segments(rng):
    t=rng.randint(1,80); lines=[str(t)]
    for _ in range(t): lines.append(" ".join(str(rng.randint(-20,20)) for _ in range(8)))
    return "\n".join(lines)+"\n"
def case_polygon(rng):
    n=rng.randint(3,20); pts=[(rng.randint(-20,20),rng.randint(-20,20)) for _ in range(n)]
    return str(n)+"\n"+"\n".join(f"{x} {y}" for x,y in pts)+"\n"
def randstr(rng,n): return "".join(rng.choice("abcde") for _ in range(n))
def case_eqsub(rng):
    n=rng.randint(1,80); q=rng.randint(1,80); s=randstr(rng,n); lines=[s,str(q)]
    for _ in range(q):
        l1=rng.randint(1,n); r1=rng.randint(l1,n); length=r1-l1+1; l2=rng.randint(1,n-length+1); r2=l2+length-1; lines.append(f"{l1} {r1} {l2} {r2}")
    return "\n".join(lines)+"\n"
def case_anagram(rng):
    n=rng.randint(1,80); q=rng.randint(1,80); s=randstr(rng,n); lines=[s,str(q)]
    for _ in range(q):
        l1=rng.randint(1,n); r1=rng.randint(l1,n); length=r1-l1+1; l2=rng.randint(1,n-length+1); r2=l2+length-1; lines.append(f"{l1} {r1} {l2} {r2}")
    return "\n".join(lines)+"\n"
def case_jobs(rng):
    n=rng.randint(1,80); lines=[str(n)]
    for _ in range(n): lines.append(f"{rng.randint(1,50)} {rng.randint(1,200)}")
    return "\n".join(lines)+"\n"
def case_cover(rng):
    target=rng.randint(1,100); n=rng.randint(1,80); lines=[f"{target} {n}"]
    for _ in range(n):
        l=rng.randint(0,target); r=rng.randint(l,target+rng.randint(0,20)); lines.append(f"{l} {r}")
    return "\n".join(lines)+"\n"
def case_mst(rng):
    n=rng.randint(1,30); m=rng.randint(0,100); edges=[]
    for _ in range(m):
        a=rng.randint(1,n); b=rng.randint(1,n)
        if a!=b: edges.append((a,b,rng.randint(1,100)))
    return f"{n} {len(edges)}\n"+"\n".join(f"{a} {b} {w}" for a,b,w in edges)+"\n"
def case_matching(rng):
    n=rng.randint(1,12); m=rng.randint(1,12); e=set()
    for _ in range(rng.randint(0,n*m)):
        e.add((rng.randint(1,n),rng.randint(1,m)))
    return f"{n} {m} {len(e)}\n"+"\n".join(f"{a} {b}" for a,b in sorted(e))+"\n"
def case_sat(rng):
    n=rng.randint(1,10); m=rng.randint(0,30); lines=[f"{n} {m}"]
    for _ in range(m):
        a=rng.randint(1,n)*rng.choice([-1,1]); b=rng.randint(1,n)*rng.choice([-1,1]); lines.append(f"{a} {b}")
    return "\n".join(lines)+"\n"
def case_score(rng):
    n=rng.randint(1,30); lines=[str(n)]
    for i in range(n): lines.append(f"team{i} {rng.randint(0,10)} {rng.randint(0,1000)}")
    return "\n".join(lines)+"\n"
def case_assign(rng):
    n=rng.randint(1,10); a=[rng.randint(1,60) for _ in range(n)]
    return f"{n}\n"+" ".join(map(str,a))+"\n"
def case_mitm(rng):
    n=rng.randint(1,28); x=rng.randint(0,200); a=[rng.randint(0,40) for _ in range(n)]
    return f"{n} {x}\n"+" ".join(map(str,a))+"\n"
def case_crt(rng):
    t=rng.randint(1,50); lines=[str(t)]
    for _ in range(t):
        m1=rng.randint(1,60); m2=rng.randint(1,60); lines.append(f"{rng.randint(0,m1-1)} {m1} {rng.randint(0,m2-1)} {m2}")
    return "\n".join(lines)+"\n"
def case_matrix(rng):
    t=rng.randint(1,50); return str(t)+"\n"+"\n".join(str(rng.randint(0,10**6)) for _ in range(t))+"\n"
BUILDERS={"parity":case_array,"xor_split":case_array,"mod_equal":case_mod,"nim":case_nim,"subtract":case_subtract,"grundy":case_grundy,"catalan":case_comb,"derange":case_comb,"necklace":case_necklace,"orient":case_points,"segments":case_segments,"polygon":case_polygon,"eqsub":case_eqsub,"pal":case_eqsub,"anagram":case_anagram,"jobs":case_jobs,"cover":case_cover,"mst":case_mst,"matching":case_matching,"sat":case_sat,"score":case_score,"assign":case_assign,"mitm_best":case_mitm,"crt":case_crt,"matrix":case_matrix}
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--count",type=int,required=True); ap.add_argument("--seed",type=int,required=True); ap.add_argument("--out-dir",type=Path,required=True)
    args=ap.parse_args(); args.out_dir.mkdir(parents=True,exist_ok=True); rng=random.Random(args.seed); builder=BUILDERS[KIND]
    for i in range(args.count):
        inp=builder(rng); stem=f"case{i:03d}"; (args.out_dir/f"{stem}.in").write_text(inp); (args.out_dir/f"{stem}.out").write_text(expected(inp))
if __name__=="__main__": main()
