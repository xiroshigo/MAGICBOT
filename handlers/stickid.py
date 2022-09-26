from telethon import TelegramClient, events
import handlers.client
import os
client = handlers.client.client
@events.register(events.NewMessage(outgoing=True, pattern='\.stickid'))
async def stickid(event):
	       chat = await event.get_chat()
	       replied_msg = await event.get_reply_message()
	       await event.edit("Kutilmoqda...")
	       x = await replied_msg.forward_to('@idstickerbot')
	       #print(x)
	       async with client.conversation('@idstickerbot') as conv:
	       	xx = await conv.get_response(x.id)
	       	await client.send_read_acknowledge(conv.chat_id)
	       	await client.send_message(chat, xx)
	       	await event.message.delete()
