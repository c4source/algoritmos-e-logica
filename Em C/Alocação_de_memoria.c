#include <stdio.h>
#include <stdlib.h> // Essencial para malloc, free e NULL

int main() {
    // Declaração de um ponteiro para inteiro
    int *ptr = NULL; 
    
    // Alocação de memória para 10 inteiros (40 bytes em sistemas típicos)
    ptr = (int *) malloc(10 * sizeof(int));

    // Verificação de alocação (Boa Prática!)
    if (ptr == NULL) {
        printf("Erro: Falha na alocacao de memoria!\n");
        return 1; // Retorna um código de erro
    }

    // --- Uso do Bloco de Memória Alocada ---
    // (Por exemplo, para inicializar os 10 elementos)
    for (int i = 0; i < 10; i++) {
        ptr[i] = i * 2; 
        printf("ptr[%d] = %d\n", i, ptr[i]);
    }
    // ----------------------------------------

    // Desalocação da memória
    free(ptr);
    
    // Boa prática: anular o ponteiro para evitar o uso de um "dangling pointer"
    ptr = NULL; 

    return 0;
}