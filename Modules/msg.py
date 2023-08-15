from tkinter.messagebox import showinfo
def msg(bot, chat_id, message): 
    try:
        txt = message.text.split(' ', 1)[1].strip('"') if len(message.text.split(' ', 1)) > 1 else '.'
        showinfo(title="Информация", message=txt)
        bot.send_message(chat_id, text='Сообщение передано')
    except:
        pass
