#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int t;cin>>t;while(t--){int n;cin>>n;vector<long long>a(n);long long total=0;for(auto&x:a){cin>>x;total+=x;}long long left=0,best=LLONG_MAX;int pos=1;for(int i=0;i<n-1;i++){left+=a[i];long long diff=llabs(left-(total-left));if(diff<best){best=diff;pos=i+1;}}cout<<best<<' '<<pos<<'\n';}}
