# Chave = i  Objeto = j 
# for i, j in pessoas.items():
# .items() ele itera (mostra chave e valor do dicionário)
# .keys() mostra apenas as chaves
# .values() mostra apenas os valores

pessoas = {'nome': 'Renata Morais', 'idade': 36, 'altura': 167}

for chave, valor in pessoas.items(): 
    print(f'chave = {chave} valor = {valor}')