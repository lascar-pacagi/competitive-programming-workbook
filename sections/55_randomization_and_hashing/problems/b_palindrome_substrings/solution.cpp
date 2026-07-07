#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string s;if(!(cin>>s))return 0;int q;cin>>q;while(q--){int l1,r1,l2,r2;cin>>l1>>r1>>l2>>r2;cout<<(([&](){string t=s.substr(l1-1,r1-l1+1),u=t;reverse(u.begin(),u.end());return t==u;})()?"YES":"NO")<<'\n';}}
