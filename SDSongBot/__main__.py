#SDBOTs <https://t.me/SDBOTs_Inifinity>

from pyrogram.types.bots_and_keyboards import reply_keyboard_markup
from SDSongBot.plugins import *
from pyrogram import idle, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from SDSongBot import SDbot as app
from SDSongBot import LOGGER

pm_start_text = """
Salam [{}](tg://user?id={}), Mən Mahnı Yükləmək Üçün Kodlaşdırılmış Botam 🎵
🖤 İsdədiyin Mahnı Adını Mənə Göndər...⚡
      Məsələn:```/song Madrigal Seni Dert etmeler```
      
**Bot @Vusaliw Tərəfindən 0 Dan Tərcümə Olunmuşdur 🕊️**
"""

@app.on_message(filters.command("start"))
async def start(client, message):
    chat_id = message.chat.id
    user_id = message.from_user["id"]
    name = message.from_user["first_name"]
    if message.chat.type == "private":
        btn = InlineKeyboardMarkup(
            [
                [
                     InlineKeyboardButton(
                        text="PlayList 🔊", url="https://t.me/MusiqiYuklemePlayList"
                    ),
                    InlineKeyboardButton(
                        text="Developer 🧒🏻", url="https://t.me/vusaliw"
                    )
                ]
            ]
        )
    else:
        btn = None
    await message.reply(pm_start_text.format(name, user_id), reply_markup=btn)


app.start()
LOGGER.info("✅ Vüsalın Botu İşləyir...⚡.")
idle()
