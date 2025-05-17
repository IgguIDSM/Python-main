#programa para cálculo de IMC
peso = eval(input("Informe o seu peso em kg: "));
altura = eval(input("Informe sua altura em metros: "));
imc = peso/(altura*altura);
print(f"O Seu Indice de Massa Corporal é: {imc}");