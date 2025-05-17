import threading;
import time;


def mens(mens):
    for i in range(3):
        print(f'{i} {mens}');
        time.sleep(1);

print('Iniciando Programa!');
x = threading.Thread(target=mens,args=('Executando?',)); #em argumentos é necessario o ',' após o ultimo, senão dá erro (n sei pq);
x.start();
print('Finalizando Programa!');