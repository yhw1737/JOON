#include<stdio.h>
int main() {
    int t;
    scanf("%d",&t);
    while(t--){
        int n,m;
        scanf("%d %d",&n,&m);
        int ans = (90-m)/n+((90-m)%n!=0);
        if (ans < 0) ans = 0;
        printf("%d\n",ans);
    }
}
