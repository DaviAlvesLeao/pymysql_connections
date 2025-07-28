import mysql.connector
from typing import Any

from src._types import DtConfig
from src.config import Config



def get_connection(config: DtConfig):
    try:
      return mysql.connector.connect(
        host=config.host,
        user=config.user,
        password=config.password,
        database=config.db
      )
    except mysql.connector.Error as err:
        print("Can't connect connect to MySQL database: {}".format(err))
        raise SystemExit(err)

def fetchall(conn: Any, query: str) -> Any:
    rows = None
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
    return rows

def exist_table(conn: Any, table: str) -> bool:
    SQL = "SHOW TABLES LIKE \"roles\""
    rows = []
    if conn:
        with conn.cursor() as cursor:
            cursor.execute(SQL)
            rows = cursor.fetchone()
        return rows
    return rows


if __name__ == '__main__':
    conn = get_connection(DtConfig(
        host=Config.MYSQL_HOST,
        port=Config.MYSQL_PORT,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        db=Config.MYSQL_DATABASE,
    ))

    print(fetchall(conn, "SELECT * FROM users"))
    print(exist_table(conn, "roles"))