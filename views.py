from flask import render_template, request
from vacaweb import app
import urllib.parse
from vacaservice import segura_essa_vaca, linhas_do_balao, frase_tratada

TEMPLATE_PRINCIPAL = 'principal.html'


@app.route('/')
def pag_upload():
    return render_template('upvaca.html', vaca=segura_essa_vaca('Frase ou arquivo.txt'))


@app.route('/', methods=['POST'])
def upload_file():
    frase = request.form.get('frase')
    arquivo = request.files['file']
    if arquivo.filename != '':
        arquivo = request.files['file']
        frase = urllib.parse.quote(str(arquivo.read(), 'utf-8'))
        frase = urllib.parse.unquote(frase)
    return render_template(TEMPLATE_PRINCIPAL, frase=segura_essa_vaca(frase),
                               linha_de_baixo=linhas_do_balao(max(frase_tratada(frase), key=len), False),
                               linha_de_cima=linhas_do_balao(max(frase_tratada(frase), key=len), True))
