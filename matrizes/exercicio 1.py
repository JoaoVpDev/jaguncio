# Faça um programa que preencha uma matriz 20x3 com as notas de vinte alunos em três provas 
# (complete com valores aleatórios de 0 a 10 para evitar a leitura de muitos valores).
# O programa deve mostrar em que posição aparecem as menores notas para: prova 1, prova 2 e prova 3. Exiba a posição e a nota.


matriz = [[int(input(f'Digite a nota {i+1}: '))for j in range(3)] for i in range(3)]

for i in range(3):
    menor_nota = 10
    linha = 0
    for j in range(3):
        if matriz[i][j] < menor_nota:
            menor_nota = matriz[i][j]
            linha = j

    print(f'{menor_nota} esta na posicao: {linha} x {i}')