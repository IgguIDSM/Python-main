veiculos = ['aviao','carro','navio','ônibus'];


#altera a lista existente
#desabilitada por conta de redundância
# for i in range(len(veiculos)):
#     veiculos[i] = veiculos[i].upper();
# print(veiculos);

#Cria uma nova lista para que contenha os valores maiúsculos.
vM = list(map(lambda x: str.upper(x),veiculos));
print(vM);


#imprime somente números pares a partir de prog funcional
numeros = [0,1,1,2,3,5,8,13,21,34];
                                                 # usamos o filter, que é usado para filtrar elementos baseado em uma verificação (verificações mais complexas exigem);
                                                 # uma função a parte para tal; 
nL = list(filter(lambda x: x % 2 == 0,numeros)); # nesse caso o filtro usa a função lambda para retornar somente numeros que divididos por 2 tenham resto 0;
                                                 # sendo assim classificados como pares;

print(nL);


#Arrendondar valores e manter na mesma ordem da lista precisão
lNumeros = [9.56783,7.57568,3.00914,6.2321];
lPrecisao = [2,2,3,3]; #os valores acima devem ser arredondados baseados no numero de digitos da lista de precisão para cada elemento da primeira;

nP = list(map(lambda x,y: round(x,y), lNumeros,lPrecisao)); #neste caso usamos a função map para mapear cada elemento da lista e arredondar para o valor mais próximo
                                                                    # baseado na lista de precisão, ou seja, o numero de casas desejado.
                                                                    #em seguida transformamos em uma lista.

print(nP)


# Somar todos os valores presentes na lista abaixo

numero = [1,2,3,4,5,6,7,8,9,10];

print(sum(numero)); # ridículo KKKKKKKKKKKKKKKKK