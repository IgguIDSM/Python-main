import time;
import threading;

def threadTeste(msg,t):
    print(f'Iniciando: {msg}');
    time.sleep(t);
    print(f'finalizando {msg}');

t1 = threading.Thread(target=threadTeste,args=('Tarefa 1',3,));
t2 = threading.Thread(target=threadTeste,args=('Tarefa 2',2,));

print('Iniciando Threads!');

t1.start();
t2.start();
# aguarda o término
t1.join();
t2.join();

print('Tarefas Finalizadas!');