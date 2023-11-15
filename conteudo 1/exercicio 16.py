# A série de Fibonacci é formada pela sequência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa que gere a série até que o valor seja maior que 500.
num = []
sequencia_anterior = sequencia = 1
atual = 0
while atual != num:
    sequencia = atual + sequencia_anterior
    sequencia_anterior = atual
    atual = sequencia
    if sequencia_anterior > 500:
        continue
    print(atual) 