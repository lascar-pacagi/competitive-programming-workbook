from __future__ import annotations
import argparse, random
from pathlib import Path

def brute(words):
    answers=[]
    for word in words:
        answer=-1
        for length in range(1,len(word)+1):
            prefix=word[:length]
            if sum(other.startswith(prefix) for other in words)==1:
                answer=length
                break
        answers.append(answer)
    return answers

def main():
    p=argparse.ArgumentParser(); p.add_argument('--count',type=int,required=True); p.add_argument('--seed',type=int,required=True); p.add_argument('--out-dir',type=Path,required=True)
    a=p.parse_args(); a.out_dir.mkdir(parents=True,exist_ok=True); rng=random.Random(a.seed)
    for c in range(a.count):
        if c==0:
            words=['a']*200000; answers=[-1]*200000
        elif c==1:
            # One extremely deep insertion complements the duplicate-heavy
            # throughput case above. Its first character is already unique.
            words=['a'*200000]; answers=[1]
        else:
            words=[''.join(rng.choice('abcd') for _ in range(rng.randint(1,7))) for _ in range(rng.randint(1,35))]
            answers=brute(words)
        z=a.out_dir/f'case{c:03d}'
        z.with_suffix('.in').write_text(str(len(words))+'\n'+'\n'.join(words)+'\n')
        z.with_suffix('.out').write_text('\n'.join(map(str,answers))+'\n')
if __name__=='__main__': main()
