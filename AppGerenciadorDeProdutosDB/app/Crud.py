import psycopg2;

class AppDB:
    def __init__(self):
        print('Método Construtor');
    def OpenConection(self):
        try:
            self.connection = psycopg2.connect(database = 'postgres',user = 'postgres',password = 'brasil2018',host = '127.0.0.1',port = '5432');
        except (Exception, psycopg2.Error) as error:
            if(self.connection):
                print('SOMETHING WENT WRONG ON DATABASE CONNECT: ',error);

    def SelectData(self):
        registros = []  # Inicializa a variável registros
        try:
            self.OpenConection()
            with self.connection.cursor() as cursor:
                print('Getting all Products from database')
                sql_query = """select * from public."PRODUTO" """  # Isso seleciona todos os produtos dentro da tabela produto.
                cursor.execute(sql_query)
                registros = cursor.fetchall()
                print(registros)  # Retorna todos os registros encontrados na tabela
        except (Exception, psycopg2.Error) as error:
            print('SOMETHING WENT WRONG IN SELECTION OPERATION: ', error)
        finally:
            # Fecha a conexão e o cursor se estiverem abertos
            if self.connection and not self.connection.closed:
                self.connection.close()
            if cursor and not cursor.closed: #type:ignore
                cursor.close()
                print('The connection with the database was closed successfully!');
        return registros

    def InsertData(self,codigo,nome,preco):
        try:
            self.OpenConection();
            with self.connection.cursor() as cursor:
                sql_query = """ INSERT INTO public."PRODUTO"("CODIGO","NOME","PRECO") VALUES (%s,%s,%s) """;
                toInsert = (codigo,nome,preco);
                cursor.execute(sql_query,toInsert);
                self.connection.commit();
                count = cursor.rowcount;
                print(f'{count}| Produto inserido com sucesso na tabela!');
        except(Exception,psycopg2.Error) as error:
            print("SOMETHING WENT WRONG WITH INSERT OPRATION: ",error);
        finally:
            #Fecha a conexão e o cursor caso estejam abertos.
            if self.connection and not self.connection.closed:
                self.connection.close();
            if cursor and not cursor.closed: #type:ignore
                cursor.close();
                print('The connection with the database was closed succesfully!');

    def UpdateData(self, codigo, nome, preco):
        try:
            self.OpenConection();
            with self.connection.cursor() as cursor:
                sql_query = """ Update public."PRODUTO" set "NOME" = %s,"PRECO" = %s where "CODIGO" = %s """
                toUpdate = (nome,preco,codigo);
                cursor.execute(sql_query,toUpdate);
                self.connection.commit();
                count = cursor.rowcount;
                print(f'{count} | Produto atualizado com sucesso!');
        except (Exception,psycopg2.Error) as error:
            print("SOMETHING WENT WRONG WITH UPDATE OPERATION: ",error);
        finally:
            #Fecha a conexão e o cursor caso estejam abertos.
            if self.connection and not self.connection.closed:
                self.connection.close();
            if cursor and not cursor.closed: #type:ignore
                cursor.close();
                print('The connection with the database was closed sucessfully!');

    def RemoveData(self,codigo):
        try:
            self.OpenConection();
            with self.connection.cursor() as cursor:
                sql_query = """ Delete from public."PRODUTO" where "CODIGO" = %s """;
                cursor.execute(sql_query,(codigo,));
                count = cursor.rowcount;
                print(f'{count} | Produto deletado com sucesso!');
        except(Exception,psycopg2.Error) as error:
            print('SOMETHING WENT WRONG WITH DELETE OPERATION: ',error);
        finally:
            #Fecha a conexão e o cursor caso estejam abertos.
            if self.connection and not self.connection.closed:
                self.connection.close();
            if cursor and not cursor.closed: #type:ignore
                cursor.close();
                print('The connection with the database was closed sucessfully!');
            


