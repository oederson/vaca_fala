from flask import render_template, request
from vacaweb import app
import urllib.parse


TEMPLATE_PRINCIPAL = 'principal.html'


def linhas_do_balao(numero, cima=True):
    if cima:
        linha_de_cima = '¯' * len(numero)
        return linha_de_cima
    else:
        linha_de_baixo = '_' * len(numero)
        return linha_de_baixo


def frase_tratada(frases, arquivo=True):
    if arquivo:
        frase = frases.replace('\r', '').split('\n')
        frase = list(map(lambda x: x + " " * (len(max(frase, key=len)) - len(x)), frase))
        return frase
    else:
        frase = frases.replace('\r', '').split('\n')
        return frase


@app.route('/')
def pag_upload():
    return render_template('upvaca.html')


@app.route('/', methods=['POST'])
def upload_file():
    frase = request.form.get('frase')
    arquivo = request.files['file']
    if arquivo.filename != '':
        arquivo = request.files['file']
        frase = urllib.parse.quote(str(arquivo.read(), 'utf-8'))
        frase = urllib.parse.unquote(frase)
        return render_template(TEMPLATE_PRINCIPAL, frase=frase_tratada(frase, True),
                               linha_de_baixo=linhas_do_balao(max(frase_tratada(frase), key=len), False),
                               linha_de_cima=linhas_do_balao(max(frase_tratada(frase), key=len), True))
    else:
        return render_template(TEMPLATE_PRINCIPAL, frase=frase_tratada(frase, False),
                               linha_de_baixo=linhas_do_balao(max(frase_tratada(frase), key=len), False),
                               linha_de_cima=linhas_do_balao(max(frase_tratada(frase), key=len), True))