import os
os.system('cls')

# Leia as temperaturas dos 7 dias da semana em um vetor.
# Mostre todas, a média semanal, a maior e a menor temperatura.

temperaturas = []
for i in range(7):
    temperatura = float(input(f'Digite a {i +1}º temperatura: '))
    temperaturas.append(temperatura)
    media_semanal = sum(temperaturas) / len(temperaturas)
print(f'Todas temperaturas: {temperaturas}\nMédia Semanal: {media_semanal}\nMaior temperatura: {max(temperaturas)}\nMenor temperatura: {min(temperaturas)}')
