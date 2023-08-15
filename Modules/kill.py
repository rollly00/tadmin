import subprocess
import platform
import os
def kill(bot,chat_id,message):
	if platform.system() == "Windows":
		try:
			pid = message.text.split(' ')[1]
			subprocess.check_output(['taskkill', '/PID', pid, '/F'])
			bot.send_message(chat_id=chat_id, text=f'Процесс с PID {pid} был завершен.')
		except (subprocess.CalledProcessError, IndexError):
			bot.send_message(chat_id=chat_id, text='Ошбибка при завершении процесса.')
	elif platform.system() == "Darwin":
		try:
			pid = message.text.split(' ')[1]
			os.system(f"kill {pid}")
			bot.send_message(chat_id=chat_id, text=f'Процесс с PID {pid} был завершен.')
		except:
			bot.send_message(chat_id=chat_id, text='Ошбибка при завершении процесса.')
