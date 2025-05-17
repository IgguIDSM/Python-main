import psycopg2;

conn = psycopg2.connect(database = 'potgres',user = 'postgres', password = 'brasil2018'); # criamos a conexão com o banco de dados..
print('Conexão com o banco de dados aberta com sucesso!');

cur = conn.cursor(); # criamos um cursor baseado nessa conexão
cur.execute('CREATE TABLE AGENDA(ID INT PRIMARY KEY NOT NULL,Nome TEXT NOT NULL,Telefone CHAR(12));'); # desse cursor executamos comandos dentro do banco de dados alvo;

print('Tabela criada com sucesso!'); 

conn.commit(); # após isso comentamos no banco de dados as alterações feitas.
conn.close(); # após a alteração podemos fechar a conexão;

#teria exemplo de inserção e delete mas isso já sei fazer em SQL.