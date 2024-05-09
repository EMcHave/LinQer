import asyncio
from storage import create_table, get_link, check_link_existence, insert_link
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from const import (
    GREETING_MESSAGE,
    WANTED_TO_READ_MESSAGE,
    NO_LINKS_MESSAGE,
    LINK_ALREADY_EXISTS_MESSAGE,
    LINK_SAVED_SUCCESSFULLY_MESSAGE,
    ACTION_NOT_FOUND_MESSAGE,
    LINK_SAVED_ONLY_ONE_SUCCESSFULLY_MESSAGE,
)
import os
from dotenv import load_dotenv

load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(GREETING_MESSAGE)


@dp.message(Command("get_article"))
async def get_article_handler(message: Message):
    id_chat = message.chat.id
    text = get_link(id_chat)
    if text:
        await message.answer(WANTED_TO_READ_MESSAGE.format(text))
    else:
        await message.answer(NO_LINKS_MESSAGE)


@dp.message()
async def process_message_handler(message: Message):
    entities = message.entities or []
    id_chat = message.chat.id
    if len(entities) > 0 and message.entities[0].type == "url":
        found_links = [
            item.extract_from(message.text) for item in entities if item.type == "url"
        ]
        if len(found_links) > 1:
            link = found_links[0]
            if not check_link_existence(link, id_chat):
                insert_link(link, id_chat)
                await message.answer(
                    LINK_SAVED_ONLY_ONE_SUCCESSFULLY_MESSAGE.format(link)
                )
            else:
                await message.answer(LINK_ALREADY_EXISTS_MESSAGE)
        else:
            link = found_links[0]
            if not check_link_existence(link, id_chat):
                insert_link(link, id_chat)
                await message.answer(LINK_SAVED_SUCCESSFULLY_MESSAGE.format(link))
            else:
                await message.answer(LINK_ALREADY_EXISTS_MESSAGE)
    else:
        await message.answer(ACTION_NOT_FOUND_MESSAGE)


async def main() -> None:
    create_table()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Конец!")
