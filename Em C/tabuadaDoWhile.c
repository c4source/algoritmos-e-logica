#include <stdio.h>
# define LIMITE 10 

    int main(){
        int t, c = 0; 
        printf("Numero da tabuada: ");    
        scanf("%i", &t);
        do {
            c++;
            printf("%i x %i = %i\n", t, c, (t*c));
            
        }while ( c < LIMITE);     
        
    return 0; 
        
    }
