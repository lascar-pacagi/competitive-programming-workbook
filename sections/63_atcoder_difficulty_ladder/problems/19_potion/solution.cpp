#include <bits/stdc++.h>
using namespace std;const long long MOD=1000000007LL;long long power(long long a,long long b,long long m){long long r=1%m;for(a%=m;b;b>>=1,a=a*a%m)if(b&1)r=r*a%m;return r;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;cin>>q;while(q--){long long a,b,c;cin>>a>>b>>c;cout<<power(a,power(b,c,MOD-1),MOD)<<'\n';}}
