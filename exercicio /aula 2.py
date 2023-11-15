#Criar matriz 3x3 e preencher os valores lidos

matriz = [[0], [0], [0]], [[0], [0], [0]], [[0], [0], [0]]

for linha in range (0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))

print('-=' * 30 )
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]::^5}]', end='') #":^" serve para formatar as colunas para 5 cassas decimais
    print()  #este print serve para quebrar a linha e printa em linha diferentes