# def soma(a,b):
#     soma = a + b
#     return soma
# x = int(input())
# y = int(input())

# print(soma(x,y))
#-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-

# def somatorio(n):
#     somatorio = 0
#     for i in range(n):
#         if i %2 != 0:
#             somatorio += i 
#     return somatorio

# n = int(input())
# print(somatorio(n))

#-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-
# Desenvolva uma função sequencia(n) para calcular a sequência da potência de 2 até o valor informado.

# Ex. sequencia(100) deve apresentar:
# 2
# 4
# 8
# 16
# 32
# 64

# def sequencia(n):
#     for i in range(n):
#         potencia = 2**i
#         if potencia <= n:
#             print(potencia)
#     return sequencia
# n = int(input())
# print(sequencia(n))
#-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-

# Faça uma função chamada multiplos7(inicio,fim) que retorna a SOMA dos 
# múltiplos de 7 entre um valor inicial e um valor final (inclusive).

# def multiplos7(inicio, fim):
#     multiplos7 = 0
#     for i in range(inicio-1, fim+1):
#         if i % 7 == 0:
#             multiplos7 += i
#     return multiplos7
#-=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=--=-=-

def minhaFuncao(a,b,c):
   x = a + b *c
   y = a *b + c
   return x-y
   x = y*2

lista = [3, 5, 7]
k = minhaFuncao(lista[0], lista[1], lista[2])
lista = [6, 4, k-77872]
print(lista[0] + lista[1] + lista[2])
