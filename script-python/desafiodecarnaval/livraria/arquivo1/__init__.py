from desafiodecarnaval.livraria.interface import *
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


def lerArquivoprodutos(Produto):
    try:
        a = open(Produto, 'rt')
    except:
        print('Erro ao ler o arquivo1')
    else:
        cabeçalho('PRODUTOS CADASTRADOS')
        print(f'{"CODIGO":<8}|{"PRODUTO":<20}|{"DESCRIÇÃO":<50}|{"QUANT.":<5}|{"VALOR":<5}')
        for l in a:
            l = l.replace('\n', '')
            print(f'{l}')
    finally:
        a.close()


def lerArquivovendas(Produto):
    try:
        a = open(Produto, 'rt')
    except:
        print('Erro ao ler o arquivo1')
    else:
        cabeçalho('VENDAS CADASTRADASS')
        print(f'{"PRODUTOS":<20}|{"QUANT.":<10}|{"VALOR UNI.":<10}|{"CLIENTE":<30}|{"VENDEDOR":<30}|{"VALOR TOTAL":<10}')
        for l in a:
            l = l.replace('\n', '')
            print(f'{l}')
    finally:
        a.close()

def cadastrarProduto(arq, Produto='desconhecido', codigo=0, descrição='Sem descrição', quantidade=0, valor=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo1!')
    else:
        try:
            a.write(f'{codigo:<8}|{Produto:<20}|{descrição:<50}|{quantidade:<5}|{valor:.2f} R$\n')
        except:
            print('Houve um erro na hora de escrever os dados!!')
        else:
            print(f'Novo registro do produto {Produto} adicionado.')
            a.close()


def cadastrarVendas(arq, Produto='desconhecido', quantidade=0, valor=0, cliente='Sem informe', vendedor='Sem informe', valortot=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo1!')
    else:
        try:
            valor = (f'{valor:.2f}')
            a.write(f'{Produto:<20}|{quantidade:<10}|{valor:<10} R$|{cliente:<30}|{vendedor:<30}|{valortot:.2f} R$\n')
        except:
            print('Houve um erro na hora de escrever os dados!!')
        else:
            print(f'Nova venda registrada com sucesso.')
            a.close()


def baixa(Produto, quantidade):
    try:
        a = open(Produto, 'rt')
    except:
        print('Erro ao ler o arquivo1')
    else:
        for l in a:
            b = l[81:86]
            n = int(b)
            s = n - quantidade


            print(f'{s}aaa')
            #a.write(in l[81:86]} == s)
    finally:
        a.close()





