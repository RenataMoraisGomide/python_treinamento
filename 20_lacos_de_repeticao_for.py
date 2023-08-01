# Usamos o laço while quando não sabemos quantas vezes o bloco irá se executar
# O laço for usamos quando sabemos quantas vezes o laço será executado
#laço for percorre o espaço que queremos(iteramos) com a range ou outro 
#Temos o for aninhado ou seja, o for em cadeia, um for dentro de outro for


for i in range(0, 100, 2):      #aqui falamos para cada i dentro de 0-100 pulando de 2em2 print i
    print(i)                    #o número 100 fica de fora(ultimo numero)

for i in range(100, 0, -2):     #aqui fazemos a ordem decrescente de i 100-0 pulando de 2 em 2
    print(i)

x = input('Nome: ')             #aqui trocamos o range por x onde o for irá percorrer o nome digitado pela 
for i in x:                     #entrada do input
    print (i)

for i in range(0,3):                #exemplo de for aninhado, ele faz o laçõ até finalizar e volta para
    for j in range (0,3):           #o outro laço
        print(f'i = {i} j = {j}')   #tomar cuidado com a curva de tempo, (complexidade algoritma) aqui seria 3x3 po i ser 3 e j também
                                    #temos que tomar cuidado e tentar evitar em caso de coisas muitos grandes
