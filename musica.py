from flask import Flask, render_template

class Musica:
    def __init__(self, nome, cantorGrupoBanda, genero):
        self.nome = nome
        self.cantorBanda = cantorGrupoBanda
        self.genero = genero


app = Flask(__name__)


@app.route('/musicas')
def listaMusicas():
    
    musica01 = Musica('vai passa', 'gaab', 'pop')
    musica02 = Musica('Flashback', 'Mc paulinho', 'Funk')
    musica03 = Musica('Bem melhor', 'Lagum', 'Pop')
    
    lista = [musica01, musica02, musica03]
    
    return render_template('lista_musica.html',
                           titulo = 'Musica', 
                           musicas = lista) 


@app.route('/cadastra')
def cadastraMusica():
    return render_template('cadastra_musica.html')


app.run(debug=True)
