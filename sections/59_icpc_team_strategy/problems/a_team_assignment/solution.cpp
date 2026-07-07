#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<int>a(n);int tot=0;for(int&x:a){cin>>x;tot+=x;}int best=1e9;for(int m=0;m<(1<<n);m++){int s=0;for(int i=0;i<n;i++)if(m>>i&1)s+=a[i];best=min(best,max(s,tot-s));}cout<<best<<'\n';}
