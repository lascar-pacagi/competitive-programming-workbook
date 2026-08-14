#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<pair<long long,long long>> a(n);for(auto& x:a)cin>>x.first>>x.second;sort(a.begin(),a.end(),[](auto x,auto y){return x.second<y.second;});long long available=-1;int answer=0;for(auto [start,end]:a)if(start>=available){++answer;available=end;}cout<<answer<<'\n';}
