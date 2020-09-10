#encoding utf-8

#__author__ = Jonas Duarte, duarte.jsystem@gmail.com
#Python3
__author__ = 'Jonas Duarte'

class Gera_query(object):
    def __init__(self):
        self.query = ""


    def nova_tabela(self, banco_de_dados, nova_tabela):
        self.query =  f"CREATE TABLE `{banco_de_dados}`"
        self.query += f".`{nova_tabela}` ENGINE = InnoDB;"

        return self.query


    def renomear_tabela(self, banco_de_dados, nome_atual, novo_nome):
        self.query =  f"RENAME TABLE `{banco_de_dados}`"
        self.query += f".`{nome_atual}` TO"
        self.query += f"`{banco_de_dados}`.`{novo_nome}`;"

        return self.query


    def excluir_tabela(self, tabela):
        self.query = f"DROP TABLE `{tabela}`"

        return self.query


    def listar_tabelas(self):
        self.query = "SHOW TABLES"

        return self.query


    def verifica_se_tabela_esta_vazia(self, tabela, where = False, coluna_verificacao = "Pessoa", valor_where = ""):
        self.query =  "SELECT * FROM"
        self.query += f"`{tabela}` "
        if where:
            self.query += f"WHERE `{coluna_verificacao}`"
            self.query += f"= '{valor_where}'"

        return self.query


    def listar_colunas(self, tabela):
        self.query = f"DESCRIBE `{tabela}`"

        return self.query


    def inserir_na_tabela(self, tabela, colunas, dados):
        """
        string é um booleano, que
        sendo verdadeiro indica que
        o dado necessita estar entre aspas simples
        caso contrario o dado pode ser inserido 
        sem estar entre aspas
        """
        self.query =  f"INSERT INTO `{tabela}`"
        self.query += f" ("
        cont = 0
        for coluna in colunas:
            cont += 1
            self.query += f"`{coluna}`"
            if cont < len(colunas):
                self.query += ", "
        self.query += ") VALUES ("
        
        cont = 0
        for dado in dados:
            cont += 1
            if dado * 0 == '' and 'now()' not in dado:
                self.query += f"'{dado}'"
            else:
                self.query += f"{dado}"
            if cont < len(dados):
                self.query += ", "
        self.query += ")"

        return self.query


    def alterar_dados_da_tabela(self, tabela, colunas, dados, where = False, coluna_verificacao = "", valor_where = "", string = False):
        """
        string é um booleano, que
        sendo verdadeiro indica que
        o dado necessita estar entre aspas simples
        caso contrario o dado pode ser inserido 
        sem estar entre aspas
        """
        self.query =  f"UPDATE `{tabela}` SET "

        x = 0
        for coluna in colunas:
            if dados[x] * 0 == '' and dados[x] != 'now()':
                self.query += f"`{coluna}` = '{dados[x]}'"
            else:
                self.query += f'`{coluna}` = {dados[x]}'
            if x < len(dados)-1:
                self.query += ', '
                x += 1

        if where:
            self.query += f" WHERE `{coluna_verificacao}` = {valor_where}"
        self.query += ";"

        return self.query


    def buscar_dados_da_tabela(self, tabela, where = False, coluna_verificacao = "", valor_where = "", returns=['*']):
        self.query = 'SELECT'

        for item in returns:
            self.query += f' {item}'
            if item != returns[len(returns)-1]:
                self.query += ','

        self.query += f' FROM `{tabela}` '
        if where:
            try:
                coluna_verificacao.append("")
            except:
                self.query += f"WHERE `{coluna_verificacao}` = '{valor_where}'"
            else:
                del(coluna_verificacao[len(coluna_verificacao)-1])
                self.query += "WHERE "
                for x in range(len(coluna_verificacao)):
                    self.query += f'`{coluna_verificacao[x]}` like "%{valor_where[x]}%"'
                    if x < len(coluna_verificacao) - 1:
                        self.query += " AND "

        return self.query


    def excluir_dados_da_tabela(self, tabela, where = False, coluna_verificacao = "", valor_where = ""):
        self.query = f"DELETE FROM `{tabela}` WHERE "
        if where:
            self.query += f"`{coluna_verificacao}` = '{valor_where}'"
        else:
            self.query += "0"

        return self.query