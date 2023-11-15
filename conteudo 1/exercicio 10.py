# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
inicial = int(input('Digite o primneiro numero: '))
final = int(input('Digite o segundo numero: '))

for i in range(inicial+1, final):
    print(i,end='')
    if i != final-1 :
        print(end= ', ')
print(f' Sao os numeros que estao entre {inicial} e {final}')