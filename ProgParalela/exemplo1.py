import threading;
import time;

#exemplo funcao sem parametros
def func():
    for i in range(3):
        print(f'Executando a Thread: {i}!');
        time.sleep(1);

print('Iniciando Programa!');
threading.Thread(target=func).start();
print('Finalizando Programa!');