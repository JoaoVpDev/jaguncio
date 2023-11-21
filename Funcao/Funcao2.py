import random

def cria_matriz_quadrada(dim):  #### Funcao para criar matriz quadrada
    '''funcao para criar matriz quadrada''' 
    m = [[ random.randint(1,9) for j in range(dim)] for i in range(dim) ]
    return m


def soma_diagonal_principal(m, dim):  
    soma = 0 
    for i in range(dim):
        soma += m[i][i]   #[i][i]  pois quando forem os mesmos valores irao se somar
    return soma


def print_matriz(l, mat):
    for l in mat:
        print(l)
    return print


matriz = cria_matriz_quadrada(3)
print(print_matriz(3, matriz))
# print(cria_matriz_quadrada(3, matriz).__doc__)


for linha in matriz:
    print(linha)
print('a soma da diagonal principal e: ', soma_diagonal_principal(matriz, 3))


matriz2 = cria_matriz_quadrada(3) 
for linha in matriz2:
    print(linha)
print('a soma da diagonal principal e: ', soma_diagonal_principal(matriz2, 3))


matriz3 = cria_matriz_quadrada(3) 
for linha in matriz3:
    print(linha)
print('a soma da diagonal principal e: ', soma_diagonal_principal(matriz3, 3))

