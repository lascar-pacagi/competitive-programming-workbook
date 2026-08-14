#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int t;cin>>t;while(t--){int n;cin>>n;map<long long,long long>d;while(n--){long long l,r;cin>>l>>r;++d[l];--d[r+1];}long long cur=0,best=-1,when=0;for(auto[x,v]:d){cur+=v;if(cur>best){best=cur;when=x;}}cout<<best<<' '<<when<<'\n';}}
