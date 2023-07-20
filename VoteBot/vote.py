from telegram import TelegramError, Update
from telegram.ext import CommandHandler
from telegram.ext.dispatcher import CallbackContext, run_async


@run_async
def vote(update: Update, context: CallbackContext):
    args = context.args
    bot = context.bot
    try:
        chat_id = str(args[0])
        del args[0]
    except TypeError:
        update.effective_message.reply_text("Please give me a chat")
    to_send = " ".join(args)
    if len(to_send) >= 2:
        try:
            bot.sendMessage(int(chat_id), str(to_send))

__help__ = """ 
• /vote <ᴄʜᴀᴛɪᴅ>
"""

__mod_name__ = "vote"

SNIPE_HANDLER = CommandHandler(
    "vote", vote, pass_args=True
)
