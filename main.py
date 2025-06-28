import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router
from utils import check_expired_users
from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_expired_users, "interval", days=1, args=[bot])
    scheduler.start()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())