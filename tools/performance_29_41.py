"""Number-theory and data-structure scale cases with independent identities."""
import math
N=200_000
MOD=1_000_000_007


def binomial(n,k):
    # Multiplicative formula instead of the solution's factorial tables.
    k=min(k,n-k);a=b=1
    for i in range(1,k+1):a=a*(n-k+i)%MOD;b=b*i%MOD
    return a*pow(b,MOD-2,MOD)%MOD


def totient_prefix(n):
    phi=list(range(n+1))
    for p in range(2,n+1):
        if phi[p]==p:
            for k in range(p,n+1,p):phi[k]-=phi[k]//p
    return sum(phi[1:])%MOD


def build(section,slug):
    n=q=N;h=n//2
    if section==29:
        if slug.startswith('a_'):return f'{q}\n'+f'{MOD-1} 1000000000000000000 {MOD}\n'*q,'1\n'*q
        if slug.startswith('b_'):return f'{MOD} {q}\n'+'1 2\n'*q,'500000004\n'*q
        return f'{q}\n'+f'{MOD-1} 1 0 999999999999999999\n'*q,'1\n'*q
    if section==30:
        if slug.startswith('a_'):
            a,b=832040,514229
            return f'{q}\n'+f'{a} {b}\n'*q,f'1 {a*b}\n'*q
        if slug.startswith('b_'):return f'{q}\n'+'999999999 1000000000\n'*q,'999999999\n'*q
        # Any valid witness is accepted by the dedicated Diophantine checker.
        return f'{q}\n'+'999999999 1000000000 1\n'*q,'-1 1\n'*q
    if section==31:
        if slug.startswith('a_'):
            # pi(10^6)=78498, independently tabulated prime-counting constant.
            return f'1000000 {q}\n'+'1 1000000\n'*q,'78498\n'*q
        if slug.startswith('b_'):return f'{q}\n'+'999983\n'*(q-1)+'1000000\n','1 1 999983\n'*(q-1)+'2 12 5\n'
        return f'{q}\n'+'999983\n'*(q-1)+'1000000\n','2\n'*(q-1)+'49\n'
    if section==32:
        if slug.startswith('a_'):
            # Central binomial values require full preprocessing and hard queries.
            answer=binomial(1_000_000,500_000)
            return f'{q}\n'+'1000000 500000\n'*q,f'{answer}\n'*q
        if slug.startswith('b_'):
            return 'a'*500000+'b'*500000+'\n',f'{binomial(1_000_000,500_000)}\n'
        return f'{q}\n'+'1000000 1000000\n'*q,f'{binomial(1_999_999,999_999)}\n'*q
    if section==33:
        if slug.startswith('a_'):
            # Repeated divisor 2 still drives all 2^20 terms of an unoptimized
            # inclusion-exclusion implementation; union is simply the evens.
            return '1000000000000000000 20\n'+'2 '*20+'\n','500000000000000000\n'
        if slug.startswith('b_'):
            # Finite differences of x^n count surjections independently of
            # the reference's binomial preprocessing. Both limits are full.
            ans=sum((-1)**i*math.comb(500,i)*pow(500-i,10**9,MOD) for i in range(501))%MOD
            return '200\n'+'1000000000 500\n'*200,f'{ans}\n'*200
        if slug.startswith('c_'):
            # 200 * min(5000,5000) reaches the aggregate million-term bound.
            # Zero caps with positive sum have zero valid allocations.
            return '200\n'+'5000 5000 0\n'*200,'0\n'*200
        # Derangements via the alternating factorial formula, independent of
        # the usual D(n)=(n-1)*(D(n-1)+D(n-2)) reference recurrence.
        top=1_000_000;factorial=1
        for i in range(2,top+1):factorial=factorial*i%MOD
        invfact=[1]*(top+1);invfact[top]=pow(factorial,MOD-2,MOD)
        for i in range(top,0,-1):invfact[i-1]=invfact[i]*i%MOD
        ans=factorial*sum((-v if i%2 else v) for i,v in enumerate(invfact))%MOD
        return f'{top}\n',f'{ans}\n'
    if section==34:
        if slug.startswith('a_'):return f'{n}\n'+'1 2 2\n'*n,f'{n}\n'
        return f'{q}\n'+'1 1000000006\n'*q,'1000000006\n'*q
    if section==35:
        letter=slug.split('_')[0]
        if letter=='a':return '1000000 1000000 1 2\n',f'{binomial(1_999_998,999_999)*pow(2,MOD-2,MOD)%MOD}\n'
        if letter=='b':return f'{n}\n'+'1 '*h+'1000000 '*h+'\n',f'{(h*(h-1)//2+h*h)}\n'
        if letter=='c':return f'{n}\n'+'1 2\n'*n,f'{(1-pow(pow(2,MOD-2,MOD),n,MOD))%MOD}\n'
        if letter=='d':
            k=20;length=10**18
            ans=sum((-1)**i*math.comb(k,i)*pow(k-i,length,MOD) for i in range(k+1))%MOD
            return f'{length} {k}\n',f'{ans}\n'
        if letter=='e':return f'{q}\n'+'999999999 1 0 1000000000\n'*q,'999999999\n'*q
        if letter=='f':return f'{q}\n'+'0 999999999 1 1000000000\n'*q,'999999998000000001\n'*q
        if letter=='g':return '20 0\n'+'999999900 '*20+'\n','1\n'
        if letter=='h':return f'{n}\n'+'1 '*(n-1)+'1000000\n',f'{(pow(2,n,MOD)-2)%MOD}\n'
        if letter=='i':
            # Max query count and aggregate k; max n and m on each query.
            return f'{q}\n'+'1000000000000000000 200000 1\n'*q,'200000\n'*q
        if letter=='j':return f'{n} 223092870\n'+'223092870 '*n+'\n',f'{(pow(2,n,MOD)-1)%MOD}\n'
        if letter=='k':
            expected=20*sum(pow(i,MOD-2,MOD) for i in range(1,21))%MOD
            return '20\n'+'1 '*20+'\n',f'{expected}\n'
        if letter=='l':
            # A prime has exactly one proper positive divisor, namely 1.
            return f'{q}\n'+'999983 '*q+'\n','1\n'*q
        if letter=='m':return f'{q}\n'+'1000000 '*q+'\n',f'{totient_prefix(1_000_000)}\n'*q
        if letter=='n':
            # Mark prime squares directly, unlike Mobius summation.
            limit=1_000_000;ok=bytearray(b'\1')*(limit+1);ok[0]=0
            for d in range(2,1001):
                square=d*d;ok[square::square]=b'\0'*(limit//square)
            return f'{q}\n'+'1000000 '*q+'\n',f'{sum(ok)}\n'*q
        if letter=='o':
            # Independent divisor convolution, not the reference's SPF recurrence.
            limit=1_000_000;phi=list(range(limit+1))
            for p in range(2,limit+1):
                if phi[p]==p:
                    for k in range(p,limit+1,p):phi[k]-=phi[k]//p
            sums=[0]*(limit+1)
            for d in range(1,limit+1):
                step=phi[d];value=step
                for multiple in range(d,limit+1,d):sums[multiple]+=value;value+=step
            queries=range(limit-q+1,limit+1)
            return f'{q}\n'+' '.join(map(str,queries))+'\n',''.join(f'{sums[x]%MOD}\n' for x in queries)
        if letter=='p':return f'{n}\n'+'1000000 '*n+'\n',f'{n*(n+1)//2*1000000%MOD}\n'
        if letter=='q':
            # On a square, coprime ordered pairs = 2*sum(phi)-1.
            answer=(2*totient_prefix(1_000_000)-1)%MOD
            return '5000\n'+'1000000 1000000\n'*5000,f'{answer}\n'*5000
        if letter=='r':
            # Two divisors means prime; three means the square of a prime.
            # pi(10^6)=78498 and pi(1000)=168 give independent counts.
            return '200\n'+'1000000 2\n1000000 3\n'*100,'78498\n168\n'*100
    if section==36:
        if slug.startswith('a_'):
            return f'{n} {q}\n'+'0 '*n+'\n'+''.join(f'1 {n} 1\n2 {i} {n}\n' for i in range(1,h+1)),''.join(f'{i}\n' for i in range(1,h+1))
        if slug.startswith('b_'):return f'{n}\n'+' '.join(map(str,range(n,0,-1)))+'\n',f'{n*(n-1)//2}\n'
        return f'{n} {q}\n'+'0 '*n+'\n'+''.join(f'1 {i} {n} 1\n2 {n}\n' for i in range(1,h+1)),''.join(f'{i}\n' for i in range(1,h+1))
    if section==37:
        if slug.startswith('a_'):return f'{n} {q}\n'+'1 '*n+'\n'+f'1 {n} -1\n2 1 {n}\n'*h,'-1\n'*h
        if slug.startswith('b_'):return f'{n} {q}\n'+'-1 '*n+'\n'+''.join(f'{i} 1\n' for i in range(1,q+1)),''.join(f'{i}\n' for i in range(1,q+1))
        return f'{n} {q}\n'+'0 '*n+'\n'+''.join(f'1 {i} {n} 1\n2 {i} {n}\n' for i in range(1,h+1)),''.join(f'{i*(n-i+1)}\n' for i in range(1,h+1))
    if section==38:
        if slug.startswith('a_') or slug.startswith('b_'):
            array=' '.join(map(str,range(1,n+1))) if slug.startswith('a_') else '6 '*n
            ans=''.join(f'{i}\n' for i in range(1,q+1)) if slug.startswith('a_') else '6\n'*q
            return f'{n} {q}\n'+array+'\n'+''.join(f'{i} {n}\n' for i in range(1,q+1)),ans
        return f'{n} {q}\n'+' '.join(map(str,range(1,n)))+'\n'+''.join(f'{n} {i}\n' for i in range(q)),''.join(f'{n-i}\n' for i in range(q))
    if section==39:
        if slug.startswith('a_'):return f'{n}\n'+' '.join(map(str,range(1,n+1)))+'\n',' '.join(str((i+1)//2) for i in range(1,n+1))+'\n'
        if slug.startswith('b_'):return f'{n}\n'+''.join(f'{i} {n+1}\n' for i in range(n)),f'{n}\n'
        return f'{n} {n} {n}\n'+'0 '*n+'\n'+'0 '*n+'\n','0 '*n+'\n'
    if section==40:
        letter=slug.split('_')[0]
        if letter=='a':return f'{n} {q}\n'+'1 '*n+'\n'+'1 '*q+'\n',' '.join(map(str,range(1,n+1)))+'\n'
        if letter=='b':return f'{n}\n'+' '.join(map(str,range(1,n+1)))+'\n'+'1 '*n+'\n',' '.join(map(str,range(1,n+1)))+'\n'
        if letter=='e':
            return f'{n} {q}\n'+' '.join(map(str,range(2,n+1)))+' 1\n'+' '.join(map(str,range(1,n+1)))+'\n'+f'1 1000000000000000000\n'*q,'1 1\n'*q
        if letter=='g':return f'{n}\n'+''.join(f'{i} {n+1}\n' for i in range(n)),' '.join(map(str,range(1,n+1)))+'\n'
        if letter=='h':return f'{n} {q}\n'+''.join(f'T {i}\n' for i in range(1,h+1))+''.join(f'K {i}\n' for i in range(h,0,-1)),''.join(f'{i}\n' for i in range(h,0,-1))
        if letter=='i':return build(37,'b_maximum_subarray_updates')
        if letter=='j':
            # Consecutive increasing windows have translation-invariant cost.
            return f'{n} {h}\n'+' '.join(map(str,range(n)))+'\n',(str(h*h//4)+' ')*(n-h+1)+'\n'
        if letter=='k':return f'{n} {q}\n'+'0 '*n+'\n'+f'U {n} 1\nQ 1 0\n'*h,f'{n}\n'*h
        if letter=='l':return f'{n} {q}\n'+'0 '*n+'\n'+f'A 1 {n} -1\nQ 1 {n} 1\n'*h,'-1\n'*h
    if section==41:
        if slug.startswith('b_'):
            return f'{n} {q}\n'+''.join(f'{i-1} {i}\n' for i in range(2,n+1))+f'1 {n}\n'*q,f'{n}\n'*q
        parents=''.join(f'{i}\n' for i in range(1,n))
        if slug.startswith('a_'):return f'{n} {q}\n'+parents+''.join(f'{i} {n}\n' for i in range(1,q+1)),''.join(f'{n-i}\n' for i in range(1,q+1))
        return f'{n} {q}\n'+parents+''.join(f'{n} 1 {i}\n' for i in range(1,q+1)),''.join(f'{n-i+1}\n' for i in range(1,q+1))
    raise KeyError((section,slug))
