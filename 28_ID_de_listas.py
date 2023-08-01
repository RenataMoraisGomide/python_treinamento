# Referência de memória
# Cada variável é armazenada em um local, tendo cada uma um ID


x = 2
y = x
y = 3               #quando mudamos aqui a variável y ela passou a valer 3

print(id(x))        # id(endereço da memória) de x = 140736165962568
print(id(y))        # id(endereço da memória) de y = 140736165962600

print(hex(id(x)))   #hex = hexadecimal de x = 0x7fffb12de348
print(hex(id(y)))   #hex = hexadecimal de y = 0x7fffb12de368

x = [1, 2, 3]       #aqui demos valores a lista x
y = x               #aqui dizemos que a lista y será igual a lista x
y[0] = 0            #aqui mudamos o index 0 da lista y para o valor 0

print(x)            #[0, 2, 3] o valor da lista x tb é alterado pois a lista Y é a mesma coisa que a lista x
print(y)            #[0, 2, 3] então muda-se tanto na lista x quanto na y pois são duas variáveis que apontam o memso valor


#   Para conseguirmos alterar um item da lista y sem alterar o mesmo da lista x podemos fazer uma cópia da lista
# usando o .copy()

y = x.copy()
y[1] = 9
print(x)            #[0, 2, 3]
print(y)            #[0, 9, 3] alteramos apenas o valor em lista y e agora cada um tem um endereço diferente pois fizemos uma cópia dele no endereço de memória















