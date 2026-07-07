#include <bits/stdc++.h>
using namespace std; const long long MOD=1000000007; long long pw(long long a,long long e){long long r=1;while(e){if(e&1)r=r*a%MOD;a=a*a%MOD;e>>=1;}return r;}int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;while(T--){int n,k;cin>>n>>k;long long s=0;for(int r=0;r<n;r++)s=(s+pw(k,gcd(n,r)))%MOD;cout<<s*pw(n,MOD-2)%MOD<<'\n';}}
