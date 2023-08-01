#x = list(range(0,5))                #[0, 1, 2, 3, 4]
#print(x)

#Para saber o index com o valor que lhe pertence:
idades = [3, 5, 27, 87, 43, 5, 62, 23, 36, 50, 69]      
for i in range(0, len(idades)):
    print(idades[i], i)                     

'''3 0
   5 1  
   27 2 
   87 3 
   43 4 
   5 5  
   62 6 
   23 7 
   36 8 
   50 9 
   69 10'''

#Porém essa na é a maneira mais pythonica de se fazer a iteração (percorrer) uma lista
#No python nos temos os interadores: 
for i in idades:
    print(i)

#ENUMERATE = a forma mais pythonica de se iterar um objeto da lista
#Irá mostrar o index com o valor 
x = list(enumerate(idades))
print(x)    #[(0, 3), (1, 5), (2, 27), (3, 87), (4, 43), (5, 5), (6, 62), (7, 23), (8, 36), (9, 50), (10, 69)]

print(type(x))