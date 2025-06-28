from datetime import datetime, timedelta
from config import GRACE_PERIOD_DAYS, CHANNEL_ID
from database import get_users, remove_user
from aiogram import Bot

async def check_expired_users(bot: Bot):
    now = datetime.utcnow()
    for user_id, _, expire in get_users():
        expire_date = datetime.fromisoformat(expire)
        if (now - expire_date).days >= GRACE_PERIOD_DAYS:
            try:
                await bot.ban_chat_member(CHANNEL_ID, user_id)
                await bot.unban_chat_member(CHANNEL_ID, user_id)
                remove_user(user_id)
                print(f"Пользователь {user_id} удалён из канала из-за просроченной подписки.")
            except Exception as e:
                print(f"Ошибка при удалении пользователя {user_id}: {e}")