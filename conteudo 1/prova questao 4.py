#input
grau = float(input(''))

#processamento
tempo_total = (grau * 240) + 21600  #1 grau equivale a 240 segundos
hora = int(tempo_total // 3600)
minuto = int((tempo_total % 3600) // 60)
segundos = int(tempo_total % 60)

if hora > 23:
    hora -= 24

#manha, tarde, noite ou madrugada
if hora >= 6 and hora <= 11:
    print('Bom Dia!!')
elif hora >= 12 and hora <= 17:
    print('Boa Tarde!!')
elif hora >= 18 and hora <= 23:
    print('Boa Noite!!')
elif hora <= 5:
    print('De Madrugada!!')

#Horas
if hora < 10:
    hora = str(f'0{hora}')

if minuto < 10:
    minuto = str(f'0{minuto}')

if segundos < 10:
    segundos = str(f'0{segundos}')

print(f'{hora}:{minuto}:{segundos}')