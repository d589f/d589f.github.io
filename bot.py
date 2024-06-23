from telebot import TeleBot, types

TOKEN = '7374610503:AAHN6nVGHi3wsNw_cRoeCCQ4OonGTLDxeqQ'
bot = TeleBot(TOKEN)

# Замените на ваш публичный URL от ngrok
WEBAPP_URL = 'https://d589f.github.io/'

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    web_app_login = types.WebAppInfo(url=f"{WEBAPP_URL}/login")
    btn1 = types.InlineKeyboardButton("Login", web_app=web_app_login)
    web_app_register = types.WebAppInfo(url=f"{WEBAPP_URL}/register")
    btn2 = types.InlineKeyboardButton("Register", web_app=web_app_register)
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Hello! Choose an option:', reply_markup=markup)

if __name__ == "__main__":
    bot.polling(none_stop=True)
