#Receba um número e forme sua tabuada

n1 = int(input('Digite o número que quer saber a tabuada: '))

i=0  # O i será o número por qual começará o laço

while i <= 10:
    print(f'{n1} X {i} = {n1*i}')
    i += 1

