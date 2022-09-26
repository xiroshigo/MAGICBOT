from telethon import TelegramClient, events
import handlers.client, handlers.love
from handlers.naruto import Narutoa
import time
naruto = Narutoa()
client = handlers.client.client
@events.register(events.NewMessage)
async def narutohandler(event):
			
					if '.naruto' in event.raw_text:
						time.sleep(0.5)
						for d in naruto.narutoa:
							time.sleep(1.5)
							await event.edit(d)