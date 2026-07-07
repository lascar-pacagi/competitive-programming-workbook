#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s)) return 0; int q;cin>>q; while(q--){int l,r;cin>>l>>r; string t=s.substr(l-1,r-l+1); string u=t; reverse(u.begin(),u.end()); cout<<(t==u?"YES":"NO")<<'\n';}}
