# Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números ímpares.
pares = impares = 0
cont = 0
for i in range(1, 11):
    num = int(input('Digite um numero: '))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'A quantidade de numero pares e: {pares} e a quantidade de numero impares e: {impares}')

