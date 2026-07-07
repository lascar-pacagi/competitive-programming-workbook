#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<long long>a(n);long long tot=0;for(auto&x:a){cin>>x;tot^=x;}long long pref=0,ans=0;for(int i=0;i+1<n;i++){pref^=a[i];if(pref==(tot^pref))ans++;}cout<<ans<<'\n';}
