#include <stdio.h>
#define LIMITE 10 

int main() {
   int n;
   printf("Numero da tabuada: ");
   scanf("%d", &n);
   for (int c = 1; c <= LIMITE; c++){
        printf("%d x %d = %d\n", n, c, (n * c));
   }
return 0; 
}
