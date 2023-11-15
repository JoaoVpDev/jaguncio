contato = {'Tiago' : '98854-9647', 'Pai' : '99952-2864', 'Nycolas' : '99966-0026'}

for i in contato:
    contato[i] = '9' + contato[i]   #S1 para: adiconando mais um 9 na frente de todos os contatos

contato = {nome : '9' + contato[nome] for nome in contato} #S2 para: adicionar valores nos contatos

contato['Andre'] = '99926-5136' #adiconando valores ao dicionario

del contato['Andre']  #deletando o contato

contato['Andre'] = 'outro numero' # para alterar 

print(contato.pop('Oliveira', 'contato nao encontrado'))

print(contato)


