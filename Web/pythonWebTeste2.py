from flask import Flask;

app = Flask(__name__);

@app.route('/')
def index():
    return 'Página Principal';

@app.route('/pg1')
def pagina1():
    return 'Essa é a Página 1!';

@app.route('/pg2')
def pagina2():
    return 'Essa é a Página 2!\nnão existe pagina 3 e nem adiante KKKKKKKKKKKKK';

@app.route('/pg/')
@app.route('/pg/<nome>')
def paginaMagica(nome = 'NotDefined'):
    return f'Bem vindo a Página {nome}, O que você colocar após a ultima barra existirá!'

if __name__ == '__main__':
    app.run();