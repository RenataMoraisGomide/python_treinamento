#Exiba todos os números pares entre 1 e 1000 usando o FOR.

#Forma 1 de fazer(não tão convencional)
for i in range(1, 1001):
    if i % 2 == 0:
        print(i)

#Forma 2 de fazer(mais usada e direta com for)

for i in range(2, 1000, 2):
    print(i)

    