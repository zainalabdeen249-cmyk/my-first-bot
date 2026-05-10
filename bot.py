import telebot

# هنا نضع المفتاح الذي أرسلته
API_TOKEN = '8661170375:AAGpYfM9EkgSn6jn_crmCI92pRlmoaebDoc'

bot = telebot.TeleBot(API_TOKEN)

# رسالة الترحيب عند الضغط على /start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "مرحباً بك في بوت زين الأسطورة! 🛡️🇸🇩\nأنا هنا لخدمتكم وتطوير المشاريع التقنية.")

# الرد على أي رسالة نصية
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"وصلت رسالتك: {message.text}\nزين العابدين سيتواصل معك قريباً!")

print("البوت شغال الآن... اذهب لتليجرام وجربه!")
bot.infinity_polling()

