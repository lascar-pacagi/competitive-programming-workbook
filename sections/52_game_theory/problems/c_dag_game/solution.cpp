#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m,q;if(!(cin>>n>>m>>q))return 0;vector<vector<int>>g(n);while(m--){int a,b;cin>>a>>b;g[a-1].push_back(b-1);}vector<int>gr(n);for(int u=n-1;u>=0;u--){set<int>s;for(int v:g[u])s.insert(gr[v]);while(s.count(gr[u]))gr[u]++;}while(q--){int s;cin>>s;cout<<(gr[s-1]?"WIN":"LOSE")<<'\n';}}
