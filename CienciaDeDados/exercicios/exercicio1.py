# neste exemplo é demonstrado como utilizamos dados para gerar um modelo, e a partir deste modelo, gerar um gráfico resposta e predição de resultados
# além de demonstrar com maior clareza a distribuição de dados.



import numpy as np;
from sklearn.linear_model import LinearRegression;
import matplotlib.pyplot as plt;

x = np.array([5,10,15,20,25,30]).reshape((-1,1));
y = np.array([6,12,14,23,27,32]);

model = LinearRegression().fit(x,y);

# Nesta área vamos predizer uma resposta e imprimí-la;
yPred = model.predict(x);
print(f'Dados do teste: {y}');
print(f'Dados da Predição: {yPred}');

#aqui, usamos o matplotlib para montar um gráfico, facilitando a visualização;

plt.scatter(x,y,color='blue'); # com a função scatter, criamos um gráfico de dispersão baseado nos dados fornecidos.
plt.plot(x,y,color='red'); # com a função plot criamos um gráfico de linhas, baseados nos dados de X e y;
plt.plot(x,yPred,color='green'); # mais uma vez com a função plot, criamos uma reta para demonstrar o crescimento linear.
plt.legend(['Predição','Real','Crescimento']); # Adicionamos legendas aos Itens do gráfico para melhor compreensão;
plt.show();