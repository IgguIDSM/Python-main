import os
import matplotlib.pyplot as plt;


x = ["A","B","C","D"];
y = [3,800000000,1,10];
# Configs
plt.bar(x,y,color = "cyan");
plt.xticks(x);
plt.ylabel("Vendas");
plt.xlabel("Produtos");
plt.title("Vendas / Produtos");
# Mostra o gráfico
plt.show();
