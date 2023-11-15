# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
usuario = 'a'
senha = 'a'

while usuario == senha: 
    usuario = str(input('Digite seu nome de usuário: '))
    senha = str(input('Digite sua senha: '))
    if usuario == senha:
        print('Tentativa inválida, nome de usuário e senha são iguais, tente novamente: ')
print(f'Parabéns {usuario}, você conseguiu se cadastrar')