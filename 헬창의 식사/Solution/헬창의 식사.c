#include<stdio.h>

int main() {
    int t, ans = 0;
    double ans2 = 0;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        double n,m;
        scanf("%lf %lf",&n,&m);
        if (ans2 > n/m || ans2 == 0){
            ans = i+1;
            ans2 = n/m;
        }
    }
    printf("%d",ans);
}
