import telebot

# O'z botingizning tokenini quyidagi qo'shtirnoq ichiga yozing:
TOKEN = "9056544226:AAGkVzzRWFjEhh8j_v3mEmW-dNvD0b0VSsk"
bot = telebot.TeleBot(TOKEN)

# /start buyrug'i uchun javob
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salom! Men sizning kino botingizman. 🎬\nMenga kino kodini yuboring.")

# Har qanday xabar yozilganda ishlaydigan qism
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    kino_kodi = message.text
    bot.reply_to(message, f"Siz yuborgan kod: {kino_kodi}\nTez orada bu kod bo'yicha kino chiqadigan qilinadi!")

print("Bot ishga tushdi...")
bot.infinity_polling()
