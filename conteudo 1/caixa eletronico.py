# Os contadores são normalmente inicializados com valor 0 (zero) e incrementados em 1 (um) a cada vez que uma nova ocorrência 
# (ou situação) é processada. Os contadores são as variáveis que irão receber o acúmulo da contagem das informações.
# Imprima o nome de todos os 150 alunos do curso de TADS da UDESC/CEAD. Os nomes estão armazenados em uma lista chamada nomes.

def fibonot(n):
    a = 1
    b = 2
    c = 3
    while n > 0:
        a = b
        b = c
        c = a + b
        n -= (c - b - 1)
    n += (c - b - 1)
    return b + n

n = int(input())
print(fibonot(n))