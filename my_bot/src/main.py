import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN=os.getenv("BOT_TOKEN")
assert BOT_TOKEN is not None

print(BOT_TOKEN)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello {message.from_user.full_name}")

@dp.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer("Send me any message")

@dp.message()
async def echo(message: types.Message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="Wait a second...",
        reply_to_message_id=message.message_id,
    )
    await message.send_copy(chat_id=message.chat.id)
    await message.answer(text=str(message.text))
    await message.reply(text=str(message.text))

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())