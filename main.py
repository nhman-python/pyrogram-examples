from pyrogram import filters
from pyrogram.client import Client
from pyrogram.handlers import MessageHandler, CallbackQueryHandler
from handlers.commands import start_command, help_command, counter_command
from handlers.message import echo_message
from handlers.callback_query import increment_call

# --------- get this data from my.telegram.org ----------- #
API_ID = 1234
API_HASH = "SDFGHJ"
# --------- get you not token from bot father on telegram @BotFather -------------#
BOT_TOKEN = "SDFGHJK"


app = Client("example-bot", api_hash=API_HASH, api_id=API_ID, bot_token=BOT_TOKEN)

app.add_handler(MessageHandler(start_command, filters=filters.command("start") & filters.private))
app.add_handler(MessageHandler(help_command, filters=filters.command("help") & filters.private))
app.add_handler(MessageHandler(counter_command, filters=filters.command("counter") & filters.private))
app.add_handler(CallbackQueryHandler(increment_call, filters=filters.regex(r"\d+")))
app.add_handler(MessageHandler(echo_message, filters=(filters.text | filters.caption) & filters.private))
app.run()

