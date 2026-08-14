#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;cin>>n;priority_queue<long long>lo;priority_queue<long long,vector<long long>,greater<long long>>hi;for(int i=0;i<n;i++){long long x;cin>>x;if(lo.empty()||x<=lo.top())lo.push(x);else hi.push(x);if(lo.size()<hi.size()){lo.push(hi.top());hi.pop();}if(lo.size()>hi.size()+1){hi.push(lo.top());lo.pop();}cout<<lo.top()<<(i+1==n?'\n':' ');}}
