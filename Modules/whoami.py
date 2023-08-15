import os
import platform
import psutil
def whoami(bot, chat_id):
	computer_name = platform.node()
	user_name = platform.uname().node
	ram = psutil.virtual_memory().total // (1024 ** 3)
	cpu_name = platform.processor()
	if platform.system() == 'Windows':
		from win32api import GetSystemMetrics
		os_version = platform.win32_ver()[0]
		screen_resolution = f"{GetSystemMetrics(0)}x{GetSystemMetrics(1)}"
	elif platform.system() == 'Darwin':
		os_version = platform.mac_ver()[0]
		command = 'system_profiler SPDisplaysDataType | awk \'/Resolution:/ {print $2"x"$4}\''
		output = os.popen(command).read().strip()
		screen_resolution = output
	message_text = f"Имя: {computer_name}\nЮзер: {user_name}\nОЗУ: {ram} GB\nЦПУ: {cpu_name}\nВерсия ОС: {os_version}\nРазрешение экрана: {screen_resolution}"
	bot.send_message(chat_id=chat_id, text=message_text)