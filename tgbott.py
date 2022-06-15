import telebot
from telebot import types


bot = telebot.TeleBot("РЫБА", parse_mode=None)

import os
checkimg = os.path.isfile('file.jpg')
if checkimg == True:
	os.remove('file.jpg')
@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Масло")
	item2 = types.KeyboardButton("Пепси")
	markup.add(item1, item2)
	bot.send_message(message.chat.id,"Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы обрабатывать твои изображения с помощью Photoshop Action. Загрузи изображение и выбери Action из представленных вариантов:".format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def new_message(message: telebot.types.Message):
	file_path = bot.get_file(message.photo[-1].file_id)
	downloaded_file = bot.download_file(file_path.file_path)
	with open('file.jpg', 'wb') as new_file:
		new_file.write(downloaded_file)

@bot.message_handler(content_types=['text'])
def send_img(message):
	start = "/start"
	oil = "Масло"
	peps = "Пепси"
	textans = str(message.text)
	if textans != start and textans != oil and textans != peps:
		bot.send_message(message.chat.id, "Напиши пожалуйста команду /start")
	if message.text == "Пепси":
		import os
		checkimg = os.path.isfile('file.jpg')
		if checkimg == False:
			bot.send_message(message.chat.id, "Отправьте пожалуйсто изображение")
		else:
			import photoshop.api as ps
			app = ps.Application()
			doc = app.open("C:/Users/Димас/PycharmProjects/tgbot/venv/file.jpg")
			app.doAction("POSTERIZE EFFECT by PhotoshopSupply.com", "POSTERIZE by PhotoshopSupply.com")
			options = ps.JPEGSaveOptions(quality=5)
			# # save to jpg
			jpg = 'C:/Users/Димас/PycharmProjects/tgbot/venv/tst.jpg'
			doc.saveAs(jpg, options, asCopy=True)
			# app.doJavaScript(f'alert("save to jpg: {jpg}")')
			photo = open('tst.jpg', 'rb')
			bot.send_photo(message.chat.id, photo)
			os.remove('file.jpg')
			doc.close()

	if message.text == "Масло":
		import os
		checkimg = os.path.isfile('file.jpg')
		if checkimg == False:
			bot.send_message(message.chat.id, "Отправьте пожалуйсто изображение")
		else:
			import photoshop.api as ps
			app = ps.Application()
			doc = app.open("C:/Users/Димас/PycharmProjects/tgbot/venv/file.jpg")
			app.doAction("Action 51", "Oil-paint")
			options = ps.JPEGSaveOptions(quality=5)
			# # save to jpg
			jpg = 'C:/Users/Димас/PycharmProjects/tgbot/venv/tst.jpg'
			doc.saveAs(jpg, options, asCopy=True)
			# app.doJavaScript(f'alert("save to jpg: {jpg}")')
			photo = open('tst.jpg', 'rb')
			bot.send_photo(message.chat.id, photo)
			os.remove('file.jpg')
			doc.close()
			import subprocess as sp
			sp.Popen('taskkill /im Photoshop.exe /f')



bot.polling( non_stop=True )
