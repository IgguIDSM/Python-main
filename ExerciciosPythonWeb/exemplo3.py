from flask import Flask;

app = Flask(__name__);



# como pode ver nos exemplos abaixo, o flask consegue carregar html diretamente, mas obvioamente não é uma boa prática!

@app.route('/')
def index():
    boasVindas = '<h1>Olá, Programadores!</h1>';
    msg = '<p>Entre com dois numeros</p>';
    return boasVindas + msg;   

@app.route('/somar/')
@app.route('/somar/<n1>/<n2>')
def helloWorld(n1 = 0,n2 = 0):
    pers = f'<h1>{int(n1)+int(n2)}</h1>';
    return pers;


if __name__ == '__main__':
    app.run();