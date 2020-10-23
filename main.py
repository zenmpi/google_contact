import telebot

API_TOKEN = '496075695:AAGeItxJwnRi-pTgP5JWiIj08uFkbvsCPVk'

bot = telebot.TeleBot(API_TOKEN)

class ImportGoogleContactApp:
    def __init__(self):
        super(ImportGoogleContactApp, self).__init__()
        self.launch_bot()
    
    @bot.message_handler(commands=['start'])
    def launch_bot(self):
        bot.send_message(message.chat.id, 'Bot start')