import asyncio
import logging
from aiogram import Bot, Dispatcher
from tokens import bot_token
from handlers import router, cleanup_inactive_users

bot = Bot(token=bot_token)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    asyncio.create_task(cleanup_inactive_users())
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit bot')
