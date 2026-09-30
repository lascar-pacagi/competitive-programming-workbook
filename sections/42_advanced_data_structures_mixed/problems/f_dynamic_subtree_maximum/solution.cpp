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
    int size=1;while(size<n)size*=2;
    vector<ll> tree(2*size,LLONG_MIN);
    for(int i=0;i<n;++i)tree[size+i]=original[order[i]];
    for(int z=size-1;z;--z)tree[z]=max(tree[2*z],tree[2*z+1]);
    auto assign=[&](int i,ll x){int z=size+i;tree[z]=x;for(z/=2;z;z/=2)tree[z]=max(tree[2*z],tree[2*z+1]);};
    auto query=[&](int l,int r){ll answer=LLONG_MIN;l+=size;r+=size;
        while(l<r){if(l&1)answer=max(answer,tree[l++]);if(r&1)answer=max(answer,tree[--r]);l/=2;r/=2;}return answer;};
    while(q--){char op;int u;cin>>op>>u;--u;
        if(op=='Q')cout<<query(tin[u],tout[u])<<'\n';
        else{ll x;cin>>x;assign(tin[u],x);}}
}
