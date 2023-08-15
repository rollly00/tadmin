import os
import shutil
def download(bot, chat_id, message):
	try:
		# Путь к файлу или папке для скачивания
		args = message.text.split(' ', maxsplit=1)
		if len(args) < 2:
			bot.send_message(chat_id=chat_id, text='Не указано имя файла для скачивания')
			return
		file_path = args[1].strip('"')

		# Проверяем существует ли файл или папка по заданному пути
		if not os.path.exists(file_path):
			bot.send_message(chat_id=message.chat.id, text=f'Файл или папка "{file_path}" не найдены')
			return

		# Если путь указывает на папку, а не на файл, архивируем её
		if os.path.isdir(file_path):
			archive_name = f'{os.path.basename(file_path)}.zip'
			shutil.make_archive(archive_name, 'zip', file_path)
			file_path = f'{archive_name}.zip'

		# Отправляем файл пользователю
		with open(file_path, 'rb') as f:
			bot.send_document(chat_id=message.chat.id, document=f)

	except Exception as e:
		bot.send_message(chat_id=message.chat.id, text=f'Произошла ошибка, укажите файл или папку: {str(e)}')