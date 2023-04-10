def metade(preço=0, formato=False):
    '''

    :param preço: valor de p
    :param formato: formatação em Real
    :return: retorno da metade do valor
    '''
    res = preço / 2
    return res if not formato else moeda(res)


def dobro(preço=0, formato=False):
    '''

    :param preço: valor de p
    :param formato: formatação em Real
    :return: retorno da dobro do valor
    '''
    res = preço * 2
    return res if not formato else moeda(res)

def aumenta(preço=0, taxa=0, formato=False):
    '''

    :param preço: valor de p
    :param taxa: pocentagem
    :param formato: formatação em Real
    :return: retorno do valor em 10% a mais
    '''
    res = preço + (preço * taxa / 100) #porcentagem
    return res if formato is False else moeda(res)

def diminuir(preço=0, taxa=0, formato=False):
    '''

    :param preço: valor de p
    :param taxa: pocentagem
    :param formato: formatação em Real
    :return: retorno do valor em 13% a menos
    '''
    res = preço - (preço * taxa / 100) #porcentagem
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    '''

    :param preço: valor de p
    :param moeda:
    :return:
    '''
    return f'{moeda}{preço:.2f}'.replace('.',',')
