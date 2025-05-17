l = [1,2,3,4,5,6,7,8,9];
# Verifica se o Input é um número!
def verifyInput(n):
    while n is not int:
        try:
            val = int(n);
            return val;
        except:
            return 0;
# Pode colocar qualquer sequencia de valores acima que ele acha o menor.
def getAllPairsSum(t):
    soma = 0;
    for i in t:
        if i % 2 == 0:
            soma += i;
    return soma;
# Retorna se o número é primo;
def isPrimo(n):
    count = 1;
    while count < (n-1):
        count += 1;
        if n % count == 0:
            return False;
    return True;
# Retorna todos os numeros primos de 1 até o intervalo designdado pelo usuário;
def getPrimosInRange(n):
    count = 1;
    l = [];
    while count < n:
        primo = isPrimo(count);
        if primo == True:
            l.insert(count,count);
            print(f"O Número: {count} é primo!");
        count += 1;
    return l;
# Retorna um Valor Fatorial de um numero qualquer
def getFatorial(n):
    l = n;
    while n > 1:
        n -= 1; l += l * (n-1);
    return l;
# Retorna o menor valor dentro de uma tabela (Aceita somente tabela com numeros!);
def getMenorValor(t):
    menor = t[len(t) - 1];
    for i in t:
        if i < menor:
            menor = i;
    return menor;

# Pega o menor valor pela função
inp = input("Insira um valor: ");
tt = verifyInput(inp);
if tt != 0:
    print(f"Lista de Primos Para {tt}:")
    getPrimosInRange(tt);
else:
    print(f"Somente Números!!!");