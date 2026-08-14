#include <bits/stdc++.h>
using namespace std; using ll=long long; const ll MOD=1000000007;
pair<ll,ll> fib(unsigned long long n){
    if (!n) return {0, 1};
    auto [a, b] = fib(n / 2);
    ll c=a*((2*b%MOD-a+MOD)%MOD)%MOD, d=(a*a%MOD+b*b%MOD)%MOD;
    return n&1?make_pair(d,(c+d)%MOD):make_pair(c,d);
}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;cin>>q;while(q--){unsigned long long l,r;cin>>l>>r;cout<<(fib(r+2).first-fib(l+1).first+MOD)%MOD<<'\n';}}
