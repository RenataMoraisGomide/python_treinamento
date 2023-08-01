# Quando vamos criar um software e receber dados, queremos que esse programa armazene os dados para futuras aplicações
# e não que quando desliguemos o pc seja tudo apagado certo? Pensa se todo dia tivermos que cadastrar usuários de um banco?
# tarefa bem fora do que queremos e in viável para todos. Por isso usamos a armazenamento persistente de dados, que se trata
# em jogarmos esses dados em um HD por ex. uma memória de longo prazo. 
# Para isso usamos banco de dados, banco de dados não relacionais, o sql, o mysql, sqlserver, mongodb etc...abs
# A primeira forma que aprendemos a trabalhar com banco de dados para depois aprendermos as outros é arquivos de texto.
# É como se usassemos o bloco de notas e salvassemos uma lista de nomes, toda vez que quizesse ter acesso a lista
# seria apenas acha-la e abri-la, certo? Então em python é a mesma coisa, vamos usar o open para abrir.
#Ex:

# Vamos criar uma variável arquivo, vou falar que ela é igual a open(função do python que irá abrir um arquivo)
# e vou passar o nome do meu arquivo com sua extensão (.txt) e vou passar como segundo parâmetro como que vou abrir esse
# arquivo, (para escrita (w), leitura (r), adicionar elementos (a), modo binário)
# o (w) write ele escreve e se vc apagar a mensagem e escrever outra ele apaga, já o reade não, ele irá adicionando

#arquivos = open('pessoas.txt', 'w')  #quando rodo essa linha no terminal ele abre no final do curso (CURSO-PYTHONANDO) um arquivo com nome pessoas.txt

#arquivos.write('OLA')       # Aqui ele vai escrever OLA no arquivo pessoas.txt

# Digamos que queremos escrever em input alguns nomes: Ficaria:

arquivo = open('pessoas.txt', 'a')   # 'a' para adicionar elementos

i = 0
while True:
    if i > 4:               #Aqui o 4 é para número de inputs add
        break
    arquivo.write(input('Digite o nome: ') + '\n')   #printar no arquivo pessoas.txt o que foi adicionado no input: renata/rodrigo/georgia/pedro/caio ( o \n para ficar um abaixo do outro)
    i += 1

arquivo.close()         #sempre que criamos esse tipo de arquivo, temos que fecha-lo por questoes variadas como segurança.


#Para evitar essas questões de seguranças, além de erros, usamos o with

#      with open('pessoas.txt', 'r') as arq  

# que diz o seguinte: abra pra mim o arquivos pessoas.txt no modo leitura e utilize como arq
