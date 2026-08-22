#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);
 int n,m,q;if(!(cin>>n>>m>>q))return 0; vector<bitset<700>> r(n);
 for(int i=0,u,v;i<m;i++){long long l,h,f;cin>>u>>v>>l>>h>>f;--u;--v;if(f<h)r[u].set(v);if(f>l)r[v].set(u);}
 for(int i=0;i<n;i++)r[i].set(i);
 for(int k=0;k<n;k++)for(int i=0;i<n;i++)if(r[i].test(k))r[i]|=r[k];
 while(q--){int u,v;cin>>u>>v;--u;--v;cout<<(r[v].test(u)?"YES\n":"NO\n");}
}
