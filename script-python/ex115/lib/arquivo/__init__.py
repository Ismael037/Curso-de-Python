from ex115.lib.interface import *
def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') #abrir o arquivo1 de texto r = leitura t = texto
        a.close() #fechar
    except FileNotFoundError:#se o arquivo1 nao for encontrado
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+') #w = escreve um arquivo1 t = texto + = cria
        a.close() # fechar
    except:
        print('Houve um ERRO na criação do arquivo1!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo1')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()

def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo1!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados!!')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()