# A série de Fibonacci é formada pela sequência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.
num = int(input('Digite um numero: '))
sequencia_anterior = sequencia = 1
atual = 0

while atual != num:
    sequencia = atual + sequencia_anterior
    sequencia_anterior = atual
    atual = sequencia
    if atual > num:
        break
    print(atual) 