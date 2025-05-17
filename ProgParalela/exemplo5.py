import time;
import threading;

def cubo(n,wait):
    print(f'Iniciando cálculo Cubo de {n}');
    print(f'O Cubo de {n} é : {n**3}'); # o simbolo ** significa elevado (em c# é ^, mas td bem kkkkkkk)
    time.sleep(wait);
    print(f'Finalizado o cubo de ({n})');
def quad(n,wait):
    print(f'Iniciando cálculo Quadrado de {n}');
    print(f"O Quadrado de {n} é : {n**2}");
    time.sleep(wait);
    print(f'Finalizado o quadrado de ({n})');


t1 = threading.Thread(target=cubo,args=(4,3,));
t2 = threading.Thread(target=quad,args=(10,2,));

print('Tarefa Inicializada!');
t1.start();
t2.start();
#
t1.join();
t2.join();
print('Tarefa Finalizada!');