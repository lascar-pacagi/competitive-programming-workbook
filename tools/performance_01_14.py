"""Full-bound constructions for early-course exercises; answers are identities."""
N=200_000


def arr(header, values, answer):
    return '1\n'+header+'\n'+' '.join(map(str,values))+'\n',str(answer)+'\n'


def build(section, slug):
    n=N;h=N//2
    if section==1:
        if slug.startswith('a_'):return arr(str(n),[10**9]*n,n*10**9)
        if slug.startswith('b_'):return '200000\n'+'1 1000000000000000000\n'*n,'59\n'*n
        if slug.startswith('c_'):return f'{n}\n'+'1000000000 1000000000000000000\n'*n,'quadratic\n'*n
        return f'{n}\n'+'1000000000000000000 3\n'*n,'333333333333333334 2\n'*n
    if section==2:
        if slug.startswith('a_'):return '1\n'+'R'*n+'\n',f'{n} 0 {n}\n'
        if slug.startswith('b_'):return '100\n'+'300 100000 1 1 1\n'*100,'-1\n'*100
        return arr('20 1048575',[1<<i for i in range(20)],1048575)
    if section==3:
        if slug.startswith('a_'):return f'1\n{h} {h}\n'+' '.join(map(str,range(h)))+'\n'+'\n'.join(map(str,range(h)))+'\n','1\n'*h
        if slug.startswith('b_'):return arr(str(n),range(n,0,-1),'1 1')
        if slug.startswith('c_'):return arr(f'{n} 2',[1]*n,n*(n-1)//2)
        return arr(str(n),[0]*n,n*(n-1)//2)
    if section==4:
        if slug.startswith('a_'):
            return f'1\n{h} {h}\n'+'1 '*h+'\n'+''.join(f'{i} {h}\n' for i in range(1,h+1)),''.join(f'{h-i+1}\n' for i in range(1,h+1))
        if slug.startswith('b_'):return f'1\n{h} {h}\n'+f'1 {h} 1\n'*h,' '.join([str(h)]*h)+'\n'
        return arr(f'{n} 0',[0]*n,n*(n+1)//2)
    if section==5:
        if slug.startswith('a_'):return arr(str(n),range(n,0,-1),1)
        if slug.startswith('b_'):
            # Base-26 names have equal length and give an independently known order.
            def name(i):
                s=''
                for _ in range(4):s=chr(97+i%26)+s;i//=26
                return s
            return '1\n'+str(n)+'\n'+''.join(f'{name(i)} 1 1\n' for i in range(n-1,-1,-1)),' '.join(name(i) for i in range(n))+'\n'
        return '1\n'+str(n)+'\n'+''.join(f'{i} {i}\n' for i in range(n,0,-1)),f'1\n1 {n}\n'
    if section==6:
        if slug.startswith('a_'):return arr(f'{n} -1',range(n),'NO')
        if slug.startswith('b_'):return arr(f'{n} {h}',[1]*n,h)
        return arr(f'{n} {n}',[0]*n,n*(n+1)//2)
    if section==7:
        if slug.startswith('a_'):return arr(f'{n} {h}',range(n),h)
        if slug.startswith('b_'):return f'1\n{h} {h}\n'+f'1 {h} 1\n'*h,f'{h} 1\n'
        if slug.startswith('c_'):return arr(f'{n} {h}',[1]*n,f'{h} 1')
        return f'1\n{h} 1 '+'R'*h+'\n',f'1 {h}\n'
    if section==8:
        if slug.startswith('a_'):return f'{n}\n'+'999999999999999999\n'*n,'1000000000\n'*n
        if slug.startswith('b_'):return arr(f'{n} {h}',range(n),2)
        return arr(f'{n} 2',[1]*n,h)
    if section==9:
        if slug.startswith('a_'):return '1\n'+str(n)+'\n'+''.join(f'{i} {i+1}\n' for i in range(n-1,-1,-1)),f'{n}\n'
        if slug.startswith('b_'):return arr(f'{n} 2',[1]*n,h)
        return f'1\n{n}\n'+'1 100000\n'*n,f'{h}\n'
    if section==10:
        if slug.startswith('a_'):return arr(str(n),range(n,0,-1),n*(n-1)//2)
        if slug.startswith('b_'):return '1\n'+'?'*n+'\n','('*h+')'*h+'\n'
        return f'1\n{n} 1000000000 {n*10**9}\n',' '.join(['1000000000']*n)+'\n'
    if section==11:
        if slug.startswith('a_'):return f'1\n{n}\n'+f'0 {n}\n'*n,f'{n}\n'
        if slug.startswith('b_'):return f'1\n{n}\n'+''.join(f'{i} {i+1}\n' for i in range(n-1,-1,-1)),f'{n}\n'
        return f'1\n{h} {h}\n'+f'0 {h}\n'*h+' '.join(map(str,range(h)))+'\n',' '.join([str(h)]*h)+'\n'
    if section==12:
        if slug.startswith('a_'):return arr(str(n),range(n,0,-1),' '.join(['-1']*n))
        if slug.startswith('b_'):return arr(f'{n} {h}',range(n),' '.join(map(str,range(h-1,n))))
        return arr(f'{n} {n+1}',[1]*n,-1)
    if section==13:
        if slug.startswith('a_'):return arr(str(n),range(n-1,-1,-1),' '.join(map(str,range(n-1,-1,-1))))
        if slug.startswith('b_'):
            return f'1\n{h} {h}\n'+' '.join(map(str,range(h)))+'\n'+f'1 {h} {h}\n'*h,f'{h}\n'*h
        return f'1\n{h} {h}\n'+' '.join(map(str,range(h)))+'\n'+''.join(f'{i} {h}\n' for i in range(1,h+1)),''.join(f'{h-i+1}\n' for i in range(1,h+1))
    if section==14:
        if slug.startswith('a_'):return arr(f'{n} {n}',range(1,n+1),n)
        if slug.startswith('b_'):return arr(f'{n} 2',[1]*n,h)
        if slug.startswith('c_'):
            return f'1\n{h} {h}\n'+''.join(f'0 {h+1} {i}\n' for i in range(1,h+1))+' '.join(map(str,range(h)))+'\n',' '.join([str(h)]*h)+'\n'
        if slug.startswith('e_'):return '1\n'+('zyxwvutsrqponmlkjihgfedcba'*(n//26+1))[:n]+'\n','abcdefghijklmnopqrstuvwxyz\n'
    raise KeyError((section,slug))
