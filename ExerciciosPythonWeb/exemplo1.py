from flask import Flask;

app = Flask(__name__);

@app.route('/')
def index():
    return 'Página Principal!'

@app.route('/ola/')
@app.route('/ola/<nome>')
def helloWorld(nome = 'Mundo!'):
    return f'Olá {nome}'


if __name__ == '__main__':
    app.run();