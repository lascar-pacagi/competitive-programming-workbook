#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;if(!(cin>>n>>m))return 0;vector<int>a(m);for(int&x:a)cin>>x;vector<int>w(n+1);for(int i=1;i<=n;i++)for(int x:a)if(i>=x&&!w[i-x])w[i]=1;cout<<(w[n]?"WIN":"LOSE")<<'\n';}
