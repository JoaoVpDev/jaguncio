# Escreva um algoritmo que permita a leitura de 7 nomes e coloque em uma lista. Exiba a lista de trás para frente, 
# exibindo no início o último nome informado e o ao final da lista o primeiro. Exiba um nome a cada linha.

nomes = ([(input())for i in range(7)]).reverse()
nomes.reverse()

for i in range(7):
    print(nomes[i])