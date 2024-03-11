from aiogram import executor
from utils.loader import dp
from db.database import create_tables

async def on_startup(dp):
    await create_tables()
    import handlers.users as users

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
