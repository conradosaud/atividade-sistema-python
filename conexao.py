import pandas

caminho = "./bd_usuarios.csv"

def conecta():
    usuarios = pandas.read_csv(caminho, sep=";")
    return usuarios
    # with open(caminho, 'r') as banco:
    #     itens = banco.read()
    #     nomes = itens.split(";")[0]
    #     senhas = itens.split(";")[1]

    #     usuarios = [nomes, senhas]
    #     return usuarios
