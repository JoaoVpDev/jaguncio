# Faça um programa para:

# Criar uma matriz 5x4 preenchendo em cada célula a multiplicação dos índices da matriz. Por exemplo, na posição [2][3] será colocado o valor 6 (2x3);
# O programa deve ler 12 valores inteiros, representando 6 posições (e 3 pares de posições). A cada quatro valores, representando duas posições na matriz, faça a troca dos valores na matriz;
# Faça as três trocas (para os 3 pares de posições);
# Mostre a matriz ao final usando print(matriz).
# trocar matriz[1][1] por matriz[2][2]  X    
# trocar matriz[1][2] por matriz [2][1]
# trocar matriz[0][0] por matriz [1][1]

matriz = [[linha * coluna for coluna in range(4)] for linha in range(5)]

for k in range(3):
    x = int(input())
    y = int(input())
    i = int(input()) 
    j = int(input()) 
    matriz[x][y], matriz[i][j] = matriz[i][j], matriz[x][y]

print(matriz)
print(matriz[2][6])

