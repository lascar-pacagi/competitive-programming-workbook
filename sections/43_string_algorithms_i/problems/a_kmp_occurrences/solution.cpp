#include <bits/stdc++.h>
using namespace std; vector<int> pi(string s){vector<int>p(s.size());for(int i=1;i<(int)s.size();i++){int j=p[i-1];while(j&&s[i]!=s[j])j=p[j-1];if(s[i]==s[j])j++;p[i]=j;}return p;}
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);string pat,text;if(!(cin>>pat>>text)) return 0; string s=pat+"#"+text; auto p=pi(s); vector<int>a; for(int i=0;i<(int)p.size();i++) if(p[i]==(int)pat.size()) a.push_back(i-2*(int)pat.size()+1); cout<<a.size()<<'\n'; for(int i=0;i<(int)a.size();i++){if(i)cout<<' ';cout<<a[i];} cout<<'\n';}
