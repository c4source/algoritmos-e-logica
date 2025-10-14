// PONTEIROS
#include <stdio.h>


int main(){

    int var = 42;
    int *ponteiro; 

    ponteiro = &var;   // Atribuindo o endereço de var ao ponteiro, ponteiro

    printf("Valor da varial 'valor': %d\n", var);
    printf("Endereço da variavel 'valor': %p\n", &var);
    printf("Conteudo do ponteiro 'ponteiro': %p\n", ponteiro);
    printf("Valor apontado por 'ponteiro' (*ponteiro): %d\n", *ponteiro);
    
}