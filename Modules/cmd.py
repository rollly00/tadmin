import subprocess
import os
import shlex
import platform
def cmd(bot, chat_id, message):
	if platform.system() == "Windows":
		command = shlex.split(message.text.split(' ', 1)[1])
		output = subprocess.check_output(command, shell=True).decode('cp866')
		if output:
			chunks = [output[i:i+4096] for i in range(0, len(output), 4096)]
			for chunk in chunks:
				bot.send_message(chat_id=chat_id, text=f'<pre>{chunk}</pre>', parse_mode='HTML')
		else:
			bot.send_message(chat_id=chat_id, text='Успешно.')
	elif platform.system() == "Darwin":
		command = shlex.split(message.text.split(' ', 1)[1])
		try:
			output = subprocess.check_output(command, shell=True).decode('cp866')
			if output:
				chunks = [output[i:i+4096] for i in range(0, len(output), 4096)]
				for chunk in chunks:
					bot.send_message(chat_id=chat_id, text=f'<pre>{chunk}</pre>', parse_mode='HTML')
			else:
				bot.send_message(chat_id=chat_id, text='Успешно.')
		except ValueError as e:
			if str(e) == "No closing quotation":
				# Handle the case of a missing closing quotation mark
				bot.send_message(chat_id=chat_id, text='Нет закрытых кавычек.')
			else:
				# Handle other ValueError exceptions
				bot.send_message(chat_id=chat_id, text=f'Произошла ошибка: {str(e)}')
		except subprocess.CalledProcessError as e:
			bot.send_message(chat_id=chat_id, text=f'Ошибка при выполнении команды: {e}')