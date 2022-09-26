from telethon import TelegramClient, events
import handlers.client, handlers.love
from handlers.sharingan import Sharingan
import time
sharingan = Sharingan()
client = handlers.client.client
@events.register(events.NewMessage)
async def sharinganhandler(event):
			
					if '.sharingan' in event.raw_text:
						for i in range(3):		
								time.sleep(0.5)
								for d in sharingan.sharingan:
									time.sleep(1.5)
									await event.edit(d)
									