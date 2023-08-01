# Estrutura de dados que parecem com as lista, podem armazenar mais de um valor porém ele não armazena um 
# index e sim uma chave. Cada objeto pode ser armazenada com uma chave usando { : }
#ex: chave e valor do determinado index
x = {'nome': 'Renata' , 'idade': 36}
# Para acessar um index determinado chamamos pelo nome que demos ex:
print(x ['nome'])   #Renata

# Para auterarmos um valor fazemos igual nas listas:
x['nome'] = "RE"
print(x)            #{'nome': 'RE', 'idade': 36}

# Você pode usar uma lista dentro do dicionário ex:
x = {'nomes': [], 'idade': 21} #aqui temos um dicionário com um index que é uma lista[] que esta vazia.
#podemos portanto usar as funções de lista dentro da lista ex:
x['nomes'].append('Caio Sampaio')  #a função append irá acrescentar nomes dentro da lista nomes[]
x['nomes'].append('Lara')

# Dicionário .update 
# Quando criamos um dicionário e queremos atualizar com algum dado podemos usar o .update
#ex: 
pessoas = {'Nome': 'Renata', 'idade': 36}

pessoas.update({'altura': 166})         #o update irá pegar a altura : 166 e adicionar ao dicionário pessoas

print(pessoas)