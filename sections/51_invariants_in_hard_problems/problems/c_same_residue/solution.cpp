#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;long long k;if(!(cin>>n>>k))return 0;long long r;cin>>r;r%=k;for(int i=1;i<n;i++){long long x;cin>>x;if((x%k+k)%k!=(r+k)%k){cout<<"NO\n";return 0;}}cout<<"YES\n";}
