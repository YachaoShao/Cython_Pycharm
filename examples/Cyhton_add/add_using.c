#include<stdio.h>
#include"addfunc.h"
int addfunc(int,int);
int main(){
    int x1=1;
    int x2=2;
    printf("The result of addition %d and %d is %d", x1,x2,addfunc(x1,x2));
}