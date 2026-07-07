#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<long long>a(n);for(auto&x:a)cin>>x;for(long long x:a)if((x-a[0])%2){cout<<"NO\n";return 0;}cout<<"YES\n";}
