# Insist on valid input
def insistOnValidNumber():
    x = input("Insira um Número Valido: ");
    try:
        return int(x);
    except ValueError:
        return insistOnValidNumber();
# Prevents Division by 0
def divide(n,divider):
    if divider != 0:
        return n/divider;
    return "Cannot divide by 0!";


n = insistOnValidNumber();
print("Teste :",divide(n,n));