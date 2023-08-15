import os
def dirlist(bot,chat_id,message):
	try:
		path = message.text.split(' ')[1] if len(message.text.split(' ')) > 1 else '.'
		files = os.listdir(path)
		files_str = '\n'.join(files)
		response = f'Текущая директория: {path}\n\n{files_str}'
		bot.send_message(chat_id, text=response)
	except FileNotFoundError:
		bot.send_message(chat_id, text=f'Путь {path} не существует')
