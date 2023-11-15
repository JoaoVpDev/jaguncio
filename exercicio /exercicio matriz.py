# Faça um programa em Python para preencher uma matriz M de dimensão 5x5 com uma sequência numérica iniciando em 0 e adicionando 
# valores coluna a coluna iniciando na primeira linha e terminando na quinta, conforme exemplo abaixo:

#Criar matriz 3x3 e preencher os valores lidos

# matriz = [[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]

# for linha in range (0, 3):
#     for coluna in range(0, 3):
#         matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

# print('-=' * 30 )
# for linha in range(0, 3):
#     for coluna in range(0, 3):
#         print(f'[{matriz[linha][coluna]::^5}]', end='') #":^" serve para formatar as colunas para 5 cassas decimais
#     print()  #este print serve para quebrar a linha e printa em linha diferentes

matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
valor = 0
for linha in range(0, 5):
    for coluna in range(0,5):
        matriz[linha][coluna] = valor
        valor += 1
print(matriz)

# Faça um programa Python para somar todos os elementos da matriz do exercício anterior e calcular a média dos valores. 
# Exiba ao final uma linha com a soma dos valores (valor inteiro) e outra linha com a média dos valores da matriz com uma casa decimal.

soma = 0
for i in range(5):
    soma += sum(matriz[i])
print(soma)
media = soma / 25
print(media)



