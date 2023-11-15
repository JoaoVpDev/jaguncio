#agenda telefonica
contatos = {'joao':'98854-9647', 'pai':'99952-2864', 'filipe': '98412-2288'}


contatos[str(input('digite o nome'))] = str(input('digite o telefone'))
print(contatos)

contatos.pop(str(input('Qual ctt vc deseja apgr')), 'erro: contato nao encontrado seu burro')
print(contatos)

busca = contatos[str(input('Qual contatos voces esta prcurando'))]
print(busca)

print(contatos)