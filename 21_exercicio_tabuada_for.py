#receba um número e mostra a tabuada completa dele usando for

t = int(input('digite o número que quer a tabuada: '))
for i in range(1,11): 
    print(f'{t} x {i} = {t*i}')



#Mostre a tabuada completa de todos os números entre 1 e 10

for i in range(1, 11):
    print(f'==========[TABUADA {i}]==========')    #só para organizar 
    for j in range(1,11):
        print(f'{i} x {j} == {i*j}')
