#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,q;if(!(cin>>n>>q))return 0;
vector<int> p(n),sz(n,1);iota(p.begin(),p.end(),0);
auto find=[&](int u){while(p[u]!=u){p[u]=p[p[u]];u=p[u];}return u;};
while(q--){char op;int u,v;cin>>op>>u>>v;u=find(u-1);v=find(v-1);
if(op=='A'){if(u!=v){if(sz[u]<sz[v])swap(u,v);p[v]=u;sz[u]+=sz[v];}}
else cout<<(u==v?"YES":"NO")<<'\n';}}
