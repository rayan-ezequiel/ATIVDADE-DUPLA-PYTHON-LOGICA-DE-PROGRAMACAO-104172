import os
os.system('cls')

# Leia 5 números inteiros, armazene-os em um vetor e
# mostre os números na ordem digitada e depois na ordem inversa.


numeros_inteiros = []

for i in range(5):
    
    numero = int(input(f'Digite o {i + 1}º numero: '))
    numeros_inteiros.append(numero)
print(f'Números: {numeros_inteiros}')
print(f'Ordem inversa: {numeros_inteiros[: : -1]}')