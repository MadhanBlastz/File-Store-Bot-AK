#(©)codeflix_bots

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ ᴏᴡɴᴇʀ : <a>sᴏᴍᴇᴏɴᴇ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ😜</a>\n○ ᴍᴏʀᴇ ᴜᴘᴅᴀᴛᴇs : <a>AnimeRulzz</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ᴄʟᴏsᴇ⚡️", callback_data = "close"),
                    InlineKeyboardButton('🍁ᴊᴏɪɴ ɴᴏᴡ🍁', url='https://t.me/+qCIH0r0zF-JkYjc1')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pas
