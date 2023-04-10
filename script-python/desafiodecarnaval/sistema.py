from desafiodecarnaval.livraria.interface import *
from desafiodecarnaval.livraria.arquivo1 import *
from time import sleep
arq = 'SistemaEstoque.txt'
vendas = 'DadosVendas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
if not arquivoExiste(vendas):
    criarArquivo(vendas)

while True:
    resposta = menu(['Ver produtos cadastrados','Cadastrar novo produtos', 'Cadastrar vendas', 'Ver Vendas' , 'Sair do Sistema'])
    if resposta == 1:
        # opcao de listar o arquivo1 o conteudo de um arquivo1!
        lerArquivoprodutos(arq)
    elif resposta == 2:
        # opc de cadastrar uma novo produto
        cabeçalho('CADASTRO DE PRODUTOS')
        Produto = str(input('Produto: ')).upper()
        codigo = str(input('Código do Produto: '))
        descrição = str(input('Descrição do Produto: '))
        quantidade = leiaInt('Quantidade de Produtos: ')
        valor = leiaDinheiro('Valor do produto: R$ ')
        cadastrarProduto(arq, Produto, codigo, descrição, quantidade, valor)
    elif resposta == 3:
        cabeçalho('CADASTRO DE VENDAS')
        Produto = str(input('Produto Vendido: ')).upper()
        quantidade = leiaInt('Quantidade Vendida: ')
        valor = leiaDinheiro('Valor do produto: R$ ')
        cliente = str(input('Cliente: '))
        vendedor = str(input('Vendedor: '))
        Valortot = valor * quantidade
        cadastrarVendas(vendas, Produto, quantidade, valor, cliente, vendedor, Valortot)
        baixa(arq, quantidade)
    if resposta == 4:
        # opcao de listar o arquivo1 o conteudo de um arquivo1!
        lerArquivovendas(vendas)
    elif resposta == 5:
        cabeçalho('Saindo do sistema... Até logo')
        break
    elif resposta > 5:
        print('\033[31mERRO! Digie uma opção válida!!\033[m')
    sleep(2)

