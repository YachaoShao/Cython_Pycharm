//main function
#include "./power/power.h"
#include <stdio.h>

double power(double,int);

int main(int argc, char const *argv[]) {
  /* code */
  if (argc<3){
    printf("Usage: %s base exponent \n",argv[0]);
    return 1;
  }
  double base = atof(argv[1]);
  int exponent =atoi(argv[2]);
  double result =power(base, exponent);
  printf("%g ˆ %d is %g\n",base, exponent, result);
  return 0;
}
