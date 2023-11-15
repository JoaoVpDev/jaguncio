# Faça um algoritmo que leia o nome de 20 pessoas e exiba ao final a lista de nomes em ordem alfabética. Exiba um nome por linha.

nomes = sorted([str(input()) for i in range(20)])

for i in range(20):
    print(nomes[i])

