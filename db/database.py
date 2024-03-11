import sqlite3 as sql

async def sql_connect():
    con = sql.connect('db/evos.db')
    cur = con.cursor()
    return con, cur


async def create_tables():
    con, cur = await sql_connect()

    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                user_id BIGINT, 
                username VARCHAR(100)
    )""")


async def add_user(user_id: int, username: str):
    con, cur = await sql_connect()
    user = cur.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,)).fetchone()

    if not user:
        cur.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
        con.commit()

