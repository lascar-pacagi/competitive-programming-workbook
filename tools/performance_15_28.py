"""Graph and DP scale cases with path, counting, and symmetry oracles."""
import math
N=200_000
MOD=1_000_000_007


def chain(n=N, weight=None, reverse=False):
    return ''.join(f'{i+1 if reverse else i} {i if reverse else i+1}'+('' if weight is None else f' {weight}')+'\n' for i in range(1,n))


def matrix(n, x):
    return ((' '.join([str(x)]*n)+'\n')*n)


def build(section,slug):
    n=N;q=N
    if section==15:
        if slug.startswith('a_'):return f'1\n{n} {n-1}\n'+chain(),f'1\n{n}\n'
        if slug.startswith('b_'):return f'{n} {n-1} 1 {q}\n'+chain()+' '.join(map(str,range(n,0,-1)))+'\n',' '.join(map(str,range(n-1,-1,-1)))+'\n'
        return '1000 1000\n'+'S'+'.'*999+'\n'+('.'*1000+'\n')*998+'.'*999+'G\n','YES\n1998\n'+'D'*999+'R'*999+'\n'
    if section==16:
        if slug.startswith('a_'):return f'{n}\n'+chain(),' '.join(map(str,range(n,0,-1)))+'\n'
        return f'{n} {n-1}\n'+chain(),'ACYCLIC\n'
    if section==17:
        if slug.startswith('a_'):
            # A wide frontier exposes repeatedly sorting/scanning available vertices.
            return f'{n} 0\n',' '.join(map(str,range(1,n+1)))+'\n'
        if slug.startswith('b_'):return f'{n} {n-1}\n'+chain(),f'{n-1}\n'
        return f'{n} {n-1}\n'+'1000000000 '*n+'\n'+chain(),' '.join(str(i*10**9) for i in range(1,n+1))+'\n'
    if section==18:
        if slug.startswith('a_'):return f'{n} {n}\n'+chain(reverse=True)+f'{n} 1\n',''.join(f'{n-i} {i+1}\n' for i in range(1,n))+f'1 {n}\n'
        if slug.startswith('b_'):return f'{n} {n-1}\n'+chain(weight=10**9),f'{(n-1)*10**9}\n'
        return f'{n} {n-1} {n//2}\n'+chain(weight=1),f'{n//2}\n'
    if section==19:
        if slug.startswith('a_'):return f'{n} {n-1} 1 {q}\n'+chain(weight=10**9)+' '.join(map(str,range(1,n+1)))+'\n',' '.join(str(i*10**9) for i in range(n))+'\n'
        if slug.startswith('b_'):return '1000 1000\n'+matrix(1000,1),'1999\n'
        return f'{n} {n-1}\n'+chain(weight=2),f'{2*(n-1)-1}\n'
    if section==20:
        if slug.startswith('a_'):return f'{n} {n-1} 1 {q}\n'+chain(weight=1)+' '.join(map(str,range(1,n+1)))+'\n',' '.join(map(str,range(n)))+'\n'
        if slug.startswith('b_'):return '1000 1000\n'+('R'*1000+'\n')*1000,'999\n'
        # Open square makes walking sufficient but exercises all warp-neighbor scans.
        return '1000 1000\n'+'S'+'.'*999+'\n'+('.'*1000+'\n')*998+'.'*999+'G\n','0\n'
    if section==21:
        if slug.startswith('a_'):return f'{n} 0 {n-1}\n'+chain(weight=1),f'{n-1}\n'
        if slug.startswith('b_'):return f'{n} {n-1} {q}\n'+'1000000000 '*n+'\n'+chain()+' '.join(map(str,range(1,n+1)))+'\n',' '.join(str(i*10**9) for i in range(1,n+1))+'\n'
        if slug.startswith('c_'):return f'{n} {n-1}\n'+chain(reverse=True),f'{n-1}\n'
        if slug.startswith('e_'):return f'{n} {n-1} 1\n'+chain()+'1\n',f'0 {n} {n-1}\n'
        if slug.startswith('f_'):return f'{n} {n-2}\n'+chain(n-1),f'2 1 {n-1}\n'
        return f'{n} {n-1}\n'+''.join(f'{i} {i+1} 1 '+('R' if i%2 else 'B')+'\n' for i in range(1,n)),f'{n-1}\n'
    if section==22:
        if slug.startswith('a_'):
            # With every odd step broken there is exactly one route: only +2 moves.
            return f'{n} {n//2}\n'+' '.join(map(str,range(1,n,2)))+'\n','1\n'
        if slug.startswith('b_'):return f'{n}\n'+'1000000000 '*n+'\n',f'{(n//2)*10**9}\n'
        if slug.startswith('c_'):return f'{n} 50\n'+' '.join(map(str,range(n)))+'\n',f'{n-1}\n'
        # Includes a full target and full denomination count. Unit denomination
        # plus 19 equal target-sized coins yields an exact optimum of one coin.
        return f'{n} 20\n1 '+' '.join([str(n)]*19)+'\n','1\n'
    if section==23:
        if slug.startswith('a_'):return '200 10000\n'+'1 1000000000\n'*200,f'{200*10**9}\n'
        if slug.startswith('b_'):return '200 10000\n'+'1 1000000000\n'*200,f'{10000*10**9}\n'
        if slug.startswith('c_'):return '100\n'+'1000 '*100+'\n','100\n'+' '.join(str(1000*i) for i in range(1,101))+'\n'
        return '200\n'+'500 '*200+'\n','0\n'
    if section==24:
        if slug.startswith('a_'):return '1000 1000\n'+('.'*1000+'\n')*1000,str(math.comb(1998,999)%MOD)+'\n'
        if slug.startswith('b_'):return '1000 1000\n'+matrix(1000,10**9),str(1999*10**9)+'\n'
        if slug.startswith('c_'):
            # A path with t turns has t+1 alternating positive runs. Splitting
            # the 79 horizontal/vertical steps into runs gives binomial factors.
            total=0
            for turns in range(1,41):
                runs=turns+1;a=(runs+1)//2;b=runs//2
                total+=2*math.comb(78,a-1)*math.comb(78,b-1)
            return '80 80 40\n'+('.'*80+'\n')*80,str(total%MOD)+'\n'
        return '70 70\n'+matrix(70,1),str(2*(70+70-1)-2)+'\n'
    if section==25:
        if slug.startswith('a_'):
            n=200;k=(n-1).bit_length()
            return f'{n}\n'+'1 '*n+'\n',str(n*k-((1<<k)-n))+'\n'
        if slug.startswith('b_'):return 'a'*500+'b'*500+'\n','500\n'
        if slug.startswith('c_'):return '200\n'+'1000 '*200+'\n',str(198*1000**3+1000**2+1000)+'\n'
        return '3000\n'+'1000000000 '*3000+'\n','0\n'
    if section==26:
        if slug.startswith('a_'):return f'{n}\n'+'1000000000 '*n+'\n'+chain(),str((n//2)*10**9)+'\n'
        if slug.startswith('b_'):return f'{n}\n'+chain(),str(n//2)+'\n'
        # Independent-set colorings of a path count as Fibonacci(n+2).
        a,b=0,1
        for _ in range(n+2):a,b=b,(a+b)%MOD
        return f'{n}\n'+chain(),str(a)+'\n'
    if section==27:
        if slug.startswith('a_'):
            text='20 30\n'+''.join(f'1 1 {i}\n' for i in range(1,21))+''.join(f'3 2 {i} {i+1}\n' for i in range(1,20,2))
            return text,'20\n'
        if slug.startswith('b_'):return '18\n'+matrix(18,10**9),str(18*10**9)+'\n'
        if slug.startswith('c_'):
            return '16\n'+''.join(' '.join('0' if i==j else '1' for j in range(16))+'\n' for i in range(16)),'16\n'
        return '20 0\n'+'1000000000 '*20+'\n',str(20*10**9)+'\n'
    if section==28:
        if slug.startswith('a_'):return f'{n}\n'+'3 '*n+'\n','0\n'
        if slug.startswith('b_'):return '60 200 200\n'+'1 1000000000\n'*60,str(60*10**9)+'\n'
        if slug.startswith('c_'):return '80 300\n'+'1 1000000000\n'*80+' '.join(str(i//2) for i in range(2,81))+'\n',str(80*10**9)+'\n'
        if slug.startswith('e_'):return '500 500\n'+matrix(500,1),'998\n'
        if slug.startswith('f_'):return '500\n'+'10000 '*501+'\n',str(499*10**12)+'\n'
        if slug.startswith('g_'):return '18\n'+''.join(' '.join('-1' if i==j else '1' for j in range(18))+'\n' for i in range(18)),'17\n'
        if slug.startswith('i_'):return '200 5000\n'+('10 '+'1 1000000000 '*10+'\n')*200,str(200*10**9)+'\n'
        if slug.startswith('k_'):return '300\n'+'1000 '*300+'\n',str(298*1000**3+1000**2+1000)+'\n'
    raise KeyError((section,slug))


def extra_cases(section,slug):
    if section==20 and slug=='c_warp_maze':
        rows=['S'+'.'*999]+['.'*1000 for _ in range(999)]
        for r in range(997,1000):rows[r]='#'*3+'.'*997
        rows[999]='G'+rows[999][1:]
        # Every other cell within warp distance two of G is blocked. Search
        # must exhaust the million-cell reachable region to prove failure.
        return [('isolated_goal', '1000 1000\n'+'\n'.join(rows)+'\n','-1\n')]
    return []
