#include <bits/stdc++.h>
using namespace std;
int main(){ios::sync_with_stdio(false);cin.tie(nullptr);int m,q;if(!(cin>>m>>q))return 0;
int size=1;while(size<m)size*=2;vector<int> count(2*size);
auto change=[&](int x,int delta){int z=size+x-1;count[z]+=delta;for(z/=2;z;z/=2)count[z]=count[2*z]+count[2*z+1];};
auto prefix=[&](int x){int l=size,r=size+x,total=0;while(l<r){if(l&1)total+=count[l++];if(r&1)total+=count[--r];l/=2;r/=2;}return total;};
while(q--){int op,x;cin>>op>>x;
if(op==1)change(x,1);else if(op==2){if(count[size+x-1])change(x,-1);}
else if(op==4)cout<<prefix(x)<<'\n';else if(x>count[1])cout<<-1<<'\n';
else{int z=1;while(z<size){if(count[2*z]>=x)z*=2;else{x-=count[2*z];z=2*z+1;}}cout<<z-size+1<<'\n';}}
}
