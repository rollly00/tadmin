import webbrowser
import os
import platform
def link(bot, chat_id, message):
	if platform.system() == "Windows":
		link = message.text.split(' ')[1]
		webbrowser.open(link)
		bot.send_message(chat_id=chat_id, text="Открываю ссылку")
	elif platform.system() == "Darwin":
		link = message.text.split(' ')[1]
		os.system('open http://' + link)
		bot.send_message(chat_id=chat_id, text="Открываю ссылку")