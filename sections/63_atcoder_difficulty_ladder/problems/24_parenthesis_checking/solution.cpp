#include <bits/stdc++.h>
using namespace std;
const long long MOD=1000000007LL;
long long mod_pow(long long a,long long e){long long r=1;for(;e;e>>=1,a=a*a%MOD)if(e&1)r=r*a%MOD;return r;}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;long long sum=0,answer=0;while(n--){long long p,q;cin>>p>>q;long long chance=p%MOD*mod_pow(q,MOD-2)%MOD;answer=(answer+sum*chance)%MOD;sum=(sum+chance)%MOD;}cout<<answer<<'\n';}
