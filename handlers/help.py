import asyncio
from helpers.filters import command
from config import BOT_NAME, SUPPORT_GROUP, CHANNEL_UPDATES, START_IMG
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Client.on_message(command("help") & filters.private & ~filters.group & ~filters.edited)
async def help_cmd(client: Client, message: Message):
    await message.reply_sticker("CAACAgIAAx0CZD3aQwACJDFjJ-eam0HLnauJcFZ2QG1VMhVI5AAC3QgAArNsUEnxuIcx41T1ECkE")
    await message.reply_photo(f"{START_IMG}", caption=f"""
π΄ **AVAILABLE COMMAND IN {BOT_NAME} :**

β /play : Start streaming the requested track on videochat.
β /pause : Pause the stream.
β /resume : Resume the paused stream.
β /skip : Skip the current playing stream and start streaming the nexttrack in queue.
β /end : Clears the queue and the current playing stream.
β /ping : Show the ping and system stats of the bot.
β /join : Request the assistant to join your chat.
β /id : Sends you the id of the user or replied file.
β /song : Downloads the requested the song and send it to you .
β /search : Search the given query on youtube and shows you the result.

π΅ **SUDO COMMAND :**

β /broadcast : Broadcast a massage to served chats of the bot.
β /eval or /sh : Runs the gives codes on the bot's terminal.
β /rmw : Clears all the cache photos on the bot's server.
β /rmp : Clears the raw files of the bot.
β /rmd : Clears the download files on the bot's server.""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        " β° ππͺπ₯π₯π€π§π© β± ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        " β° ππ₯πππ©ππ¨ β± ", url=f"https://t.me/{CHANNEL_UPDATES}"
                    )
                ],
                [
                    InlineKeyboardButton(
                        " π ππΉπΌππ² ", callback_data="close_play"
                    )
                ]
            ]
       ),
    )
