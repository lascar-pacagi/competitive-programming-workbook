#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int n, q;
vector<ll> sm, addv, asgv;
vector<char> hasa;

static void put_assign(int x, int len, ll v) {
    sm[x] = v * len; asgv[x] = v; hasa[x] = 1; addv[x] = 0;
}
static void put_add(int x, int len, ll v) {
    sm[x] += v * len;
    if (hasa[x]) asgv[x] += v; else addv[x] += v;
}
static void push(int x, int l, int r) {
    int m = (l + r) / 2, lc = 2 * x, rc = 2 * x + 1;
    if (hasa[x]) {
        put_assign(lc, m - l + 1, asgv[x]);
        put_assign(rc, r - m, asgv[x]);
        hasa[x] = 0; asgv[x] = 0;
    }
    if (addv[x]) {
        put_add(lc, m - l + 1, addv[x]);
        put_add(rc, r - m, addv[x]);
        addv[x] = 0;
    }
}
static void build(int x, int l, int r, vector<ll> &a) {
    if (l == r) { sm[x] = a[l]; return; }
    int m = (l + r) / 2;
    build(2 * x, l, m, a); build(2 * x + 1, m + 1, r, a);
    sm[x] = sm[2 * x] + sm[2 * x + 1];
}
static void upd(int x, int l, int r, int ql, int qr,
                ll v, bool assign_) {
    if (qr < l || r < ql) return;
    if (ql <= l && r <= qr) {
        if (assign_) put_assign(x, r - l + 1, v);
        else put_add(x, r - l + 1, v);
        return;
    }
    push(x, l, r);
    int m = (l + r) / 2;
    upd(2 * x, l, m, ql, qr, v, assign_);
    upd(2 * x + 1, m + 1, r, ql, qr, v, assign_);
    sm[x] = sm[2 * x] + sm[2 * x + 1];
}
static ll qry(int x, int l, int r, int ql, int qr) {
    if (qr < l || r < ql) return 0;
    if (ql <= l && r <= qr) return sm[x];
    push(x, l, r);
    int m = (l + r) / 2;
    return qry(2 * x, l, m, ql, qr) + qry(2 * x + 1, m + 1, r, ql, qr);
}

int main() {
    ios::sync_with_stdio(false); cin.tie(nullptr);
    if (!(cin >> n >> q)) return 0;
    vector<ll> original(n); for(auto &x:original) cin>>x;
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
    vector<ll> a(n+1); for(int i=0;i<n;++i) a[i+1]=original[order[i]];
    sm.assign(4 * n + 4, 0); addv.assign(4 * n + 4, 0);
    asgv.assign(4 * n + 4, 0); hasa.assign(4 * n + 4, 0);
    build(1, 1, n, a);
    string out;
    while (q--) {
        int t,u; ll x; cin>>t>>u; --u;
        int l=tin[u]+1,r=tout[u];
        if(t==3) out+=to_string(qry(1,1,n,l,r))+"\n";
        else {cin>>x;upd(1,1,n,l,r,x,t==1);}
    }
    cout << out;
}
