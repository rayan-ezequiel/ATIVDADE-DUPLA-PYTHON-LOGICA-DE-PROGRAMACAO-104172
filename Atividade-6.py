import os
os.system('cls')

# Leia dois vetores A e B com 5 inteiros cada.
# Gere C somando as posições correspondentes e mostre os três vetores.

vetor_A = []
vetor_B = []
vetor_C = []

while True:
    
    numeros_a = int(input('Digite um número inteiro para A: '))
    vetor_A.append(numeros_a)
    numeros_b = int(input('Digite um número inteiro para B: '))
    vetor_B.append(numeros_b)
    vetor_C.append(numeros_a + numeros_b)
    
    if len(vetor_A) and len(vetor_B) == 5:
        print(f'Vetor A: {vetor_A}\nVetor B: {vetor_B}\nSoma dos dois vetores: {vetor_C}')
        break