#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,a,b,c;if(!(cin>>n>>a>>b>>c))return 0;vector<int> dp(n+1,-1e9);dp[0]=0;for(int x=1;x<=n;x++)for(int d:{a,b,c})if(d<=x)dp[x]=max(dp[x],dp[x-d]+1);cout<<(dp[n]<0?-1:dp[n])<<'\n';}
