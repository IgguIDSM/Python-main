import threading;
import time;

#sincronização de threads!


ls = [];

def contador1(n):
    for i in range(1, n + 1):
        print(i);
        ls.append(i);
        time.sleep(0.4);

def contador2(n):
    for i in range(6,n+1):
        print(i);
        ls.append(i);
        time.sleep(0.5);


#ao utilizar o .join() garante que o próximo passo só seja executado após o termino da execução da thread, isso garante que a função que a thread esteja executando, termine antes de seguir com o processo.



x = threading.Thread(target=contador1,args=(5,));
x.start();
x.join(); # com isso executamos primeiro a thread inicial para depois seguir com a execução da segunda.

y = threading.Thread(target=contador2,args=(10,));
y.start();

y.join();

print(ls);