#include <bits/stdc++.h>
using namespace std; struct Line{long long m,b; long long get(long long x){return m*x+b;}}; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int q;if(!(cin>>q))return 0;vector<Line>ls;while(q--){int t;cin>>t;if(t==1){long long m,b;cin>>m>>b;ls.push_back({m,b});}else{long long x;cin>>x;long long ans=4e18;for(auto &l:ls)ans=min(ans,l.get(x));cout<<ans<<'\n';}}}
