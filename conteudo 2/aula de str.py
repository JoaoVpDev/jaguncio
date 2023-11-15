# str1 = 'ola mundo'
# print(str1)
# str1 = str1.replace("m", "M") # (troca o caracter: "x", por"y")
# print(str1)

# if 'ola' in str1: #procurar um elemento na string
#     print('esta')

# if '$' not in str1: #procurar se n tem elemento na string
#     str1 = str1 + '$'
#     print(str1)

# posicao = str1.find('Mundo') #find procura em qual posi;'ao esta o elemento
# print(posicao)

# posicao = str1.find('1234')
# print(posicao)

# str1 = 'digite meu saco no teclado'
# lista = str1.split() #split separa a string em varaios elementos de lista
# print(lista)

# str1 = 'digite meu saco no teclado'
# lista = str1.replace(" ", "") #aqui usei replace para tirar os espacos entre uma string
# print(lista)

# letras = ['a', 'b', 'c']
# print('gato' in letras) # vai teronar False pois n tem 'gato' na array

# numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numeros[:5]) # limita aos 5 primeiros numeros   [inicio:final:passos]

# strings = ['te', 'ne', 'bro', 'so']
# print(''.join(strings)) # concatenar strings de uma lista (as aspas estao sem nada no meio, entao vai tirar os espacos entre elas)


# Exercício de criptografia resolvido
# Trecho de Código: Criptografia 1 (Python)
# # Entrada de dados (frase):
# frase = str(input())

# # primeira passada:
# passo1 = ''
# for j in frase:
#     if j.isalpha():
#         passo1 += chr(ord(j) + 3)
#     else: passo1 += j
# print('Passo1:', passo1)

# # segunda passada:
# passo2 = passo1[::-1]
# print('Passo2:', passo2)

# # terceira passada:
# meio = int(len(passo2) / 2)
# passo3 = passo1[:meio]
# for j in range(meio, len(passo1)):
#     passo3 += chr(ord(passo1[j]) - 1)
# print(passo3)




# Trecho de Código: Criptografia 2 (Python)
# alphabet = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\)^_`abcdefghijklmnopqrstuvwxyz{|}~"

# #Entrada:
# frase = input()

# # primeira passada:
# passo1 = ""
# for i in frase:
#   if i.isalpha():
#     index = alphabet.find(i)
#     index = index + 3
#     index = index % len(alphabet)
#     passo1 = passo1 + alphabet[index]
#   else:
#     passo1 = passo1 + i
# print(f"Passo2: '{passo1}'")

# # segunda passada
# passo2 = passo1[::-1]
# print(f"Passo2: '{passo2}'")

# # terceira passada
# meio = int(len(passo2)/2)
# passo3 = passo2[:meio]
# for i in range(meio, len(passo2)):
#   index = alphabet.find(passo2[i]) - 1
#   if index<0:
#     index = len(alphabet)-1
#   passo3 = passo3 + alphabet[index]
# print(f"Passo3: '{passo3}'")


#
#  DEScriptografia (do exercício anterior)
# Trecho de Código: Descriptografia 1 (Python)
# # Leitura de passo3 (ou continuação do outro código)
# passo3 = input()

# # terceira passada invertida:
# meio = int(len(passo3)/2)
# passo2 = passo3[:meio]
# for i in range(meio, len(passo3)):
#   passo2 += chr(ord(passo3[j]) + 1)
# print(f"Novo Passo2: '{passo2}'")

# # segunda passada invertida:
# passo1 = passo2[::-1]
# print(f"Novo Passo1: '{passo1}'")

# # primeira passada invertida:
# frase = ""
# for i in passo1:
#   letra  = chr(ord(j) - 3)
#   if letra.isalpha():
#     frase += letra
#   else:
#     frase += i
# print(f"Frase descriptografada: '{frase}'")



# Trecho de Código: Descriptografia 2 (Python)
# # Leitura de passo3 (ou continuação do outro código)
# passo3 = input()

# # terceira passada invertida:
# meio = int(len(passo3)/2)
# passo2 = passo3[:meio]
# for i in range(meio, len(passo3)):
#   passo2 += alphabet[alphabet.find(passo3[i]) + 1]
# print(f"Novo Passo2: '{passo2}'")

# # segunda passada invertida:
# passo1 = passo2[::-1]
# print(f"Novo Passo1: '{passo1}'")

# # primeira passada invertida:
# frase = ""
# for i in passo1:
#   letra  = alphabet[alphabet.find(i) - 3]
#   if letra.isalpha():
#     frase += letra
#   else:
#     frase += i
# print(f"Frase descriptografada: '{frase}'")
str1 = 'Universidade do Estado  ' + 'de Santa Catarina'
if 'Catarina' in str1:
    print("está")