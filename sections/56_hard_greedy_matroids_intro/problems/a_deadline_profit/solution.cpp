#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<pair<int,int>>j(n);for(auto&x:j)cin>>x.first>>x.second;sort(j.begin(),j.end());priority_queue<int,vector<int>,greater<int>>pq;for(auto[d,p]:j){pq.push(p);if((int)pq.size()>d)pq.pop();}long long s=0;while(!pq.empty()){s+=pq.top();pq.pop();}cout<<s<<'\n';}
