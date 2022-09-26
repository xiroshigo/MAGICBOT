from telethon import TelegramClient, events
import wikipedia
import asyncio
@events.register(events.NewMessage(pattern='.tipratikan$', outgoing=True))
async def wiki(event: events.NewMessage.Event):
    for i in range(9999):
        await event.edit('🍎'*(18 - i) + '🦔')
        await asyncio.sleep(.5)