from flask import render_template, request, redirect
from vacaweb import app
import urllib.parse

TEMPLATE_PRINCIPAL = 'principal.html'


@app.route('/')
def pag_upload():
    return render_template('upvaca.html')


@app.route('/', methods=['POST'])
def upload_file():
    arquivo = request.files['file']
    if arquivo.filename != '':
        frase = urllib.parse.quote(str(arquivo.read(), 'utf-8'))
        return redirect(f'/vacafala/{frase}')


@app.route('/vacafala/<frase>')
def fala(frase):
    frase = frase.replace('\r', '').split('\n')
    maior_frase_da_lista = max(frase, key=len)
    frase = list(map(lambda x: x + " " * (len(maior_frase_da_lista) - len(x)), frase))
    linha_de_baixo = '_'*len(maior_frase_da_lista)
    linha_de_cima = '¯'*len(maior_frase_da_lista)
    return render_template(TEMPLATE_PRINCIPAL, frase=frase, linha_de_baixo=linha_de_baixo, linha_de_cima=linha_de_cima)






