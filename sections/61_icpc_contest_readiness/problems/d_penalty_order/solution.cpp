#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int n;if(!(cin>>n))return 0;vector<long long> t(n);for(auto&x:t)cin>>x;sort(t.begin(),t.end());__int128 elapsed=0,answer=0;for(long long x:t){elapsed+=x;answer+=elapsed;}if(answer==0)cout<<0;string out;while(answer){out.push_back('0'+answer%10);answer/=10;}reverse(out.begin(),out.end());cout<<out<<'\n';}
