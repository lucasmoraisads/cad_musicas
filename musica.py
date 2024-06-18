from flask import Flask, render_template, request, redirect, session

class Musica:
    def __init__(self, nome, cantorGrupoBanda, genero):
        self.nome = nome
        self.cantorBanda = cantorGrupoBanda
        self.genero = genero

musica01 = Musica('vai passa', 'gaab', 'pop')
musica02 = Musica('Flashback', 'Mc paulinho', 'Funk')
musica03 = Musica('Bem melhor', 'Lagum', 'Pop')
    
lista = [musica01, musica02, musica03]


app = Flask(__name__)

app.secret_key = 'aprendendoFlask'

@app.route('/')
def listaMusicas():
    
    
    return render_template('lista_musica.html',
                           titulo = 'Musica', 
                           musicas = lista) 


@app.route('/cadastra')
def cadastraMusica():
    return render_template('cadastra_musica.html')


@app.route('/adicionar', methods=['POST',])
def adicionar_musica():
    nome = request.form['nome']
    cantor = request.form['cantor']
    genero = request.form['genero']
    
    novaMusica = Musica(nome, cantor, genero)
    
    lista.append(novaMusica)

    return redirect('/')

@app.route('/login')
def login():
    
    return render_template('login.html')
    
@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['senha'] == 'admin':
        
        session['usuario_logado'] = request.form['login']
        
        return redirect('/')
    else:
        return redirect('/login')



app.run(debug=True)
