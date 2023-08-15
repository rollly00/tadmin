import os
import platform
import subprocess
def process(bot, chat_id):
	if platform.system() == 'Windows':
		try:
			output = subprocess.check_output(['tasklist']).decode('cp866')
			if len(output) < 4096:
				bot.send_message(chat_id=chat_id, text=f'<pre>{output}</pre>', parse_mode='HTML')
			else:
				for i in range(0, len(output), 4000):
					bot.send_message(chat_id=chat_id, text=f'<pre>{output[i:i+4000]}</pre>', parse_mode='HTML')
		except subprocess.CalledProcessError:
			bot.send_message(chat_id=chat_id, text='Произошла ошибка при получении списка процессов.')
	elif platform.system() == 'Darwin':
		try:
			command = "ps axc -o pid,command | awk '{print $1, \"\\\"\" $2 \"\\\"\"}'"
			output = os.popen(command).read().strip()
			if len(output) < 4096:
				bot.send_message(chat_id=chat_id, text=f'<pre>{output}</pre>', parse_mode='HTML')
			else:
				for i in range(0, len(output), 4000):
					bot.send_message(chat_id=chat_id, text=f'<pre>{output[i:i+4000]}</pre>', parse_mode='HTML')
		except:
			bot.send_message(chat_id=chat_id, text='Ошибка')
