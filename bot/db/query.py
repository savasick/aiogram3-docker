import aiopg
from bot.config import config

async def user_access(user_id: int, database_name: str, database_user: str, database_password: str, database_host: str, database_port: str):
    dsn = f'dbname={database_name} user={database_user} password={database_password} host={database_host} port={database_port}'
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    "SELECT * FROM users WHERE user_id = %s",
                    (user_id,)
                )
                ret = await cur.fetchone()
                return bool(ret)
            
async def insert_message(user_id: int, database_name: str, database_user: str, database_password: str, database_host: str, database_port: str, text: str):
    dsn = f'dbname={database_name} user={database_user} password={database_password} host={database_host} port={database_port}'
    async with aiopg.create_pool(dsn) as pool:
        async with pool.acquire() as conn:
            async with conn.cursor() as cur:
                await cur.execute(
                    "INSERT INTO messages (user_id, message_text) VALUES (%s, %s)",
                    (user_id, text)
                )
                #await cur.fetchone()
                #await conn.commit()
