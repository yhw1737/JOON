#include<stdio.h>
#include<math.h>
int main() {
    int t;
    scanf("%d",&t);
    while(t--){
        double k,d,a;
        scanf("%lf %lf %lf",&k,&d,&a);
        if (d == 0){
            printf("Perfect\n");
        }
        else{
            double dd = (k+a)/d*10;
            double di = round(dd)/10;
            printf("%.1lf\n",di);
        }
    }
}
