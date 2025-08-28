#include <stdio.h>
#define limite 10


int main () {
    int c = 0;
    int n; 
    printf("Numero da tabuada: ");
    scanf("%i", &n);

    while (c < limite){
        c++; 
        printf("%i x %i = %i\n", c, n, (c*n));
    }
    return 0;
}
