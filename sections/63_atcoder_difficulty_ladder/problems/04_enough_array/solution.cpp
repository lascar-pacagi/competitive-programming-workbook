#include <bits/stdc++.h>
using namespace std;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;cin>>T;while(T--){int n;long long d,z;cin>>n>>d>>z;vector<pair<long long,long long>>a(n);for(auto&x:a)cin>>x.first>>x.second;sort(a.begin(),a.end());long long cur=0;for(auto[l,r]:a){if(cur+d-1<l)break;cur=max(cur,r+1);}cout<<(cur+d-1<=z?cur:-1)<<'\n';}}
