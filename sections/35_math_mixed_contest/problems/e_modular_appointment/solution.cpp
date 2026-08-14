#include <bits/stdc++.h>
using namespace std;using ll=long long;
ll eg(ll a,ll b,ll&x,ll&y){if(!b){x=1;y=0;return a;}ll x1,y1,g=eg(b,a%b,x1,y1);x=y1;y=x1-a/b*y1;return g;}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;cin>>q;while(q--){ll a,b,c,m;cin>>a>>b>>c>>m;ll target=(b-c)%m;if(target<0)target+=m;ll x,y,g=eg(a,m,x,y);if(target%g){cout<<-1<<'\n';continue;}ll mod=m/g;__int128 value=(__int128)(target/g)*x;ll ans=(ll)(value%mod);if(ans<0)ans+=mod;cout<<ans<<'\n';}}
