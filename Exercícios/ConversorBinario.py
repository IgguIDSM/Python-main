numero_decimal = 314;
#Retorna a divisão inteira e o quociente em string.
def divide(n,d):
  return n//d,str(n%d);
# Converte para binário;
def convertToBinary(n):
  div,resto = divide(n,2);
  while div > 0:
    div,r = divide(div,2);
    resto += r;
  return resto[::-1];
#imprime o Resultado 
print(convertToBinary(numero_decimal));