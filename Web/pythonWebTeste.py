from flask import Flask;

app = Flask(__name__);

@app.route('/pg1') # esse '/' representa a rota, ou seja, o que vem depois da barra representa a página que será carregada.
def func1():
    return 'Te Amo Vida <3 :D';

@app.route('/pg2')
def func2():
    return 'Como pode ver, o que vem depois da barra dita em qual rota você será direcionado!';

@app.route('/pg3')
def func3():
    return 'assim como essa pagina também está em uma rota diferente!';



if __name__ == '__main__':
    app.run();