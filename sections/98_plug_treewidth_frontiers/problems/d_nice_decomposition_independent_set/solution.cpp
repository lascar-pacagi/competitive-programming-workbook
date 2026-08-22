#include <bits/stdc++.h>
using namespace std;
using ll=long long;
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n,m;
    cin>>n>>m;
    vector<ll>w(n);
    for(ll&x:w)cin>>x;
    vector<unsigned long long>adj(n);
    while(m--) {
        int u,v;
        cin>>u>>v;
        --u;
        --v;
        adj[u]|=1ULL<<v;
        adj[v]|=1ULL<<u;
    }
    int t;
    cin>>t;
    vector<unsigned long long>bag(t);
    vector<map<unsigned long long,ll>>dp(t);
    for(int i=0;i<t;i++) {
        char type;
        cin>>type;
        if(type=='L')dp[i][0]=0;
        else if(type=='I') {
            int child,v;
            cin>>child>>v;
            --child;
            --v;
            bag[i]=bag[child]|1ULL<<v;
            dp[i]=dp[child];
            for(auto[mask,val]:dp[child])if(!(mask&adj[v])) {
                auto nextmask=mask|1ULL<<v;
                ll candidate=val+w[v];
                if(!dp[i].count(nextmask)||candidate>dp[i][nextmask])dp[i][nextmask]=candidate;
            }
        }
        else if(type=='F') {
            int child,v;
            cin>>child>>v;
            --child;
            --v;
            bag[i]=bag[child]&~(1ULL<<v);
            for(auto[mask,val]:dp[child]) {
                auto nextmask=mask&~(1ULL<<v);
                if(!dp[i].count(nextmask)||val>dp[i][nextmask])dp[i][nextmask]=val;
            }
        }
        else {
            int a,b;
            cin>>a>>b;
            --a;
            --b;
            bag[i]=bag[a];
            for(auto[mask,val]:dp[a])if(dp[b].count(mask)) {
                ll duplicate=0;
                for(int v=0;v<n;v++)if(mask>>v&1)duplicate+=w[v];
                dp[i][mask]=val+dp[b][mask]-duplicate;
            }
        }
    }
    cout<<dp.back()[0]<<'\n';
}
