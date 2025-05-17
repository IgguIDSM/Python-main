from flask import Flask;

app = Flask(__name__);



# como pode ver nos exemplos abaixo, o flask consegue carregar html diretamente, mas obvioamente não é uma boa prática!

@app.route('/')
def index():
    boasVindas = '<h1>Olá, Programadores!</h1>';
    link = '<p><a href = "user/Usuario">Clique Aqui!</a></p>';
    return boasVindas + link;

@app.route('/user/')
@app.route('/user/<nome>')
def helloWorld(nome = 'Usuário!'):
    pers = f'<h1>Olá, {nome}!</h1>';
    instruc = '<p>Altere o Nome no <em>endereço do browser</em> e recarregue a página.</p>'
    return pers + instruc;


if __name__ == '__main__':
    app.run();