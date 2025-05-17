from flask import Flask, render_template, request;

app = Flask(__name__);
app.debug = True;

@app.route('/')
def index():
    return render_template('index.html');

@app.route('/ola/')
@app.route('/ola/<nome>')
def olaMundo(nome = 'mundo'):
    return render_template('ola.html',nome_recebido = nome);


@app.route('/logar',methods = ['GET','POST'])
def logar():
    if request.method == 'POST':
        return 'Recebeu Post!, Fazer login!';
    else:
        return 'Recebeu Get!, Exibir FORM de login!';


if __name__ == '__main__':
    app.run();
