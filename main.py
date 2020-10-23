import telebot
from telebot import types
API_TOKEN = '496075695:AAGeItxJwnRi-pTgP5JWiIj08uFkbvsCPVk'
bot = telebot.TeleBot(API_TOKEN)

class ImportGoogleContactApp:
    @bot.message_handler(commands=['start'])
    def launch_bot(message):
        bot.send_message(message.chat.id, 'Bot start')

    def load_keyboard(self, message):
        keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(*)
if __name__ == '__main__':
    app = ImportGoogleContactApp()
    bot.polling(none_stop=True,timeout=123)