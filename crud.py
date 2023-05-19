from conexao import conecta
con = conecta()

# Retorna um usuário do banco se ele existir
def buscaNome( nome ):
    for nome_bd in con['nome']:
        if nome_bd == nome:
            return True
    
    return False

def buscaSenha( senha ):
    for senha_bd in con['senha']:
        if senha_bd == senha:
            return True
    
    return False

# Mostra todos os usuários do banco
def buscaTodos():
    global con
    # atualizar o banco
    con = conecta()
    print(con) # os Pandas já monta o dataframe

# Adiciona um novo usuário ao final da lista do banco
def insere( nome, senha ):

    if len(nome) < 3:
        print("Nome do item muito curto")
        return False
    
    #nome = nome.capitalize()
    with open("./bd_usuarios.csv", 'a') as banco:
        banco.write( "\n"+nome+";"+senha )

    return True

# Altera um usuário do banco, usando o nome como índice
def altera( nome, senha ):
    
    indice = int(indice)

    if len(con) == 0 or len( con ) < indice - 1:
        print("Esse índice é maior do que a lista...")
        return

    con[indice-1] = con.capitalize()

    print("Item alterado com sucesso!")

# Remove um usuario do banco usando o nome dele
def remove( nome ):

    for i in con:
        if i == nome:
            con.remove(nome)
            print("Item removido da lista!")
            return

    print("Este item não existe na lista")
