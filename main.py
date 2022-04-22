from aiogram.utils import executor

from config import dp
from handlers import client, callback, extra, fsmadmin, \
    survey_one, survey_two, fsmadmin_register, notification, prayer_note
from database import bot_db
import asyncio


async def on_startup(_):
    bot_db.sql_create()
    asyncio.create_task(notification.scheduler())
    asyncio.create_task(prayer_note.scheduler())
    print("Bot is online")


fsmadmin_register.register_handler_for_users(dp)
survey_two.register_handlers_client(dp)
survey_one.register_handlers_client(dp)
fsmadmin.register_handler_admin(dp)
client.register_handlers_client(dp)
callback.register_handlers_callback(dp)
prayer_note.register_handler_prayer(dp)
notification.register_handler_notification(dp)
extra.register_handlers_other(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
