from telethon import events
from html_telegraph_poster.upload_images import upload_image
from os import remove

@events.register(events.NewMessage(outgoing=True, pattern=r'\.tgi'))
async def runtgu(event):
    await event.edit("Yuklanmoqda...")
    getcontent = await event.get_reply_message()
    messagelocation = event.to_id
    try:
        targetcontent = await getcontent.download_media()
        uploadcontent = upload_image(targetcontent)
    except:
        return await event.edit("Nimadir hato")
    await event.delete()
    await event.client.send_message(messagelocation, uploadcontent)
    remove(targetcontent)