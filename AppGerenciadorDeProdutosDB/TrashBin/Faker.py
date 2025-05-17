from faker import Faker;
import psycopg2;

conn = psycopg2.connect(database = 'postgres',user = 'postgres',password = 'brasil2018',host = '127.0.0.1',port = '5432');
print('Conection made with success!');
cur = conn.cursor();

fake = Faker('pt_BR');

#-----

n = 10;

for i in range(n):
    codigo = i+10;
    nome = 'produto' + str(i+1);
    preco = fake.pyfloat(left_digits = 3, right_digits = 2, positive = True, min_value = 5, max_value = 1000);
    print(f'Nome: {nome} | Preço: {preco}');

    comandoSQL = """INSERT INTO public."PRODUTO" ("CODIGO","NOME","PRECO") VALUES (%s,%s,%s) """;
    registro = (codigo,nome,preco);
    cur.execute(comandoSQL,registro);

#Commit connection
conn.commit();
print('Inserção dos produtos fake feita com sucesso!');
print('FInalizando Inserção do Programa Faker.py');
conn.close();