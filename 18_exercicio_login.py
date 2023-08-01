# Defina um usuário e senha e depois verifique se o login é válido


USUARIO = "renata"
SENHA = "minha_senha123"

while True:
    usuario_login = input('Digite o login: ')
    senha_login = input('Digite sua senha: ')

    if usuario_login == USUARIO and senha_login == SENHA:
        print('Login efetuado com sucesso!')
        break
    else:
        print ('Usuário ou senha inválido, favor digitar novamente.')
    