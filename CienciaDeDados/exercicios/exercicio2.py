from sklearn.datasets import load_digits;

digitos = load_digits(); # carregamos a biblioteca de digitos teste para uso de trinamento

#Existem 1797 imagens, sendo que cada uma tem uma dimensão 8x8 = 64;
print('Shape dos dados de imagem :{}'.format(digitos.data.shape)); # type: ignore
#Apresentar o total de dados rotulados com inteiros de 0 a 9;
print('Shape dos dados Rotulados :{}'.format(digitos.target.shape));# type: ignore

#agora vamos visualizar os dados.
import numpy as np; #importamos a biblioteca numpy para facilidade.
import matplotlib.pyplot as plt; # importamos a biblioteca matplotlib para visualizar os dados fornecidos de maneira gráfica.

plt.figure(figsize=(14,4));

for index, (imagem,rotulo) in enumerate(zip(digitos.data[0:10],digitos.target[0:10])): #type: ignore
                            # sinceramente não faço a menor ideia do que esse trecho de código faz....
    plt.subplot(1,10,index+1);
    plt.imshow(np.reshape(imagem,(8,8)),cmap = plt.cm.gray); #type: ignore
    plt.title(f'Treinamento: {rotulo}',fontsize = 5);

# O comando abaixo é para visualizar as imagens geradas.
plt.show(); # <-- habilite esse comando para ver as figuras geradas no código acima;

# a partir de agora usaremos regressão logística para treinar o modelo
from sklearn.model_selection import train_test_split;
# Criamos os parametros para treinamento....
x_treino, x_teste, y_treino, y_teste = train_test_split(digitos.data,digitos.target,test_size=0.25,random_state=0); #type:ignore

from sklearn.linear_model import LogisticRegression;
from sklearn.pipeline import Pipeline, make_pipeline;
from sklearn.preprocessing import StandardScaler;
# a partir daqui eu não sei o que está acontecendo...
pipe = make_pipeline(StandardScaler(),LogisticRegression());

pipe.fit(x_treino,y_treino);

Pipeline(steps=[('standardscaler',StandardScaler()),('logisticregression',LogisticRegression())]);

# agora usamos o modelo treinado para fazer classificação de dados

previsto = pipe.predict(x_teste[0].reshape(1,-1));
real = y_teste[0];
print(f'Previsto: {previsto[0]} | Real: {real}');


# resumo, tendi foi nada.
