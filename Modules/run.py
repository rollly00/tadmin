import subprocess
import platform
def run(bot, chat_id, message):
	if platform.system() == "Windows":
		try:
			process_name = message.text.split(' ')[1]
			subprocess.Popen(['start', process_name], shell=True)
			bot.send_message(chat_id=chat_id, text=f'Процесс {process_name} был запущен.')
		except (subprocess.CalledProcessError, IndexError):
			bot.send_message(chat_id=chat_id, text='Ошибка при запуске процесса')
	elif platform.system() == "Darwin":
		bot.send_message(chat_id=chat_id, text='Только для Windows')
