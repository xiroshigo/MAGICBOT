from telethon import events, Button
import handlers.client
#part2
client = handlers.client.client
#bot
botClient = handlers.client.botClient
with client as darknet:
				darknet.add_event_handler(handlers.greetings.greeting)

@botClient.on(events.InlineQuery)
async def iquery(query):
			if query.text == 'vhelp':
							result = query.builder.article('Ahelp', text = "PLUGINLAR (VOICE MEMLAR) MENUSI\n~~INFORMATION~~\nMAGICBOT_UZ - 2021 YIL 22-MAYDA DASTURLANGAN\n2022-yil 5-avgust kuni mukammallashtirildi\nCreatorlar: @utc_creators\ndasturchi: @darknet_off1cial", buttons=[
							[Button.inline("MADARA", data=b"1"),Button.inline("я ждал тебя", data=b"2")],
							[Button.inline("Chidori sasuke", data=b"3"),Button.inline("dattebayo", data=b"4")],
							
							[Button.inline("почувствой Боль", data=b"5"),Button.inline("Катон", data=b"6")],
							[Button.inline("Shindat tense", data=b"7"),Button.inline("есть слабость", data=b"8")],
							[Button.inline("Naruto golos", data=b"9"),Button.inline("GAARA DRUG", data=b"10")],
							[Button.url("MAGICBOT-UZ", url="https://t.me/Magicbot_uz"), Button.url("PLUGINS INFO", url="https://t.me/userbotcadr")]
							
							])
							await query.answer([result])
#callbackquery
@botClient.on(events.CallbackQuery)
#Madara
async def callback(event):
				if event.data== b'1':
								await event.answer("я учиха мадара: ishlatish: .madara", alert=True)
#я ждал тебя хаширама
				if event.data== b'3':
								await event.answer("использовал саске: ishlatish: .chidori", alert=True)
				if event.data== b'4':
								await event.answer("датебаё наруто: ishlatish: .dattebayo", alert=True)
				if event.data== b'5':
								await event.answer("почувствойте боль премите боль: ishlatish: .bol", alert=True)
				if event.data== b'2':
								await event.answer("я ждал тебя хаширама: ishlatish: .jdal", alert=True)
				if event.data== b'6':
								await event.answer("катон суитана жутсу, мадара учиха: ishlatish: .katon", alert=True)
				if event.data== b'7':
								await event.answer("шиндат тенсеи: ishlatish: .shinra", alert=True)
				if event.data== b'8':
								await event.answer("у каждой технике есть слабость#: ishlatish: .slabost", alert=True)
				if event.data== b'9':
								await event.answer("ishlatish: .Gnaruto", alert=True)
				if event.data== b'10':
								await event.answer("ishlatish: .GaaraDrug", alert=True)
				#if event.data== b'2':
#								await event.answer("я ждал тебя хаширама: ishlatish: .jdal", alert=True)

#ishlatish
@events.register(events.NewMessage(outgoing=True, pattern=r'\.vhelp'))

async def vhelphandler(event):
				results = await client.inline_query('@MAGICBOT_UZBOT', 'vhelp')
				await results[0].click(event.chat_id)
				await event.message.delete()
	