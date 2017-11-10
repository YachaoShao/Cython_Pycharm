//main function
//#include "./power/power.h"
#include <stdio.h>
#include "config.h"
#include <stdlib.h>




#ifdef USE_MYMATH
  #include "power/power.h"
#else
  #include<math.h>
#endif


int main(int argc, char const *argv[]) {
  /* code */
  if (argc<3){
    printf("Usage: %s base exponent \n",argv[0]);
    return 1;
  }
  double base = atof(argv[1]);
  int exponent =atoi(argv[2]);

#ifdef HAVE_POW
      printf("Now we use the standard library.\n");
      double result=pow(base, exponent);
#else
      printf("Now we are using our own Math library.\n");
      double result =power(base, exponent);
#endif

  // #ifdef USE_MYMATH
  //   printf("Now we are using our own Math library.\n");
  //   double result =power(base, exponent);
  // #else
  //   printf("Now we use the standard library.\n");
  //   double result=pow(base, exponent);
  // #endif
  printf("%g ˆ %d is %g\n",base, exponent, result);
  return 0;
}
