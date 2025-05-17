from collections import OrderedDict
from faker import Faker;
import numpy as np;
import matplotlib.pyplot as plt;
from sklearn.linear_model import LinearRegression;
# Imports ^^^^^^^^^^^^^^

#Inicio da classe Dispesas
class Dispesas:
    def __init__(self,dispesas = OrderedDict({})):
        self.dispesas = dispesas;
    #
    def getDispesas(self):
        return self.dispesas;
    #
    def addDispesas(self,nome,tabela = OrderedDict({})):
        if len(tabela) > 0:
            self.dispesas[nome] = tabela;
        else:
            print('Não é possivel adicionar uma tabela de dispesas vazia!');
    #
    def addDispesa(self,nome,dia,valor):
        if self.dispesas[nome]:
            self.dispesas[nome][dia] = valor;
        else:
            self.dispesas[nome] = OrderedDict({dia : valor});
    #
    def removeDispesas(self,nome):
        self.dispesas[nome].clear();
#Fim Classe Dispesas ---------------------------------------------------

#Inicio classe Gráfica
class Grafica:
    def __init__(self):
        self.regr = LinearRegression();
    #
    #a função abaixo retorna uma array no formato [x,y]
    def __Reshape__(self,dispesa = OrderedDict({})):
        mother = [[],[]];
        if len(dispesa) > 0:
            for dia in dispesa:
                mother[0].append(dia);
                mother[1].append(dispesa[dia]);
            return np.array(mother);
        else:
            print('Não é possivel Remodelar um dicionário vazio!');
            return np.array([]);
    #
    def getKeys(self,dictionary):
        keys = [];
        for k in dictionary.keys():
            keys.append(k);
        return keys;
    #
    def getRegression(self,target):
        if target:
            mother = self.__Reshape__(target);
            model = self.regr.fit(mother[0].reshape(-1,1),mother[1]);
            predict = model.predict(mother[0].reshape(-1,1));
            return predict,mother;
        return [],[];
    #
    def showDispesasGrafica(self,dispesas = OrderedDict({}),ColorTable = {}):
        if len(dispesas) > 0 and len(ColorTable) > 0:
            for tipo in dispesas:
                #pega todos os dados necessários
                _,shaped_data = self.getRegression(dispesas[tipo]);
                #display dos dados
                try:
                    plt.plot(shaped_data[0],shaped_data[1],color = ColorTable[tipo],marker='o',linestyle='-');
                except:
                    plt.plot(shaped_data[0],shaped_data[1],color = 'blue',marker='o',linestyle='-');
                    print(f'Não foi possível encontrar uma cor para o gráfico: ({tipo}), Setado como azul por padrão.');
                    print(f'Por acaso esqueceu de referenciar a cor na ColorTable?');
            #
            keys = self.getKeys(dispesas);
            plt.legend(keys);
            plt.title('Visão Geral');
            plt.xlabel('Dia');
            plt.ylabel('Dispesa em R$');
            plt.show();
    #
    def showDispesaEmGraficoAlvo(self,dispesas,ColorTable = {},tipo = ''):
        if dispesas[tipo]:
            #pega os dados para apresentar no gráfico alvo
            linear_data,shaped_data = self.getRegression(dispesas[tipo]);
            #display dos dados
            try:
                plt.plot(shaped_data[0],shaped_data[1],color=ColorTable[tipo],marker='o',linestyle='-');
            except:
                plt.plot(shaped_data[0],shaped_data[1],color='blue',marker='o',linestyle='-');
                print(f'Não foi possível encontrar uma cor para o gráfico: ({tipo}), Setado como azul por padrão.');
                print(f'Por acaso esqueceu de referenciar a cor na ColorTable?');
            #
            plt.plot(shaped_data[0],linear_data,color='black',linestyle='-');
            plt.title(tipo);
            plt.xlabel('Dia');
            plt.ylabel('Dispesa em R$');
            plt.legend([f'{tipo} - original','Regressão Linear']);
            plt.show();
        else:
            print('A dispesa alvo não foi definida ou não existe.');
#Fim Classe Gráfica


#pré processamento de dados --------------------------------------------

#Utilizamos o faker para gerar valores.
fake = Faker('pt_BR');
def getFakeValues(min, max, dias):
    fakedValues = OrderedDict({});
    for i in range(dias):
        gasto = fake.pyfloat(left_digits = 3, right_digits = 2, positive = True, min_value = min, max_value = max);
        fakedValues[i+1] = gasto;
    return fakedValues;

# a partir de agora geramos os valores necessários
# por padrão deixei 20 dias como base (pode ser qualquer valor positivo).
# Obs: os valores gerados pelo faker são aleatórios a cada execução.
dias = 15;
# Aqui criamos um dicionário contendo o tipo de dispesa, juntamente com os gastos por dia.
disp_Obj = Dispesas(dispesas = OrderedDict(
{
    'Alimentar' : getFakeValues(15,50,dias),
    'Vestimenta' : getFakeValues(20,80,dias),
    'Transporte' : getFakeValues(5,40,dias),
    'Luz' : getFakeValues(90,130,dias),
    'Água' : getFakeValues(100,130,dias),
    'Internet' : getFakeValues(89,100,dias),
    'Telefone' : getFakeValues(40,60,dias),
})
);
# essa tabela de cores dita a cor que será usada Pela gráfica para gerar o gráfico de visão geral.
# se algum item do dicionário acima não tiver uma cor setada abaixo, ele ficará azul no gráfico por padrão.
ColorTable = {
    'Alimentar' : 'black',
    'Vestimenta' : 'pink',
    'Transporte' : 'green',
    'Luz' : 'brown',
    'Água' : 'blue',
    'Internet' : 'red',
    'Telefone' : 'purple',
}
#Apresentação dos Dados --------------------------------
graf = Grafica();

graf.showDispesasGrafica(dispesas = disp_Obj.dispesas,ColorTable = ColorTable);
#
graf.showDispesaEmGraficoAlvo(disp_Obj.dispesas,tipo= 'Alimentar',ColorTable = ColorTable);
graf.showDispesaEmGraficoAlvo(disp_Obj.dispesas,tipo= 'Vestimenta',ColorTable = ColorTable);
graf.showDispesaEmGraficoAlvo(disp_Obj.dispesas,tipo= 'Transporte',ColorTable = ColorTable);
graf.showDispesaEmGraficoAlvo(disp_Obj.dispesas,tipo= 'Luz',ColorTable = ColorTable);
graf.showDispesaEmGraficoAlvo(disp_Obj.dispesas,tipo= 'Água',ColorTable = ColorTable);
graf.showDispesaEmGraficoAlvo(disp_Obj.dispesas,tipo= 'Internet',ColorTable = ColorTable);
graf.showDispesaEmGraficoAlvo(disp_Obj.dispesas,tipo= 'Telefone',ColorTable = ColorTable);
# #---------