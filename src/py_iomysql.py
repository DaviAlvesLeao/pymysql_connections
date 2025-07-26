import asyncio
import aiomysql
from src.config import Config
from src._types import DtConfig

async def get_connection(config: DtConfig):
    return await aiomysql.connect(
        host=config.host,
        port=config.port,
        user=config.user,
        password=config.password,
        db=config.db,
    )

async def execute_sql(sql: str, conn: aiomysql.Connection):
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(sql)
            await conn.commit()
    except Exception as e:
        raise e
    finally:
        conn.close()

async def fetchall(conn: aiomysql.Connection, query: str):
    try:
        async with conn.cursor() as cursor:
            await cursor.execute(query)
            rows = await cursor.fetchall()
            for row in rows:
                print(row)
    except Exception as e:
        raise e
    finally:
        conn.close()


async def main():
    conn = await get_connection(DtConfig(
        host=Config.MYSQL_HOST,
        port=Config.MYSQL_PORT,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        db=Config.MYSQL_DATABASE,
    ))
    insert_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    # await execute_sql(insert_table, conn)

    await fetchall(conn, "select * from users")

asyncio.run(main())
