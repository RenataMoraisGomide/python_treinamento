#usando lista, while, if

nomes = []
while True:
    nome = input('Digite -1 para sair ou cadastre um nome: ')
    if nome =='-1':
        break
    
    nomes.append(nome)

print(nomes)