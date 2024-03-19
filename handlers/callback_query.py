from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery


async def increment_call(_, query: CallbackQuery):
    if query.data.isdigit():
        num = str(int(query.data) + 1)
        await query.edit_message_text(num,
                                      reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton(num, num)
            ]
        ]))
