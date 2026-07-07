#include <bits/stdc++.h>
using namespace std; const long long MOD=1000000007; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;vector<int>q(T);int N=1;for(int&i:q){cin>>i;N=max(N,i);}vector<long long>d(N+1);d[0]=1;if(N>=1)d[1]=0;for(int i=2;i<=N;i++)d[i]=(i-1)*(d[i-1]+d[i-2])%MOD;for(int n:q)cout<<d[n]<<'\n';}
