#include <bits/stdc++.h>
using namespace std;
using u64=uint64_t;
using u128=__uint128_t;
using i128=__int128_t;
u64 mul(u64 a,u64 b,u64 m) {
    return(u128)a*b%m;
}
u64 power(u64 a,u64 e,u64 m) {
    u64 r=1%m;
    for(;e;e>>=1,a=mul(a,a,m))if(e&1)r=mul(r,a,m);
    return r;
}
bool prime(u64 n) {
    if(n<2)return false;
    for(u64 p:{2,3,5,7,11,13,17,19,23,29,31,37})if(n%p==0)return n==p;
    u64 d=n-1,s=0;
    while(!(d&1))d>>=1,++s;
    for(u64 a:{2,325,9375,28178,450775,9780504,1795265022}) {
        if(a%n==0)continue;
        u64 x=power(a,d,n);
        if(x==1||x==n-1)continue;
        bool witness=true;
        for(u64 r=1;r<s;r++) {
            x=mul(x,x,n);
            if(x==n-1) {
                witness=false;
                break;
            }
        }
        if(witness)return false;
    }
    return true;
}
mt19937_64 rng(712367821);
u64 rho(u64 n) {
    if(n%2==0)return 2;
    if(n%3==0)return 3;
    while(true) {
        u64 c=rng()%(n-1)+1,x=rng()%n,y=x,d=1;
        while(d==1) {
            x=(u128(mul(x,x,n))+c)%n;
            y=(u128(mul(y,y,n))+c)%n;
            y=(u128(mul(y,y,n))+c)%n;
            d=gcd(x>y?x-y:y-x,n);
        }
        if(d!=n)return d;
    }
}
vector<u64> factor(u64 n) {
    vector<u64>out,st= {
        n
    }
    ;
    while(!st.empty()) {
        u64 x=st.back();
        st.pop_back();
        if(x==1)continue;
        if(prime(x))out.push_back(x);
        else {
            u64 d=rho(x);
            st.push_back(d);
            st.push_back(x/d);
        }
    }
    sort(out.begin(),out.end());
    return out;
}
vector<pair<u64,int>>groups(u64 n) {
    vector<pair<u64,int>>g;
    for(u64 p:factor(n))if(!g.empty()&&g.back().first==p)g.back().second++;
    else g.push_back({p,1});
    return g;
}
u64 phi(u64 n) {
    u64 r=n;
    for(auto[p,e]:groups(n))r=r/p*(p-1);
    return r;
}
u64 lcm64(u64 a,u64 b) {
    return a/gcd(a,b)*b;
}
u64 lambda(u64 n) {
    u64 r=1;
    for(auto[p,e]:groups(n)) {
        u64 z;
        if(p==2&&e>=3)z=1ULL<<(e-2);
        else {
            z=p-1;
            for(int i=1;i<e;i++)z*=p;
        }
        r=lcm64(r,z);
    }
    return r;
}
u64 primitive(u64 p) {
    if(p==2)return 1;
    vector<u64>q;
    for(auto[x,e]:groups(p-1))q.push_back(x);
    for(u64 g=2;;g++) {
        bool ok=true;
        for(u64 x:q)if(power(g,(p-1)/x,p)==1) {
            ok=false;
            break;
        }
        if(ok)return g;
    }
}
long long invmod(long long a,long long m) {
    long long b=m;
    i128 x=1,y=0;
    while(b) {
        long long q=a/b,t=a%b;
        a=b;
        b=t;
        i128 z=x-(i128)q*y;
        x=y;
        y=z;
    }
    x%=m;
    if(x<0)x+=m;
    return(long long)x;
}
optional<u64>bsgs(u64 a,u64 b,u64 m) {
    if(m==1)return 0;
    u64 z=sqrtl((long double)m)+1;
    while((u128)z*z<m)z++;
    unordered_map<u64,u64>baby;
    u64 value=1;
    for(u64 j=0;j<z;j++) {
        if(!baby.count(value))baby[value]=j;
        value=mul(value,a,m);
    }
    u64 step=invmod(power(a,z,m),m);
    value=b;
    optional<u64>best;
    for(u64 i=0;i<=z;i++) {
        auto it=baby.find(value);
        if(it!=baby.end()) {
            u64 candidate=i*z+it->second;
            if(!best||candidate<*best)best=candidate;
        }
        value=mul(value,step,m);
    }
    return best;
}
optional<u64>dlog(u64 a,u64 b,u64 m) {
    a%=m;
    b%=m;
    if(b==1%m)return 0;
    u64 added=0,scale=1;
    while(true) {
        u64 g=gcd(a,m);
        if(g==1)break;
        if(b%g)return {
        }
        ;
        m/=g;
        b/=g;
        scale=mul(scale,a/g,m);
        added++;
        if(scale==b)return added;
        if(m==1)return added;
    }
    u64 target=mul(b,invmod(scale,m),m);
    auto tail=bsgs(a%m,target,m);
    if(!tail)return {
    }
    ;
    return added+*tail;
}
optional<u64>tonelli(u64 a,u64 p) {
    a%=p;
    if(a==0)return 0;
    if(power(a,(p-1)/2,p)!=1)return {
    }
    ;
    if(p%4==3)return power(a,(p+1)/4,p);
    u64 q=p-1,s=0;
    while(!(q&1))q>>=1,++s;
    u64 z=2;
    while(power(z,(p-1)/2,p)!=p-1)z++;
    u64 c=power(z,q,p),x=power(a,(q+1)/2,p),t=power(a,q,p),m=s;
    while(t!=1) {
        u64 i=1,v=mul(t,t,p);
        while(v!=1)v=mul(v,v,p),i++;
        u64 h=power(c,1ULL<<(m-i-1),p);
        x=mul(x,h,p);
        t=mul(t,mul(h,h,p),p);
        c=mul(h,h,p);
        m=i;
    }
    return x;
}
u64 order(u64 a,u64 n) {
    u64 r=lambda(n);
    for(auto[p,e]:groups(r))while(r%p==0&&power(a,r/p,n)==1)r/=p;
    return r;
}
optional<u64>linear(u64 a,u64 b,u64 m) {
    u64 g=gcd(a,m);
    if(b%g)return {
    }
    ;
    u64 mod=m/g;
    if(mod==1)return 0;
    return mul((b/g)%mod,invmod((a/g)%mod,mod),mod);
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int q;
    cin>>q;
    while(q--) {
        u64 p,a;
        cin>>p>>a;
        auto x=tonelli(a,p);
        if(!x) {
            cout<<"NONE\n";
            continue;
        }
        u64 y=(p-*x)%p;
        if(*x==y)cout<<*x<<'\n';
        else cout<<min(*x,y)<<' '<<max(*x,y)<<'\n';
    }
}
