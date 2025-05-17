from copy import deepcopy
# entrada de dados.
conjuntoInicial = [1,2,3];

# cálculos intermediários.

# Obs a função abaixo funciona para qualquer conjunto, independente do tipo de valor que contenha. (ex: pode ser um conjunto do tipo : [1,'a',549,'abacate',['sou','um','conjunto'],0.6754] ).
def doCalc(conjunto): # a função recebe um conjunto como argumento.

    l = [[]]; # Iniciamos um novo array contendo um array vazio já de início.

    for n in conjunto: # para cada número no conjunto inicial..
        l.append([n]); # adicionamos esse número ao array criado acima.
    
    for i in conjunto[::-1]: # agora, para cada número no conjunto inicial invertido ([::-1])...
        r = deepcopy(conjunto); # criamos uma deepCopy para que seja possivel manipular o conjunto sem afetar o original.
        r.remove(i); # removemos o numero iterado da cópia.
        l.append(r); # adicionamos o array resultante (r) ao array inicialmente criado.
    
    l.append(conjunto); # após todo o processo adicionamos o próprio conjunto no final do array.

    return l;# retornamos a lista.

#saída de dados
conjuntoResultante = doCalc(conjuntoInicial);
print(conjuntoResultante);

