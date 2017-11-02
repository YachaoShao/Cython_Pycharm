#include<stdio.h>
#include"addfunc.h"
double mean(double, double);
int main(){
	double x1,x2,m;
	x1=2.4;
	x2=4.8;
	
	m=mean(x1,x2);
//	m=x1+x2;
//	std::cout << "The result of "<<x1<<" + "<<x2<<" is " << m<< std::endl;
	printf("The mean of %f and %f is %f\n",x1,x2,m);
	return 0;
}

