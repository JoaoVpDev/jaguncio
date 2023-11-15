# Escreva um algoritmo que permita a leitura de 7 números inteiros. Gere um vetor com os mesmos valores 
# digitados mas de maneira invertida, ou seja, o primeiro número lido ficará na última posição do vetor. 
# Exiba o vetor ao final colocando um número a cada linha.

lista = [0] * 7

for i in range(-1, -8, -1):
    lista[i] = int(input(''))

for i in range(0, 7):
    print(lista[i])
