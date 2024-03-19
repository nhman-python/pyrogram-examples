from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_command(_, message: Message):
    await message.reply(f"hello {message.from_user.full_name} this is a text bot")


async def help_command(_, message: Message):
    await message.reply(f"this is text of help command")


async def counter_command(_, message: Message):
    await message.reply("1", reply_markup=InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(str(1), str(1))
            ]
        ]
    ))
