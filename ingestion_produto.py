from credentials import credentials as cd

from sqlalchemy import create_engine
# import pyodbc
import pandas as pd
# import os

import warnings
# from sqlalchemy.exc import SAWarning

warnings.filterwarnings("ignore")

import mysql.connector


def extract():
  try:
    conn = mysql.connector.connect(host=cd.host_mysql,
                                   user=cd.user_mysql,
                                   password=cd.password_mysql,
                                   database=cd.database_mysql
                                   )

    cursor = conn.cursor()

    # for tab in result:
    df = pd.read_sql(f'select '
                      f'{cd.pm_id_prd}, '
                      f'{cd.pm_prd_prd}, '
                      f'{cd.pm_vl_prd} '
                      f'from {cd.pm_tb_dm_prd}', conn)
    load(df, [0])  # , tab[0]

  except Exception as e:
      print("Data extract error: ", str(e))
      raise

  finally:
    conn.close()


def load(df, tab):
  try:
    rows = 0
    engine = create_engine(f'{cd.driver_postgres}://{cd.user_postgres}:{cd.password_postgres}@{cd.host_postgres}/{cd.dbname_postgres}')

    print(f'Importing rows {rows} to {rows + len(df)}... for table {tab}')


    df.to_sql(f'stg_produto', engine, if_exists='replace', index=False)
    print("Data imported successful")


  except Exception as e:
    print("Data load error: ", str(e))
    raise

try:
  extract()

except Exception as e:
  print("Error while extracting data: ", str(e))
  raise
