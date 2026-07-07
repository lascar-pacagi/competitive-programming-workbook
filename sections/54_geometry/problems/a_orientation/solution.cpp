#include <bits/stdc++.h>
using namespace std; int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int T;if(!(cin>>T))return 0;while(T--){long long ax,ay,bx,by,cx,cy;cin>>ax>>ay>>bx>>by>>cx>>cy;long long v=(bx-ax)*(cy-ay)-(by-ay)*(cx-ax);cout<<(v>0?"LEFT":v<0?"RIGHT":"TOUCH")<<'\n';}}
