#x²
from math import sqrt;
def pegaDados(coef):
    return eval(input(f"Insira o Coeficiente {coef}: "));
# Bss
a = pegaDados("a");
b = pegaDados("b");
c = pegaDados("c");
#Calcula o delta
def calcDelta(a,b,c):
    delta = (b*b) - 4*a*c;
    return delta;

def calcBaskhara(b,delta,a):
    if delta < 0:
        print("Não é possivel calcular raiz de número Negativo!");
    if delta == 0:
        x = (-b/2*a);
        return x;
    if delta > 0:
        x1 = (-b + sqrt(delta))/2*a;
        x2 = (-b - sqrt(delta))/2*a;
        return x1,x2;


print(calcBaskhara(b,calcDelta(a,b,c),a));