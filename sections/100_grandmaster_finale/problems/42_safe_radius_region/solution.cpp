#include <bits/stdc++.h>
using namespace std;
const double EPS=1e-10,PI=acos(-1.0);
struct P {
    double x,y;
    P operator+(P b)const {
        return {
            x+b.x,y+b.y
        }
        ;
    }
    P operator-(P b)const {
        return {
            x-b.x,y-b.y
        }
        ;
    }
    P operator*(double k)const {
        return {
            x*k,y*k
        }
        ;
    }
}
;
double cross(P a,P b) {
    return a.x*b.y-a.y*b.x;
}
double dot(P a,P b) {
    return a.x*b.x+a.y*b.y;
}
double norm(P a) {
    return hypot(a.x,a.y);
}
struct L {
    P p,v;
    double angle;
}
;
P meet(L a,L b) {
    double t=cross(b.p-a.p,b.v)/cross(a.v,b.v);
    return a.p+a.v*t;
}
vector<P>halfplanes(vector<pair<P,P>>raw, bool presorted=false) {
    vector<L>a;
    for(auto[p,q]:raw) {
        P v=q-p;
        a.push_back({p,v,atan2(v.y,v.x)});
    }
    if(!presorted)sort(a.begin(),a.end(),[](L x,L y){return x.angle<y.angle;});
    vector<L>u;
    for(L z:a) {
        if(!u.empty()&&abs(cross(u.back().v,z.v))<=EPS&&dot(u.back().v,z.v)>0) {
            if(cross(u.back().v,z.p-u.back().p)>EPS)u.back()=z;
        }
        else u.push_back(z);
    }
    deque<L>q;
    deque<P>pts;
    auto inside=[](L l,P p) {
        return cross(l.v,p-l.p)>=-EPS;
    }
    ;
    for(L z:u) {
        while(!pts.empty()&&!inside(z,pts.back()))pts.pop_back(),q.pop_back();
        while(!pts.empty()&&!inside(z,pts.front()))pts.pop_front(),q.pop_front();
        if(!q.empty()&&abs(cross(q.back().v,z.v))<=EPS)return {
        }
        ;
        if(!q.empty())pts.push_back(meet(q.back(),z));
        q.push_back(z);
    }
    while(!pts.empty()&&!inside(q.front(),pts.back()))pts.pop_back(),q.pop_back();
    while(!pts.empty()&&!inside(q.back(),pts.front()))pts.pop_front(),q.pop_front();
    if(q.size()<3)return {
    }
    ;
    pts.push_back(meet(q.back(),q.front()));
    return vector<P>(pts.begin(),pts.end());
}
double area(vector<P>p) {
    double s=0;
    for(int i=0;i<(int)p.size();i++)s+=cross(p[i],p[(i+1)%p.size()]);
    return abs(s)/2;
}
vector<P>shifted(vector<P>p,double r) {
    vector<pair<P,P>>l;
    for(int i=0;i<(int)p.size();i++) {
        P q=p[(i+1)%p.size()],v=q-p[i],s= {
            -v.y*r/norm(v),v.x*r/norm(v)
        }
        ;
        l.push_back({p[i]+s,q+s});
    }
    return halfplanes(l,true);
}
double inradius(vector<P>p) {
    int at=0;
    for(int i=1;i<(int)p.size();i++) {
        P vi=p[(i+1)%p.size()]-p[i],va=p[(at+1)%p.size()]-p[at];
        if(atan2(vi.y,vi.x)<atan2(va.y,va.x))at=i;
    }
    rotate(p.begin(),p.begin()+at,p.end());
    double minx=p[0].x,maxx=p[0].x,miny=p[0].y,maxy=p[0].y;
    for(P x:p)minx=min(minx,x.x),maxx=max(maxx,x.x),miny=min(miny,x.y),maxy=max(maxy,x.y);
    double lo=0,hi=max(maxx-minx,maxy-miny)+1;
    for(int z=0;z<70;z++) {
        double m=(lo+hi)/2;
        (shifted(p,m).empty()?hi:lo)=m;
    }
    return lo;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout<<fixed<<setprecision(10);
    int n;
    cin>>n;
    vector<P>p(n);
    for(auto&x:p)cin>>x.x>>x.y;
    cout<<inradius(p)<<'\n';
}
