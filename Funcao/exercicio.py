#MENU
print('(C) para calcular area do circulo')
print('(R) para calcular area do retangulo')
print('(Q) para calcular area do quadrado')
print('(T) para calcular area do Trapezio')
print('(S) para sair')

escolha = 0
def areaCirculo():
    raio = float(input('Informe o raio do circulo: '))
    area_circulo = 3.14 * raio**2
    print(area_circulo)

def areaRetangulo():
    altura: int(input('Informe a altura do retangulo/quadrado : '))
    largura: int(input('Informe a largura do retangulo/quadrado: '))
    area_retangulo = altura * largura
    print(area_retangulo)

# def areaTrazpezio():
#     base = int(input('Informe a base do trapezio:'))
#     topo = int(input('Informe o comprimeito do topo'))
#     altura_t = int(input('informe a altura do trapezio'))   
#     area_trapezio = 
#     print(are)

while escolha != 'S':

    escolha = str(input('Digite sua opcao desejada')).upper()
    
    if escolha == 'C': areaCirculo()

    elif escolha == 'R':areaRetangulo()

    # elif escolha == 'T':areaTrazpezio()
    
    elif escolha == 'S':
        break

    print('(C) para calcular area do circulo')
    print('(R) para calcular area do retangulo')
    print('(Q) para calcular area do quadrado')
    print('(T) para calcular area do Trapezio')
    print('(S) para sair')




