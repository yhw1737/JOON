#include<stdio.h>

int main(){
    int t;
    scanf("%d",&t);
    while(t--){
        int n;
        scanf("%d",&n);
        printf("%d\n",n/80+n%80/40+n%40/20+n%20/10+n%10/5);
    }
}