from flask import Flask, render_template


app = Flask(__name__)


@app.route('/musicas')
def listaMusicas():
    return render_template('lista_musica.html',
                           titulo = 'Musica') 


app.run()