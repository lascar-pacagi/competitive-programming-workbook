#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;while(T--){int n;cin>>n;long long x=0,v;while(n--){cin>>v;x^=v;}cout<<(x?"WIN":"LOSE")<<'\n';}}
