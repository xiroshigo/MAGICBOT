from telethon import TelegramClient, events
import handlers.client
client = handlers.client.client

from asyncio import gather

from asyncio import gather


@events.register(events.NewMessage(outgoing=True, pattern=r'\.rma'))
async def runrma(event):
    messagelocation = event.to_id
    thisuser = "me"
    messageslimit = event.message.raw_text.split()
    try:
        gather(*[client.delete_messages(messagelocation, id) for id in [msg.id for msg in await client.get_messages(messagelocation, limit=int(messageslimit[1]), from_user=thisuser) if msg]])
    except:
        await event.client.send_message(messagelocation, "Something Went Wrong")