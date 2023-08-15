import os
def create_dir(bot,chat_id,message):
	try:
		dir_name = message.text.split(' ', 1)[1]
	except IndexError:
			bot.send_message(chat_id, text='Пожалуйста укажите название папки')
			return
	try:
		os.mkdir(dir_name)
		bot.send_message(chat_id, text=f'Папка{dir_name} была создана')
	except Exception as e:
		bot.send_message(chat_id, text=str(e))