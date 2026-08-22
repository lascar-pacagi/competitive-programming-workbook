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
struct C {
    P p;
    double r;
}
;
double overlap(C a,C b) {
    double d=norm(a.p-b.p);
    if(d>=a.r+b.r)return 0;
    if(d<=abs(a.r-b.r))return PI*min(a.r,b.r)*min(a.r,b.r);
    double x=acos(clamp((d*d+a.r*a.r-b.r*b.r)/(2*d*a.r),-1.0,1.0)),y=acos(clamp((d*d+b.r*b.r-a.r*a.r)/(2*d*b.r),-1.0,1.0));
    return a.r*a.r*x+b.r*b.r*y-d*a.r*sin(x);
}
int tangents(C a,C b) {
    double d=norm(a.p-b.p);
    if(d<=EPS)return abs(a.r-b.r)<=EPS?-1:0;
    int ans=0;
    for(double z:{abs(a.r-b.r),a.r+b.r})ans+=d>z+EPS?2:(abs(d-z)<=EPS);
    return ans;
}
C circle2(P a,P b) {
    P c=(a+b)*.5;
    return {
        c,norm(a-b)/2
    }
    ;
}
C circle3(P a,P b,P c) {
    double d=2*cross(b-a,c-a);
    double aa=dot(a,a),bb=dot(b,b),cc=dot(c,c);
    P o= {
        (aa*(b.y-c.y)+bb*(c.y-a.y)+cc*(a.y-b.y))/d,(aa*(c.x-b.x)+bb*(a.x-c.x)+cc*(b.x-a.x))/d
    }
    ;
    return {
        o,norm(o-a)
    }
    ;
}
C mec(vector<P>p) {
    mt19937 rng(947311);
    shuffle(p.begin(),p.end(),rng);
    C c {
        {
            0,0
        }
        ,-1
    }
    ;
    auto outside=[](P x,C c) {
        return c.r<0||norm(x-c.p)>c.r+1e-9;
    }
    ;
    for(int i=0;i<(int)p.size();i++)if(outside(p[i],c)) {
        c= {
            p[i],0
        }
        ;
        for(int j=0;j<i;j++)if(outside(p[j],c)) {
            c=circle2(p[i],p[j]);
            for(int k=0;k<j;k++)if(outside(p[k],c))c=circle3(p[i],p[j],p[k]);
        }
    }
    return c;
}
struct T {
    int a,b,c;
}
;
double orient(P a,P b,P c) {
    return cross(b-a,c-a);
}
bool incircle(P a,P b,P c,P p) {
    double ax=a.x-p.x,ay=a.y-p.y,bx=b.x-p.x,by=b.y-p.y,cx=c.x-p.x,cy=c.y-p.y;
    double d=(ax*ax+ay*ay)*(bx*cy-by*cx)-(bx*bx+by*by)*(ax*cy-ay*cx)+(cx*cx+cy*cy)*(ax*by-ay*bx);
    return d>EPS;
}
pair<vector<T>,vector<pair<int,int>>>delaunay(vector<P>p) {
    int n=p.size();
    if(n<3)return {
        {
        }
        , {
        }
    }
    ;
    double minx=p[0].x,maxx=p[0].x,miny=p[0].y,maxy=p[0].y;
    for(P x:p)minx=min(minx,x.x),maxx=max(maxx,x.x),miny=min(miny,x.y),maxy=max(maxy,x.y);
    double s=max({maxx-minx,maxy-miny,1.0}),cx=(minx+maxx)/2,cy=(miny+maxy)/2;
    p.push_back({cx-10000*s,cy-8000*s});
    p.push_back({cx+10000*s,cy-8000*s});
    p.push_back({cx,cy+10000*s});
    vector<T>tri= {
        {
            n,n+1,n+2
        }
    }
    ;
    for(int x=0;x<n;x++) {
        map<pair<int,int>,pair<int,pair<int,int>>>edges;
        vector<char>bad(tri.size());
        for(int i=0;i<(int)tri.size();i++)if(incircle(p[tri[i].a],p[tri[i].b],p[tri[i].c],p[x])) {
            bad[i]=1;
            for(auto e:{pair{tri[i].a,tri[i].b},pair{tri[i].b,tri[i].c},pair{tri[i].c,tri[i].a}}) {
                auto key=minmax(e.first,e.second);
                edges[key].first++;
                edges[key].second=e;
            }
        }
        vector<T>next;
        for(int i=0;i<(int)tri.size();i++)if(!bad[i])next.push_back(tri[i]);
        for(auto[key,data]:edges)if(data.first==1) {
            auto[u,v]=data.second;
            if(orient(p[u],p[v],p[x])<0)swap(u,v);
            next.push_back({u,v,x});
        }
        tri.swap(next);
    }
    vector<T>clean;
    set<pair<int,int>>edges;
    for(T t:tri)if(max({t.a,t.b,t.c})<n) {
        clean.push_back(t);
        edges.insert(minmax(t.a,t.b));
        edges.insert(minmax(t.b,t.c));
        edges.insert(minmax(t.c,t.a));
    }
    return {
        clean,vector<pair<int,int>>(edges.begin(),edges.end())
    }
    ;
}
double radii(vector<P>p,bool maximum) {
    auto[tri,e]=delaunay(p);
    double ans=0;
    for(T t:tri) {
        double r=circle3(p[t.a],p[t.b],p[t.c]).r;
        if(maximum)ans=max(ans,r);
        else ans+=r;
    }
    return ans;
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout<<fixed<<setprecision(10);
    int n;
    cin>>n;
    vector<P>p(n);
    for(auto&x:p)cin>>x.x>>x.y;
    cout<<radii(p,false)<<'\n';
}
