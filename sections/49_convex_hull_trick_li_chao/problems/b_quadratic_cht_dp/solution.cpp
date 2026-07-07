#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;long long c;if(!(cin>>n>>c))return 0;vector<long long>x(n),dp(n);for(auto&v:x)cin>>v;for(int i=1;i<n;i++){dp[i]=4e18;for(int j=0;j<i;j++)dp[i]=min(dp[i],dp[j]+(x[i]-x[j])*(x[i]-x[j])+c);}cout<<dp.back()<<'\n';}
