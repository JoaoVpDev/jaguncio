# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação.
import math
continuar = 'S'
while continuar == 'S':
    ordem_a = int(input('Digite a ordem da população a: '))
    crescimento_a = float(input('Digite a porcenteagem de crescimento A: ')) / 100 + 1

    ordem_b = int(input('Digite a ordem da população b: '))
    crescimento_b = float(input('Digite a porcenteagem de crescimento B: ')) /100 + 1
    contador = 0


    while ordem_b >= ordem_a:
        ordem_a = ordem_a *  crescimento_a
        contador += 1
        ordem_b = ordem_b *crescimento_b
    print(math.trunc(ordem_a))
    print(math.trunc(ordem_b))
    print(f'Demorou {contador} anos para a população A se igualar a população B ')
    continuar = str(input('você deseja importar outros valores? se sim digite "S", se não digite "N": ')).strip().upper()
e