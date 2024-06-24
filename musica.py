from flask import Flask, render_template, request, redirect, session, flash, url_for

class Musica:
    def __init__(self, nome, cantorGrupoBanda, genero):
        self.nome = nome
        self.cantorBanda = cantorGrupoBanda
        self.genero = genero

musica01 = Musica('vai passa', 'gaab', 'pop')
musica02 = Musica('Flashback', 'Mc paulinho', 'Funk')
musica03 = Musica('Bem melhor', 'Lagum', 'Pop')
    
lista = [musica01, musica02, musica03]

class Usuario:
    def __ini__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha
        
usuario01 = Usuario("Lucas Morais", "lucas", "admin01")
usuario02 = Usuario("Geo", "Geo", "Geo123")
usuario03 = Usuario("jhessyca", "jhessyca", "12345")

usuarios = {
    usuario01.login : usuario01,
    usuario02.login : usuario02,
    usuario03.login : usuario03  
}

app = Flask(__name__)

app.secret_key = 'aprendendoFlask'

@app.route('/')
def listaMusicas():
    
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))
    
    return render_template('lista_musica.html',
                           titulo = 'Musicas cadastradas', 
                           musicas = lista) 


@app.route('/cadastra')
def cadastraMusica():
    
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('login'))
    
    
    return render_template('cadastra_musica.html',
                           titulo = "Cadastra Musicas")


@app.route('/adicionar', methods=['POST',])
def adicionar_musica():
    nome = request.form['nome']
    cantor = request.form['cantor']
    genero = request.form['genero']
    
    novaMusica = Musica(nome, cantor, genero)
    
    lista.append(novaMusica)

    return redirect(url_for('listaMusicas'))

@app.route('/login')
def login():
    
    return render_template('login.html')
    
@app.route('/autenticar', methods=['POST',])
def autenticar():
    if request.form['login'] in usuarios:
        
        usuarioEncontrado = usuarios[request.form['login']]
        
        if request.form['senha'] == usuarioEncontrado.senha:
        
            session['usuario_logado'] = request.form['login']
        
            flash("Usuario Logado com Sucesso!")
        
            return redirect(url_for('listaMusicas'))
    else:
        flash("Usuario ou Senha invalida!")
        
        return redirect(url_for('login'))

@app.route('/sair')
def sair():
    session ['usuario_logado'] = None
    
    return redirect('/login')

app.run(debug=True)
