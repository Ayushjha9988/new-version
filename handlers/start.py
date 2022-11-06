import asyncio

from helpers.filters import command
from config import BOT_NAME as bn, BOT_USERNAME as bu, CHANNEL_UPDATES, SUPPORT_GROUP, OWNER_USERNAME as me, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(command("start") & filters.private & ~filters.group & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAILx2NntoLIEI1EkUjRidSvRiiVk-JlAAJ_BgACGHNAV0RLWPOsXuu5KwQ")
    await message.reply_photo(
        photo=f"{START_IMG}",
        caption=f""" ** 𝗛𝗲𝘆👋 {message.from_user.mention()} , 🥀\n\n

➤ 𝚃𝚑𝚎 𝚖𝚘𝚜𝚝 𝙿𝚘𝚠𝚎𝚛𝚏𝚞𝚕 𝚝𝚎𝚕𝚎𝚐𝚛𝚊𝚖 𝚖𝚞𝚜𝚒𝚌  𝚋𝚘𝚝 𝚠𝚒𝚝𝚑 𝚜𝚘𝚖𝚎 𝚊𝚠𝚎𝚜𝚘𝚖𝚎 𝚊𝚗𝚍 𝚞𝚜𝚎𝚏𝚞𝚕 𝚏𝚎𝚊𝚝𝚞𝚛𝚎𝚜.

──────────────────
➤ 𝙰𝚕𝚕 𝚘𝚏 𝚖𝚢 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚌𝚊𝚗 𝚋𝚎 𝚞𝚜𝚎𝚍 𝚠𝚒𝚝𝚑 𝙼𝚢 𝚌𝚘𝚖𝚖𝚊𝚗𝚍 𝚑𝚊𝚗𝚍𝚕𝚎 : ( / . • $ ^ ~ + * ? )
➤ 𝙷𝚒𝚝 /help 𝚝𝚘 𝚜𝚎𝚎 𝚖𝚢 𝙿𝚘𝚠𝚎𝚛𝚜 𝙱𝚞𝚍𝚍𝚢.
➤ 𝙼𝚊𝚍𝚎 𝚋𝚢 ❤️ 𝚊𝚗𝚍 [𝚂𝚊𝚗𝚐𝚛𝚊𝚖](https://t.me/OpSangram) ** """,
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " ❰ 𝘼𝙙𝙙 𝙢𝙚 𝙗𝙖𝙗𝙮 ❱ ", url=f"https://t.me/{bu}?startgroup=true"
                       ),
                 ],[
                    InlineKeyboardButton(
                        " ❰ 𝙐𝙥𝙙𝙖𝙩𝙚𝙨 ❱ ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    ),
                    InlineKeyboardButton(
                        " ❰ 𝙎𝙪𝙥𝙥𝙤𝙧𝙩 ❱ ", url=f"https://t.me/{SUPPORT_GROUP}"
                    )
                  ],[
                    InlineKeyboardButton(
                        " ❰ 𝙊𝙬𝙣𝙚𝙧🥀 ❱ ", url=f"https://t.me/{me}"
                    ),
                    InlineKeyboardButton(
                        " ❰ ❤️𝘿𝙚𝙫𝙚𝙡𝙤𝙥𝙚𝙧❤️ ❱ ", url=f"https://t.me/OpSangram"
                    ),
                  ],[
                    InlineKeyboardButton(
                        "✅ Inline ", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        " ❰ 💬𝙒𝘾𝙁 𝘾𝙝𝙖𝙩𝙩𝙞𝙣𝙜💬 ❱ ", url="https://t.me/WorldChattingFriendsWCF"
                    )]
            ]
       ),
    )

