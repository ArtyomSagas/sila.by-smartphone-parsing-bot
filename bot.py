import asyncio
import logging
from aiogram import Bot, Dispatcher
from config import settings
from handlers import router, cleanup_inactive_users, update_data

bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    asyncio.create_task(cleanup_inactive_users())
    asyncio.create_task(update_data())
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit bot')
