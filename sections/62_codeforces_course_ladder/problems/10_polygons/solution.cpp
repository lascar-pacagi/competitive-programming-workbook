#include <bits/stdc++.h>
using namespace std;int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int t;cin>>t;while(t--){long long n,k,s;cin>>n>>k>>s;if(s>n*k){cout<<-1<<'\n';continue;}for(long long i=0;i<n;i++){long long x=max(0LL,s-(n-i-1)*k);if(i)cout<<' ';cout<<x;s-=x;}cout<<'\n';}}
