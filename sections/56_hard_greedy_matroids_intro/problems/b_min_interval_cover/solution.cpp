#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T,n;if(!(cin>>T>>n))return 0;vector<pair<int,int>>s(n);for(auto&x:s)cin>>x.first>>x.second;sort(s.begin(),s.end());int i=0,cur=0,ans=0;while(cur<T){int best=cur;while(i<n&&s[i].first<=cur)best=max(best,s[i++].second);if(best==cur){cout<<-1<<'\n';return 0;}cur=best;ans++;}cout<<ans<<'\n';}
