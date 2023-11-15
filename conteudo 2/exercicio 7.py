# Crie um programa em Python para ler uma frase, separar palavra por palavra e exibir cada palavra em uma linha.

frase = str(input())
frase = frase.split()

for i in range(len(frase)):
    print(frase[i])