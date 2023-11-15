#sequencia de fibonacci com while
num = int(input('digite um numero: '))
sequencia_anterior = 1
sequencia = 1
atual = 0
fibonot = 4
while atual < num:
    print(f'{atual}',end= '')
    sequencia = atual + sequencia_anterior
    sequencia_anterior = atual
    atual = sequencia
    if atual <= num:
        print(' -> ',end='')
    