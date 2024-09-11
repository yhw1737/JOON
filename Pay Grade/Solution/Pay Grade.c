#include<stdio.h>
#include<string.h>
int main() {
    char a[9][500] = { "" };
    char txt[10], txt2[10];
    int t;
    scanf("%d",&t);
    while(t--){
        scanf("%s %s", txt, txt2);
        if (strcmp(txt,"PVT")==0){
            strcat(a[0]," ");
            strcat(a[0],txt2);
        }
        if (strcmp(txt,"PV2")==0){
            strcat(a[1]," ");
            strcat(a[1],txt2);
        }
        if (strcmp(txt,"PFC")==0){
            strcat(a[2]," ");
            strcat(a[2],txt2);
        }
        if (strcmp(txt,"SPC")==0){
            strcat(a[3]," ");
            strcat(a[3],txt2);
        }
        if (strcmp(txt,"CPL")==0){
            strcat(a[3]," ");
            strcat(a[3],txt2);
        }
        if (strcmp(txt,"SGT")==0){
            strcat(a[4]," ");
            strcat(a[4],txt2);
        }
        if (strcmp(txt,"SSG")==0){
            strcat(a[5]," ");
            strcat(a[5],txt2);
        }
        if (strcmp(txt,"SFC")==0){
            strcat(a[6]," ");
            strcat(a[6],txt2);
        }
        if (strcmp(txt,"MSG")==0){
            strcat(a[7]," ");
            strcat(a[7],txt2);
        }
        if (strcmp(txt,"1SG")==0){
            strcat(a[7]," ");
            strcat(a[7],txt2);
        }
        if (strcmp(txt,"SGM")==0){
            strcat(a[8]," ");
            strcat(a[8],txt2);
        }
        if (strcmp(txt,"CSM")==0){
            strcat(a[8]," ");
            strcat(a[8],txt2);
        }
    }
    for(int i=0;i<9;i++){
        if (strcmp(a[i], "") != 0) printf("E%i%s\n", i+1, a[i]);
    }
}
