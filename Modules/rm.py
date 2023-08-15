import os
import shutil
def rm(bot, chat_id, message):
	try:
		path = message.text.split(' ', 1)[1]
	except IndexError:
		bot.send_message(chat_id, text='Пожалуйста укажите название файла или папки')
		return

	try:
		if os.path.isdir(path):
			shutil.rmtree(path)
			bot.send_message(chat_id, text=f'Папка или файл {path} были удалены')
		else:
			os.remove(path)
			bot.send_message(chat_id=chat_id, text=f'Папка или файл {path} были удалены')
	except Exception as e:
			bot.send_message(chat_id, text=str(e))