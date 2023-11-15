# Faça um programa que leia 5 números e informe o maior número.
numeros = []

for i in range(0, 5):
    num = int(input('Digite um número'))
    numeros.append(num)
    num_max = max(numeros)
print(f' o maior numero  e: {num_max}')
