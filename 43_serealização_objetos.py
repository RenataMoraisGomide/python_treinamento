'''# Serealização de objetos é pegar algo que esta em memória e tornar persistênte.
# quando um objeto é transformado, em uma cadeia de bytes e 
# desta forma pode ser manipulado de maneira mais fácil, seja através de transporte pela rede ou salvo no disco.
# para fazer isso, vamos utilizar o pickle que já é nativo do python

import pickle


# Aqui, x que é uma lista(list), está armazenados na memória não sendo persistênte. Eles são apagados e quando serealizamos
# esse objeto, guardamos ele na memória persistênte, trazer ele (retorno) tem que ser igual, o mesmo. Como abrir o arquivo e fechar
#   x = [1, 2, 3, 4]

#dump escreve um objeto em um arquivo
#dumps (s) de string - busca a srt do obj.
# A serealização não é criptografia, é um método que retorna o que era antes
x = [1, 2, 3, 4]
string = pickle.dumps(x)         #b'\x80\x04\x95\r\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04e.'

print(pickle.loads(string))      # Volta a ser lista [1, 2, 3, 4]

'''


import pickle

x = [1, 2, 3, 4]

arq = open('arquivo.pkl', 'wb')

pickle.dump(x, arq)

arq = open('arquivo.pkl', 'rb')
retornou = pickle.load(arq)
print(retornou)


