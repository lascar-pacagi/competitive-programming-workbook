#include <bits/stdc++.h>
using namespace std;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;cin>>n;vector<long long>a(n),dp(n);for(long long&x:a)cin>>x;for(int l=n-1;l>=0;--l){dp[l]=a[l];for(int r=l+1;r<n;++r)dp[r]=max(a[l]-dp[r],a[r]-dp[r-1]);}cout<<dp[n-1]<<'\n';}
