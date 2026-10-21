import os
os.system('cls')

# Leia 8 números inteiros em um vetor e peça um número para
# pesquisar. Informe se ele existe e em qual posição está;
# caso não exista, mostre Número não encontrado.

numeros_inteiros = []

while True:
    numeros_inteiros.append(int(input('Digite um número: ')))
    if len(numeros_inteiros) == 8:
        pesquisa = int(input('Digite um número para pesquisar: '))
        if pesquisa in numeros_inteiros:
            print('Esse número existe na lista.')
        else: print('Esse número não existe na lista.')
        break