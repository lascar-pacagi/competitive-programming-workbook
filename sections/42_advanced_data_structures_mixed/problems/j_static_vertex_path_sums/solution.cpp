#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    int n,q; if (!(cin>>n>>q)) return 0;
    vector<ll> original(n); for (auto &x:original) cin>>x;
    vector<vector<int>> g(n);
    for (int i=1,u,v; i<n; ++i) {cin>>u>>v; --u; --v; g[u].push_back(v); g[v].push_back(u);}
    vector<int> tin(n),tout(n),order;
    vector<tuple<int,int,bool>> stack{{0,-1,false}};
    while (!stack.empty()) {
        auto [u,p,leaving]=stack.back(); stack.pop_back();
        if (leaving) {tout[u]=order.size(); continue;}
        tin[u]=order.size(); order.push_back(u); stack.emplace_back(u,p,true);
        for (auto it=g[u].rbegin();it!=g[u].rend();++it)
            if (*it!=p) stack.emplace_back(*it,u,false);
    }
    vector<int> parent(n),depth(n);vector<ll> sums(n);sums[0]=original[0];
    for(int u:order)for(int v:g[u])if(v!=parent[u]){parent[v]=u;depth[v]=depth[u]+1;sums[v]=sums[u]+original[v];}
    int levels=1;while((1<<levels)<=n)++levels;
    vector<vector<int>> up(levels,parent);
    for(int k=1;k<levels;++k)for(int u=0;u<n;++u)up[k][u]=up[k-1][up[k-1][u]];
    auto lca=[&](int u,int v){
        if(depth[u]<depth[v])swap(u,v);int diff=depth[u]-depth[v];
        for(int k=0;k<levels;++k)if(diff>>k&1)u=up[k][u];
        if(u==v)return u;
        for(int k=levels-1;k>=0;--k)if(up[k][u]!=up[k][v]){u=up[k][u];v=up[k][v];}
        return parent[u];
    };
    while(q--){int u,v;cin>>u>>v;--u;--v;int w=lca(u,v);cout<<sums[u]+sums[v]-2*sums[w]+original[w]<<'\n';}
}
