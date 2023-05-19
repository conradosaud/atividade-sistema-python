# AUTENTICAÇÃO E CADASTRO DE USUÁRIOS

from crud import *

usuario_autenticado = False

def main():
    
    global usuario_autenticado

    # Verifica se o usuário NÃO está autenticado
    # Caso não esteja, pede para ele se autenticar
    if usuario_autenticado == False:
        # Valida e autentica o usuário
        usuario_autenticado = autentica()
        if usuario_autenticado == False:
            print("Verifique os dados e tente novamente...")
            main()
        else:
            print("Usuário validado com sucesso!")

    # Oferece as opções ao usuário
    resposta = mostraOpcoes()
    
    # Identifica a opção de sair do sistema
    if resposta < 1 or resposta > 4:
        print("Você foi saiu do sistema!")
        usuario_autenticado = False

    # Listagem de usuários
    if resposta == 1:
        buscaTodos()

    # Opção de cadastro de usuário
    if resposta == 2:
        nome = input("Digite o nome do novo usuário: ")
        senha = input("Digite a senha do novo usuário: ")
        resultado = insere( nome, senha )
        if resultado == False:
            print("O nome está inválido...")
        else:
            print("Usuário cadastrado com sucesso!")
    
    main()

# Processo de autenticação do usuário
def autentica():

    # Valida o nome do usuário
    nome = input("Para acessar o sistema, digite seu nome: ")
    usuario_valido = buscaNome( nome )

    if usuario_valido == False:
        # print("O usuário está incorreto")
        return False
    
    # Valida a senha
    senha = input("Digite a senha: ")

    senha_valida = buscaSenha( senha )
    if senha_valida == False:
        # print("A senha está incorreta")
        return False
    
    # Se chegar até aqui, sem ser interrompido por um False, recebe um True validado
    return True

def mostraOpcoes():
    print("Opções disponíveis no sistema:")
    print("1 - Listar usuários")
    print("2 - Cadastrar novo usuário")
    print("3 - Alterar um usuário")
    print("4 - Deletar usuário")
    print("5 - Sair do sistema")
    resposta = int( input("Escolha uma opção: ") )
    return resposta

main()
