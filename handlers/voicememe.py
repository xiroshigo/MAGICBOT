from telethon import TelegramClient, events
import handlers.client
client = handlers.client.client

@events.register(events.NewMessage(outgoing=True, pattern='\.madara'))
async def madara(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/10")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.jdal'))
async def jdal(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/13")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.chidori'))
async def chidori(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/15")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.dattebayo'))
async def dattebayo(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/17")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.posje'))
async def posje(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/19")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.bol'))
async def bol(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/21")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.katon'))
async def katon(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/23")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.shinra'))
async def shinra(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/25")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.slabost'))
async def slabost(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/35")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.Gnaruto'))
async def nandemo(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/44")
    await send_file.message.delete()

@events.register(events.NewMessage(outgoing=True, pattern='\.GaaraDrug'))
async def drug(send_file):
    await client.send_file(send_file.chat_id, "https://t.me/GolosHost/46")
    await send_file.message.delete()