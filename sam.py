#👀

import pyrogram
import asyncio

from asyncio import sleep as slp
from pyrogram import Client, filters
from pyrogram.types import User, Message

from info import API_ID
from info import API_HASH
from info import SESSION
from info import ADMINS
from info import TIME
from info import GROUPS
#=======================================================================

Sam = Client(
    session_name= SESSION,
    api_id= API_ID,
    api_hash= API_HASH
)

#=======================================================================

@Sam.on_message(filters.group & filters.chat(GROUPS) & filters.all)
async def deleter(bot: Client, cmd: Message):
         if cmd.from_user.id not in ADMINS:
                  await slp(int(TIME))
                  await cmd.delete()

#=======================================================================

Sam.run()
print("Userbot Started!")

#=======================================================================
