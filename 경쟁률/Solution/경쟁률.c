#include<stdio.h>
#include<math.h>
int main() {
    int t;
    scanf("%d",&t);
    while(t--){
        double n,m;
        scanf("%lf %lf",&n,&m);
        printf("%.1lf:1\n",round(m/n*10)/10);
    }
}
