from flask import Flask


app = Flask(__name__)

@app.route('/inicio')
def helo():
    return "<h4>Seja bem Vindo Ao Flask</h4>"

app.run()