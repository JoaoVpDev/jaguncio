# Crie um programa em Python para ler dois vetores de 15 posições de inteiros cada e mostre a interseção dos vetores. 
# Primeiro faça a leitura dos 15 valores inteiros para o primeiro vetor e depois os 15 valores do segundo. 
# Lembrando que intersecção são elementos repetidos em ambos sem repetição (observe que os valores iguais normalmente não estarão na mesma posição). 
# Para facilitar, considere que os valores não se repetem dentro do mesmo vetor.

lista01 = [0] * 15
lista02 = [0] * 15
interseccao =[]

for i in range(15):
    lista01[i] = int(input())

for i in range(15):
    lista02[i] = int(input())


for i in lista01:
    if i in lista02:
        print(i)
