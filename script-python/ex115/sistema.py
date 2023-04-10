from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep
arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoas', 'Sair do Sistema'])
    if resposta == 1:
        # opcao de listar o arquivo1 o conteudo de um arquivo1!
        lerArquivo(arq)
    elif resposta == 2:
        # opc de cadastrar uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo')
        break
    else:
        print('\033[31mERRO! Digie uma opção válida!\033[m')
    sleep(2)

