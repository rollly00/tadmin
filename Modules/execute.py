import os
import subprocess
import platform
def execute(bot,chat_id,message):
	try:
		if platform.system() == 'Windows':
			filename = message.text.split(' ')[1]
			os.startfile(filename)
		elif platform.system() == 'Darwin':
			filename = message.text.split(' ')[1]
			subprocess.call(['open', filename])
		bot.send_message(chat_id=chat_id, text=f'"{filename}" был запущен.')
	except IndexError:
		bot.send_message(chat_id=chat_id, text='Укажите файл или папку')
	except FileNotFoundError:
		bot.send_message(chat_id=chat_id, text='Файл или папка не найдены')
	except Exception as e:
		bot.send_message(chat_id=chat_id, text=f'Ошибка при запуске файла: {e}')	