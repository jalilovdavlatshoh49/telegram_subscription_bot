import asyncio
import threading
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from handlers import router
from utils import check_expired_users
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import http.server
import socketserver

# 🟡 Dummy HTTP server барои Render Web Service
def run_dummy_server():
    PORT = 8080
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Dummy server running on port {PORT}")
        httpd.serve_forever()

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)

    scheduler = AsyncIOScheduler()
    scheduler.add_job(check_expired_users, "interval", days=1, args=[bot])
    scheduler.start()

    # 🔵 Start dummy server in background thread
    threading.Thread(target=run_dummy_server, daemon=True).start()

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
