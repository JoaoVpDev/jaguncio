# Altere o programa anterior para mostrar no final a soma dos números.
inicial = int(input('Digite o primneiro numero: '))
final = int(input('Digite o segundo numero: '))
soma = 0
for i in range(inicial+1, final):
    print(i,end='')
    if i != final-1 :
        print(end= ', ')
    soma = soma + i
print(f' Sao os numeros que estao entre {inicial} e {final} e a soma entre os numero do intervalo e: {soma}')
