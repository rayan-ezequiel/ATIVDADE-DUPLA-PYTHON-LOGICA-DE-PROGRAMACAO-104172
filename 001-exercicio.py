import os
os.system('cls')

# 1. Crie um algoritmo que leia 5 números inteiros, armazenando em um vetor.
# Mostre os números na ordem em que foram digitados e, em seguida, na ordem inversa.

numeros = []

while True:
    numeros.append(int(input('Digite um número: ')))
    if len(numeros) == 5:
        print(f'Ordem em que foram digitados: {numeros}')
        print(f'Ordem Inversa: {numeros[4], numeros[3], numeros[2], numeros[1], numeros[0]}')
        break