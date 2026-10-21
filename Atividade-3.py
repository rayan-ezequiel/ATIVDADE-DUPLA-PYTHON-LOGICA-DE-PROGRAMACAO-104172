import os
os.system('cls')

# Leia 10 números inteiros em um vetor.
# Mostre a soma de todos os elementos e quantos números são maiores que 10.

numeros_inteiros = []
maior_10 = []
while True:
    numeros = int(input('Digite um número: '))
    numeros_inteiros.append(numeros)
    if numeros > 10:
        maior_10.append(numeros)
    if len(numeros_inteiros) == 10:
        soma = sum(numeros_inteiros)
        print(f'A soma é: {soma}\nMaiores que 10: {len(maior_10)}')
        break