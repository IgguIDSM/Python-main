import psycopg2;

conn = psycopg2.connect(database = 'postgres',user = 'postgres',password = 'brasil2018',host = '127.0.0.1',port = '5432');
print('Conexão executada com sucesso!');

cur = conn.cursor();

cur.execute('''CREATE TABLE IF NOT EXISTS PRODUTO (CODIGO INT PRIMARY KEY NOT NULL,NOME TEXT NOT NULL,PRECO REAL NOT NULL);''');
print('Tabela produto criada com sucesso!');
conn.commit();
conn.close();

