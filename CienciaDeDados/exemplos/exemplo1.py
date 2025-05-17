import matplotlib.pyplot as plt;
import numpy as np;
from sklearn.linear_model import LinearRegression;
import pandas;
#pré processamento
#coleta e integração
arquivo = pandas.read_csv('CienciaDeDados/exemplos/casos.csv');

anos = arquivo[['ano']];
casos = arquivo[['casos']];

#Mineração

regr = LinearRegression();

regr.fit( X = anos, y = casos);

anoFuturo = np.array([[2018]]);

casos2018 = regr.predict(anoFuturo);

print(f'Casos previstos para 2018: {int(casos2018[0,0])}');

#pós processamento (esse pós pricessamento é para mostrar ao usuário final os dados coletados de forma mais amigável)

plt.scatter(anos,casos,color='black');
plt.scatter(anoFuturo,casos2018,color='red');
plt.plot(anos,regr.predict(anos),color='blue');

plt.xlabel('Anos');
plt.ylabel('Casos de Dengue');
plt.xticks([2018]);
plt.yticks([int(casos2018[0,0])]);

plt.show();