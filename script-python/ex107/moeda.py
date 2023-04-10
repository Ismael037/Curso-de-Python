def metade(preço):
    res = preço / 2
    return res


def dobro(preço):
    res = preço * 2
    return res

def aumenta(preço, taxa):
    res = preço + (preço * taxa / 100) #porcentagem
    return res

def diminuir(preço, taxa):
    res = preço - (preço * taxa / 100) #porcentagem
    return res