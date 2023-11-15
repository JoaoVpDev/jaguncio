# Faça um programa que leia e valide as seguintes informações:
# Nome: maior que 3 caracteres;
# Idade: entre 0 e 150;
# Salário: maior que zero;
# Sexo: 'f' ou 'm';
# Estado Civil: 's', 'c', 'v', 'd';
# Use a função len(string) para saber o tamanho de um texto (número de caracteres).
nome = '0'
letras = 0
while len(nome) < 3:
    nome = str(input('Digite seu nome: '))
    if len(nome) < 3:
        print(f'Opção inválida, tente novamente: ')

idade = -1
while idade < 0 or idade > 150:
    idade = int(input('Digite a sua idade: '))
    if idade < 0 or idade > 150:
        print('Opção inválida, tente novamente: ')

salario = -1
while salario < 0:
    salario = float(input('Digite o seu salário: '))
    if salario < 0:
        print('opção inválida, tente novamente: ')

sexo = 'N'
while sexo != 'masculino' and sexo != 'feminino':
    sexo = str(input(' Seu sexo é (M)asculino ou (F)eminino? ')).upper().strip()
    if sexo == 'M':
        sexo = 'masculino'
    elif sexo == 'F':
        sexo = 'feminino'
    else:
        print('Opção inválida, tente novamente: ')

estado = 'jovem'
while estado != 'solteiro' and estado != 'casado' and estado != 'viuvo' and estado != 'divorciado':
    print('(S)olteiro(a)')
    print('(C)asado(a)')
    print('(V)iúvo(a)')
    print('(D)ivorciado')
    estado = str(input('Digite o seu estado civil: ')).upper().strip()
    if estado == 'S':
        estado = 'solteiro'
    elif estado == 'C':
        estado = 'casado'
    elif estado == 'V':
        estado = 'viuvo'
    elif estado == 'D':
        estado = 'divorciado'
    else:
        print('Opção inválida, tente novamente')

print(f' seu nome é: {nome}',end='')
print(f', sua idade é: {idade} anos',end='')
print(f',e seu salário é de R$ {salario}',end='')
print(f', e seu sexo é: {sexo}',end='')
print(f', e seu estado civil é: {estado}')