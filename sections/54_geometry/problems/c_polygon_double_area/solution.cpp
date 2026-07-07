#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<long long>x(n),y(n);for(int i=0;i<n;i++)cin>>x[i]>>y[i];long long s=0;for(int i=0;i<n;i++){int j=(i+1)%n;s+=x[i]*y[j]-y[i]*x[j];}cout<<llabs(s)<<'\n';}
