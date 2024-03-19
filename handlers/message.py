from pyrogram.types import Message


async def echo_message(_, message: Message):
    if text := message.text or message.caption:
        await message.reply(text)
