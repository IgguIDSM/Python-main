import threading
import urllib.request as urllib2;
import time;

start = time.time();
urls = ['http://www.google.com','http://www.Apple.com','http://www.Microsoft.com','http://www.instagram.com'];

def chamaUrl(url):
    req = urllib2.Request(url); # requisitamos a página
    response = urllib2.urlopen(req); # obtemos a resposta
    thePage = response.read(); #lemos a resposta para termos a página
    print(f'{url} Carregado em: {time.time() - start} s'); #Printamos o tempo necessário para o carregamento


threads = [threading.Thread(target=chamaUrl,args=(url,)) for url in urls]; # aqui instanciamos as treads em uma lista

for thread in threads: # para cada thread iniciamos
    thread.start();
for thread in threads: # logo em seguida iteramos novamente para que seja possivel colocálas em ordem de execução usando o .join();
    thread.join();


# após isso deixamos impresso o tempo de execução total
print(f'Elapsed Time: {time.time() - start} s');