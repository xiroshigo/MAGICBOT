from telethon import TelegramClient, events
import handlers.client
import os
import time
client = handlers.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.alive'))
async def alive(noob_py):
		client = noob_py.client
		me = await client.get_me()
		username = me.username
		darknet7719 = await client.download_profile_photo(username)
		await client.edit_message(noob_py.message, "Hayrli kun...")
		time.sleep(0.5)
		await noob_py.respond("Mening Userim: ~~@{}~~\n**MAGICBOT-UZ userbot**" "\nUserbot yangiliklari: ~~@MAGICBOT_UZ~~\nHAMKORLAR: @UTC_CREATORS\nDASTURCHI: ~~@darknet_off1cial~~{}".format(username, '\nEng havfsiz userbot'), file=darknet7719)
		await noob_py.message.delete()
		os.remove(darknet7719)