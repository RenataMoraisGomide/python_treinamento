# Operadores logicos and, or, not
# and só retorna true se for tudo true
# or se um único for verdadeiro ele retorna True
# not tras a inversão do resultado

operador = True and True
print(operador)
#Resultado True

operador = 5 == 5 and 3 < 2
print(operador)
#Resultado False

operador = not ( (5 == 7 or 3 > 2) and (2 == 2 or 5 < 5) )
print(operador)
#Resultado False