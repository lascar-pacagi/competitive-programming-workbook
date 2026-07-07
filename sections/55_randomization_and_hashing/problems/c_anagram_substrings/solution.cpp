#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s))return 0;int q;cin>>q;while(q--){int l1,r1,l2,r2;cin>>l1>>r1>>l2>>r2;array<int,26>a{},b{};for(int i=l1-1;i<r1;i++)a[s[i]-'a']++;for(int i=l2-1;i<r2;i++)b[s[i]-'a']++;cout<<(a==b?"YES":"NO")<<'\n';}}
