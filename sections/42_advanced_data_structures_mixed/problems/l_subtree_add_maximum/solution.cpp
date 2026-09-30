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
    vector<ll> mx(4*n),lazy(4*n);
    function<void(int,int,int)> build=[&](int z,int l,int r) {
        if(r-l==1){mx[z]=original[order[l]];return;}
        int m=(l+r)/2;build(z*2,l,m);build(z*2+1,m,r);mx[z]=max(mx[z*2],mx[z*2+1]);
    };
    auto apply=[&](int z,ll x){mx[z]+=x;lazy[z]+=x;};
    auto push=[&](int z){if(lazy[z]){apply(z*2,lazy[z]);apply(z*2+1,lazy[z]);lazy[z]=0;}};
    function<void(int,int,int,int,int,ll,bool)> update=[&](int z,int l,int r,int a,int b,ll x,bool assign) {
        if(b<=l||r<=a)return;
        if(a<=l&&r<=b){if(assign){mx[z]=x;lazy[z]=0;}else apply(z,x);return;}
        push(z);int m=(l+r)/2;update(z*2,l,m,a,b,x,assign);update(z*2+1,m,r,a,b,x,assign);mx[z]=max(mx[z*2],mx[z*2+1]);
    };
    function<ll(int,int,int,int,int)> query=[&](int z,int l,int r,int a,int b)->ll {
        if(b<=l||r<=a)return LLONG_MIN;
        if(a<=l&&r<=b)return mx[z];
        push(z);int m=(l+r)/2;return max(query(z*2,l,m,a,b),query(z*2+1,m,r,a,b));
    };
    build(1,0,n);
    while(q--){char op;int u;cin>>op>>u;--u;if(op=='Q')cout<<query(1,0,n,tin[u],tout[u])<<'\n';
        else{ll x;cin>>x;update(1,0,n,tin[u],tout[u],x,false);}}
}
