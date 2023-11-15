# Ler dois valores inteiros L e C.
# Crie uma matriz de inteiros com dimensão LxC;
# Preencha a matriz com valores informados pelo usuário. Faça a leitura de cada um dos valores da matriz;
# Exiba a matriz ao final: print(matriz).



linha = int(input())
coluna = int(input())

matriz = [[0] * coluna for k in range(linha)]

print(matriz)

for i in range(linha):
    for j in range(coluna):
        matriz[i][j] = int(input())

print(matriz)


