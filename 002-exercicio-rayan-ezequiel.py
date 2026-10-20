import os
os.system('cls')


# 2. Crie um algoritmo que leia a temperatura registrada em cada dia da semana (7 dias), 
# armazenando em um vetor. Mostre todas as temperaturas, a média da semana, a maior e a menor temperatura.

temperaturas = []

for i in range(7):
    temperaturas.append(float(input(f'Digite a {i + 1}º temperatura: ' )))

media_temperaturas = sum(temperaturas) / len(temperaturas)
print(f'Temperaturas: {temperaturas}.\nMédia da semana: {media_temperaturas:.2f}°.\nMaior temperatura: {max(temperaturas)}°.\nMenor temperatura: {min(temperaturas)}°')
