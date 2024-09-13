#include<stdio.h>
#include<math.h>
int main() {
    int t;
    scanf("%d",&t);
    while(t--){
        double n,m;
        scanf("%lf %lf",&n,&m);
        printf("%.0lf:1\n",round((m-n)/n));
    }
}
