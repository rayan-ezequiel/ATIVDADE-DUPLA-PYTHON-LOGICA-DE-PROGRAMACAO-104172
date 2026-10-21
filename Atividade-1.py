import os
os.system('cls')

# Leia 5 números inteiros, armazene-os em um vetor e
# mostre os números na ordem digitada e depois na ordem inversa.


numeros_inteiros = []

for i in range(5):
    numero = int(input(f'Digite o {i + 1}º numero: '))
print(f'Números: {numeros_inteiros}\nOrdem Inversa: {(numeros_inteiros[4]), (numeros_inteiros[3])} ')