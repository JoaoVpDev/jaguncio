# Faça um algoritmo que leia um vetor de 30 elementos inteiros e exiba o mesmo em ordem crescente. Imprima (exiba) um valor por linha.


lista = sorted([int(input()) for i in range(3)])

for i in range(3):
    print(lista[i])