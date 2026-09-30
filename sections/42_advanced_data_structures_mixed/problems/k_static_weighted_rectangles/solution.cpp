#include <bits/stdc++.h>
using namespace std;using ll=long long;
struct BIT{vector<ll>b;BIT(int n):b(n+1){}void add(int i,ll x){for(;i<(int)b.size();i+=i&-i)b[i]+=x;}ll sum(int i){ll s=0;for(;i;i-=i&-i)s+=b[i];return s;}};
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,q;if(!(cin>>n>>q))return 0;
vector<tuple<ll,ll,ll>> points;vector<ll> ys;
for(int i=0;i<n;++i){ll x,y,w;cin>>x>>y>>w;points.emplace_back(x,y,w);ys.push_back(y);}
vector<tuple<ll,ll,ll,int,int>> events;vector<ll> ans(q);
for(int i=0;i<q;++i){ll a,b,c,d;cin>>a>>b>>c>>d;events.emplace_back(c,b,d,i,1);events.emplace_back(a-1,b,d,i,-1);}
sort(points.begin(),points.end());sort(events.begin(),events.end());sort(ys.begin(),ys.end());ys.erase(unique(ys.begin(),ys.end()),ys.end());BIT bit(ys.size());int p=0;
for(auto [x,lo,hi,id,sign]:events){while(p<n&&get<0>(points[p])<=x){auto [px,y,w]=points[p++];bit.add(lower_bound(ys.begin(),ys.end(),y)-ys.begin()+1,w);}
int l=lower_bound(ys.begin(),ys.end(),lo)-ys.begin(),r=upper_bound(ys.begin(),ys.end(),hi)-ys.begin();ans[id]+=sign*(bit.sum(r)-bit.sum(l));}
for(ll x:ans)cout<<x<<'\n';}
