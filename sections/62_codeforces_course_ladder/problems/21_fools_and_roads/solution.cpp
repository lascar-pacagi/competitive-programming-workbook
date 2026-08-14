#include <bits/stdc++.h>
using namespace std;
struct DSU{vector<int>p,s;DSU(int n):p(n+1),s(n+1,1){iota(p.begin(),p.end(),0);}int find(int x){return p[x]==x?x:p[x]=find(p[x]);}bool unite(int a,int b){a=find(a);b=find(b);if(a==b)return false;if(s[a]<s[b])swap(a,b);p[b]=a;s[a]+=s[b];return true;}};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,m;cin>>n>>m;vector<tuple<long long,int,int>>e;for(int i=0,u,v;i<m;i++){long long w;cin>>u>>v>>w;e.emplace_back(w,u,v);}if(n==1){cout<<0<<'\n';return 0;}sort(e.begin(),e.end());DSU d(n);for(auto [w,u,v]:e){d.unite(u,v);if(d.find(1)==d.find(n)){cout<<w<<'\n';return 0;}}cout<<-1<<'\n';}
