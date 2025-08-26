#include <stdio.h>
int main(){
    float imc, peso, altura; 

    printf("Digite seu peso: ");
    scanf("%f", &peso);
   
    printf("Digite sua altura: ");    
    scanf("%f", &altura);
   
    imc = peso / (altura * altura);
    printf("Seu imc e: %.2f\n", imc);
    
    if (imc < 18.5) {
        printf("A baixo do peso.");
    }
    else if ( imc >= 18.5 && imc <= 24.9 ) {
        printf("Peso normal.\n");
    }
    else if ( imc >= 25.0 && imc <= 29.9 ) {
        printf("Excesso de peso.\n");
    }
    else if ( imc >= 30.0 && imc <= 34.9 ) {
        printf("Obesidade grau 1.\n");
    }
    else if ( imc >= 35.0 && imc <= 39.9 ) {
        printf("Obesidade grau 2.\n");
    }
    else {
        printf("Obesidade grau 3.\n ");
    }


    return 0; 



}
