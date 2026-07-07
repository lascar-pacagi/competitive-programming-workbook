#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<tuple<int,int,string>>v;for(int i=0;i<n;i++){string s;int a,b;cin>>s>>a>>b;v.push_back({-a,b,s});}sort(v.begin(),v.end());for(auto [a,b,s]:v)cout<<s<<'\n';}
