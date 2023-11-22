#include <stdio.h>
#include <math.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        double a, s, d, m, ans;
        scanf("%lf %lf %lf %lf",&a,&s,&d,&m);
        ans = round(a * floor(m * s) * (100 / (100 + d))*10)/10;
        printf("%.1lf\n",ans);
    }
}