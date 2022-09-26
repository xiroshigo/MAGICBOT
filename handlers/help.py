from telethon import events, Button
import handlers.client
#part2
client = handlers.client.client
#bot
botClient = handlers.client.botClient
#with client as darknet:
#				darknet.add_event_handler(handlers.greetings.greeting)

@botClient.on(events.InlineQuery)
async def iquery(query):
			if query.text == 'help':
							
							result = query.builder.article('Help', text ="PLUGINLAR (funksiyalar) MENUSI\n~~INFORMATION~~\nMAGICBOT_UZ - 2021 YIL 22-MAYDA DASTURLANGAN\n2022-yil 5-avgust kuni mukammallashtirildi\nCreatoelar: @utc_creators\ndasturchi: @darknet_off1cial", buttons=[
							
												[Button.inline("NedoQuote", data=b"test"), Button.inline("ALIVE",data=b"test2")],
												[Button.inline("QUOTE", data=b"test3"), Button.inline("MemosityQuote", data=b"test4")],
												
												[Button.inline("CHat Info", data=b"test5"), Button.inline("Count",data=b"test6")],
												
												[Button.inline("rev", data=b"test7"), Button.inline("tagall",data=b"test8")],
												
												[Button.inline("admins", data=b"test9"), Button.inline("type",data=b"test10")],
												
												[Button.inline("clone pic", data=b"test11"), Button.inline("premium plugin", data=b"test12")],
												[Button.inline("ping", data=b"test13"), Button.inline("KICKER", data=b"test17")],
												
												
												[Button.inline("QR CODE MAKER", data=b"test114"), Button.inline("BASE 64 EN AND DE",data=b"test15")],
												[Button.inline("calculator", data=b"test16"),Button.inline("Ban all", data=b"test17")],
												[Button.inline("RENAME", data=b"test18"),Button.inline("spamm", data=b"test19")],
												[Button.inline("Text to emoji", data=b"test20"),Button.inline("wikipedia", data=b"test21")],
												[Button.inline("MANGA ANIME", data=b"test22")],
												
												
												[Button.url("MAGICBOT-UZ", url="https://t.me/MAGICBOT-UZ"), Button.url("PLUGINS INFO", url="https://t.me/userbotcadr")]
											
							
							])
							await query.answer([result])
#callbackquery
@botClient.on(events.CallbackQuery)
#nq
async def callback(event):
				if event.data== b'test':
								await event.answer("~~Textni rasm korinishidagi memga aylantiradi~~\nIshga tushurish: .nq", alert=True)
								#alive
				if event.data== b'test2':
								await event.answer("~~Userbotimiz haqida Malumotlar~~\nIshga tushurish: .alive", alert=True)
								#qq
				if event.data== b'test3':
								await event.answer("~~Textlarni sticker qilib beradi~~\nIshga tushurish: .qq", alert=True)
								#mq
				if event.data== b'test4':
								await event.answer("~~Textlarni sticker meme korinishida qilib beriadi~~\nIshga tushurish: .mq", alert=True)
								#chatinfo
				if event.data== b'test5':
								await event.answer("~~Telegram ommaviy chatlar hawida Toliq malumot beroladi~~\nIshga tushurish: .chatinfo", alert=True)
								#count
				if event.data== b'test6':
								await event.answer("~~Telegramda nechta kontagiz, nechta guruhiz, nechta kaanliz, nechta botiz bor ekanini korsatadi~~\nIshga tushurish: .count", alert=True)
				if event.data== b'test8':
								await event.answer("Guruhga yozselar hamma azolarni chaqiradi\nIshlatish: .tagall", alert=True)	
				if event.data== b'test10':
								await event.answer("Type moduli siz .type + biron soz yozsez uni write effecti bn yozilvotganday qiladi\nIshlatish: .type so'z", alert=True)
				if event.data== b'test9':
								await event.answer("Telegram guruhga .admins deb yzisez grdagi adminlarni chiwarib beradi\nIshlatish: .admins", alert=True)
				if event.data== b'test7':
								await event.answer("Rev moduli nomidan ham malum biron textga reply qib yozsez textni teskari qiberadi\nishlatish: .rev", alert=True)
				if event.data== b'test11':
								await event.answer("Kimgadir reply wib yozsez uni profel rasmini sizga avtomatik koʻchirib beradi\nishlatish: .picer", alert=True)		
				if event.data== b'test12':
								await event.answer("Premium modul uchun @films_uzru guruhiga 50 ta obunachi qoʻshish kerak\nPremium modul orqali siz Userbotimiz foydalanuvchilarini qaysi chatlarda bor ekanini scanerlay olasiz", alert=True)		
				if event.data== b'test13':
								await event.answer("Userbot Tezligini korsatadi\nIshlatish: .ping", alert=True)	
				if event.data==b'test14':
								await event.answer("QR CODE LARNI YASASH UCHUN YANGI PLUGIN\nIshlatish: .qrc create \nBiron bir textga reply wib yuborasiz", alert=True)		
				if event.data==b'test15':
								await event.answer("BASE64 SHIFRLASH VA SHIFRDAN YECHISH UCHUN PLUGIN\nISHLATISH: .b64 en\nBiron textga reply qib yuborasiz shifrlab beradi\nShifrdan yechish uchun shifrlangan textga: .b64 de\n buyrugini yuboras", alert=True)
				if event.data==b'test16':
								await event.answer("Kalkulyator plugini sizga hisoblashda komak beradi\n ishlatish: .ccr", alert=True)	
				if event.data==b'test17':
								await event.answer("guruhizda kimgadir reply qib yozsez uni guruhizdan blockledi\n ishlatish: .kick", alert=True)
				if event.data==b'test17':
								await event.answer("Uziz admin bugan guruhds  BANALL buyrugini yozsez guruhdagilarni hammasini blockledi\n ishlatish: .banall", alert=True)		
				if event.data==b'test18':
								await event.answer("Telegram nikizi hohlagan chatizda almashtirishiz mumkun bitta huyruq bilan\n ishlatish: .rename va nickname yozas", alert=True)		
				if event.data==b'test19':
								await event.answer("Spamm xabarlar, biron habarga reply qib yuborgsnda u habarni takroran 50 marotabagacha yuborishi mumkun max 50 yahshi\n ishlatish: qaysidir habarga reply qilib .spamm qayta yuborish soni", alert=True)
				if event.data==b'test20':
								await event.answer("Bu modulda text yozsez uni emoji textga aylantirib beradi\n ishlatish: .emoji text", alert=True)		
				if event.data==b'test21':
								await event.answer("Telegramda wikipwdia qidirish ingliz tilida\nishlatish: .wiki qidiruv sorovi", alert=True)		
				if event.data==b'test22':
								await event.answer("Anime msngalarni qidirish uchun\n ishlatish: .manga anime nomi ", alert=True)	

			
						
												
								
								#ishga tushurish
@events.register(events.NewMessage(outgoing=True, pattern=r'\.help'))
async def helphandler(event):
				results = await client.inline_query('@magicbot_uzbot', 'help')
				await results[0].click(event.chat_id)
				await event.message.delete()
				
			
	