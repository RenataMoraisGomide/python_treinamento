# Receba um numero e mostre todos os números pares de 0 até o digitado

n1 = int(input('Digite o número inteiro: '))
i = 0
while i <= n1:
    if i % 2 == 0:
        print(i)
    i += 1