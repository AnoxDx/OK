from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery, Update

bot = Client(
    "my project",
    api_id="10534530",
    api_hash="8760d7849212237231adda6255eec300",
    bot_token="5656569490:AAGMMWe-4aLXg14ZiKmxgjYSy_t0J05dbS4"

)
START_PIC = 'https://graph.org/file/77809b5bf1db62f8e6ae5.jpg'
START_MESSAGE = """
**» ᴄʀᴇᴀᴛᴇ ᴠᴏᴛᴇ ᴘᴏʟʟ ꜰᴏʀ ɢɪᴠᴇᴀᴡᴀʏꜱ ᴏʀ ᴏᴛʜᴇʀ ᴘᴜʀᴘᴏꜱᴇꜱ ᴄʜᴇᴄᴋ ᴄᴏᴍᴍᴀɴᴅꜱ ᴜꜱɪɴɢ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ.** \n\n\
**‣ ʟᴇɢᴇɴᴅᴀʀʏ-ᴠᴏᴛᴇ-ʙᴏᴛ**
**‣ Oᴡɴᴇʀ ( @AnoxDx )**\n\n\
**ɪғ ʙᴏᴛ ɴᴏᴛ ᴡᴏʀᴋɪɴɢ ᴛʜᴇɴ ʀᴇᴘᴏʀᴛ ᴛᴏ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ( @EvonixZone ).**"""
START_BUTTONS = [
    [
        InlineKeyboardButton('ᴇᴠᴏɴɪᴛʏ', url='https://t.me/Evonity'),
        InlineKeyboardButton('ꜱᴜᴘᴘᴏʀᴛ', url='https://t.me/EvonixZone')
    ],
    [
        InlineKeyboardButton('✘ ʜᴇʟᴘ ✘', callback_data="HELP")
    ]
]


@bot.on_message(filters.command("start") & filters.private)
def start(bot, message):
    message.reply_photo(
        photo=START_PIC,
        caption=START_MESSAGE,
        reply_markup=InlineKeyboardMarkup(START_BUTTONS)
    )


@bot.on_callback_query()
def callback_query(Client, CallbackQuery):
    if CallbackQuery.data == "HELP":
        PAGE_TEXT = """✅ 𝗛𝗼𝘄 𝘁𝗼 𝘂𝘀𝗲 𝘁𝗵𝗶𝘀 𝗕𝗼𝘁?\n\n\
 **‣ ꜰɪʀꜱᴛ ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴠᴏᴛᴇ-ᴘᴏʟʟ ᴜsɪɴɢ /vote ᴄᴏᴍᴍᴀɴᴅ.**\n\n\
 **‣ ᴛʜᴇɴ ʙᴏᴛ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ᴘᴀʀᴛɪᴄɪᴘᴀᴛɪᴏɴ ʟɪɴᴋ. ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴏɴ ᴛʜɪꜱ ʟɪɴᴋ, ᴜꜱᴇʀꜱ ᴄᴀɴ ᴘᴀʀᴛɪᴄɪᴘᴀᴛᴇ ɪɴ ʏᴏᴜʀ ᴠᴏᴛᴇ-ᴘᴏʟʟ.**\n\n\
 **‣ ʏᴏᴜ ᴄᴀɴ ᴅᴇʟᴇᴛᴇ ʏᴏᴜʀ ᴠᴏᴛᴇ-ᴘᴏʟʟ ᴜsɪɴɢ /delete ᴄᴏᴍᴍᴀɴᴅ.**
"""
        PAGE_BUTTONS = [
            [
                InlineKeyboardButton('⟲ ʙᴀᴄᴋ', callback_data="OKBHAY")
            ]
        ]
        CallbackQuery.edit_message_text(
            PAGE_TEXT,
            reply_markup=InlineKeyboardMarkup(PAGE_BUTTONS)
        )
    if CallbackQuery.data == "OKBHAY":
        CallbackQuery.edit_message_text(
            START_MESSAGE,
            reply_markup=InlineKeyboardMarkup(START_BUTTONS)
        )


HELP_TEXT = """
**ʜᴇʟᴘ -> ** \n\n\
**/vote <ᴄʜᴀᴛ_ɪᴅ>/<ᴄʜᴀᴛ_ʟɪɴᴋ>** \n\n\
**ɴᴏᴛᴇ ɢɪᴠᴇᴀᴡᴀʏ ᴏɴʟʏ ʜᴇʟᴅ ɪɴ ᴘɪʙʟɪᴄ ᴄʜᴀɴɴᴇʟ ᴏʀ ɢʀᴏᴜᴘ**"""
SUPPORT = -1001629296335

@bot.on_message(filters.command('vote') & filters.private)
def vote(bot, message):
    message.reply(
        HELP_TEXT
    )

bot.run()
