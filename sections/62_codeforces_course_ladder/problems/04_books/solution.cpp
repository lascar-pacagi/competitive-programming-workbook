#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n,q;if(!(cin>>n>>q))return 0;vector<long long>d(n+2);while(q--){int l,r;long long x;cin>>l>>r>>x;d[l]+=x;d[r+1]-=x;}long long cur=0,best=LLONG_MIN;int pos=1;for(int i=1;i<=n;i++){cur+=d[i];if(cur>best){best=cur;pos=i;}}cout<<best<<' '<<pos<<'\n';}
