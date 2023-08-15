import os
def cd(bot,chat_id,message):
	try:
		path = message.text.split(' ', 1)[1].strip('"') if len(message.text.split(' ', 1)) > 1 else '.'
		os.chdir(path)
		bot.send_message(chat_id, text=f'Текущая директория: {os.getcwd()}')
	except FileNotFoundError:
		bot.send_message(chat_id, text=f'Путь {path} не существует')
	except OSError as e:
		bot.send_message(chat_id, text=f'Ошибка: {str(e)}')