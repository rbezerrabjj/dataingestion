
class Credentials():
    def credentials(self,
                    host_mysql,
                    user_mysql,
                    password_mysql,
                    database_mysql,
                    driver_postgres,
                    host_postgres,
                    user_postgres,
                    dbname_postgres,
                    password_postgres,
                    sslmode_postgres,
                    port_postgres
                    ):

        self.host_mysql = host_mysql
        self.user_mysql = user_mysql
        self.password_mysql = password_mysql
        self.database_mysql = database_mysql
        self.driver_postgres = driver_postgres
        self.host_postgres = host_postgres
        self.user_postgres = user_postgres
        self.dbname_postgres = dbname_postgres
        self.password_postgres = password_postgres
        self.sslmode_postgres = sslmode_postgres
        self.port_postgres = port_postgres

# Mysql
host_mysql = "localhost"
user_mysql = "rbezerra"
password_mysql = "021212"
database_mysql = "pocingestionprd"

# Postgres
driver_postgres = "postgresql+psycopg2"
host_postgres = "localhost"
user_postgres = "etl"
dbname_postgres = "pocdw"
password_postgres = "021212"
sslmode_postgres = "require"
port_postgres = "5432"

# Table fato_pedidos
pm_id = "id"
pm_prd = "produto"
pm_lj = "loja"
pm_dt = "data"
pm_tb_ft_pd = "fato_pedidos"


def main():
    pass

if __name__ == "__main__":
    main()
