import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from bot.config import config
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from bot.db.query import user_access, insert_message
from datetime import timedelta, datetime


database_host = config.BOT_DATABASE_HOST
database_port = config.BOT_DATABASE_PORT
database_name = config.BOT_DATABASE_NAME
database_user = config.BOT_DATABASE_USER
database_password = config.BOT_DATABASE_PASSWORD.get_secret_value()
bot_token = config.BOT_TOKEN.get_secret_value()

logging.basicConfig(level=logging.INFO)
bot = Bot(bot_token, parse_mode="HTML")
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    logging.info("Received start command from user %s", message.from_user.id)
    if await user_access(message.from_user.id, database_name, database_user, database_password, database_host, database_port):
        builder = ReplyKeyboardBuilder()
        builder.add(types.KeyboardButton(text=str("/info")))
        builder.add(types.KeyboardButton(text=str("/start")))
        await insert_message(message.from_user.id, database_name, database_user, database_password, database_host, database_port, message.text)
        await message.answer("yolo?", reply_markup=builder.as_markup(resize_keyboard=True))
    else:
        ban_duration = timedelta(hours=1)
        await bot.ban_chat_member(message.chat.id, message.from_user.id, until_date=int((datetime.now() + ban_duration).timestamp()))
        await message.answer("You don't have access to this command.")


@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    logging.info("Received info command from user %s", message.from_user.id)
    chat = await bot.get_chat(message.from_user.id)
    user_info = f"Username: {chat.username}, First Name: {chat.first_name}, Last Name: {chat.last_name}, ID: {chat.id}"
    await message.answer(f"Here is your information:\n{user_info}")



async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
