vaca = [ '  \ ',
         '   \   ^__^ ',
         '    \  (oo)\_______ ',
         '       (__)\       )\/\ ',
         '           ||----w | ',
         '           ||     || ']

def segura_essa_vaca(texto):
    frase = frase_tratada(texto)
    devolvendo = []
    devolvendo.append('/' + linhas_do_balao(max(frase, key=len), True) + '\\')
    for frases in frase:
        devolvendo.append('|' + frases + '|')
    devolvendo.append('\\' + linhas_do_balao(max(frase, key=len), False) + '/')
    for partes in vaca:
        devolvendo.append(partes)
    return devolvendo


def linhas_do_balao(numero, cima=True):
    if cima:
        linha_de_cima = '¯' * len(numero)
        return linha_de_cima
    else:
        linha_de_baixo = '_' * len(numero)
        return linha_de_baixo


def frase_tratada(frases):
        frase = frases.replace('\r', '').split('\n')
        frase = list(map(lambda x: x + " " * (len(max(frase, key=len)) - len(x)), frase))
        return frase


