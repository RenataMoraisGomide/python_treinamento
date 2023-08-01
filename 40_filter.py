# Também faz parte da programação funcional, como lambda. 
# Como o nome já diz ele faz um filtro para facilitar e diminuir o código.
# Ao invés de usar o for e gerar umas 3 ou 4 linhas só para ver por ex. pessoas maiores de 18 anos usamos o filter.
# Pode ser usado com várias estruturas e passando vários operadores lógicos 
#Ex:

x = [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
x = list(filter(lambda x: x < 18, x))               # convertemos para list para que mostre o resultado
print(x)                                            # [12, 13, 14, 15, 16, 17]


