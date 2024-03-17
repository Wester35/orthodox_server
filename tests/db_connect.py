import aiopg


async def get_connection_pool():
    return await aiopg.create_pool(
        database='mes12121',
        user='postgres',
        password='Mercedes555!',
        host='5.228.52.190',
        port='5432'
    )


async def check_user_data(user_name, user_data, pool):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(f"SELECT * FROM usrs WHERE user_name = '{user_name}' AND passwd = '{user_data}'")
                row = await cursor.fetchone()

        return row is not None

    except Exception as error:
        print("Ошибка при работе с базой данных:", error)
        return False


async def add_user(user_name, user_data, pool):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(f"INSERT INTO usrs (user_name, passwd) VALUES ('{user_name}', '{user_data}')")
            await conn.commit()

    except Exception as error:
        print("Ошибка при работе с базой данных:", error)
        return False


async def add_msg(user_name, msg, pool):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute(f"INSERT INTO messages (usr_name, msg) VALUES ('{user_name}', '{msg}')")
            await conn.commit()

    except Exception as error:
        print("Ошибка при работе с базой данных:", error)
        return False


async def get_all_messages(pool):
    try:
        async with pool.acquire() as conn:
            async with conn.cursor() as cursor:
                await cursor.execute("SELECT * FROM messages")
                rows = await cursor.fetchall()

                return rows

    except Exception as error:
        print("Ошибка при работе с базой данных:", error)
        return False