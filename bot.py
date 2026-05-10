import telebot
import re

API_TOKEN = '8661170375:AAGpYfM9EkgSn6jn_crmCI92pRlmoaebDoc'
bot = telebot.TeleBot(API_TOKEN)

print("البوت المطور شغال الآن...")

# الترحيب
@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "أهلاً بك في نظام زين جارد (Zain Guard) 🛡️\nأرسل 'خدمات' لرؤية ما يمكنني فعله.")

# قائمة الخدمات
@bot.message_handler(func=lambda m: m.text == "خدمات")
def services(message):
    bot.reply_to(message, "1- حماية المجموعات من الروابط 🛡️\n2- الرد التلقائي الذكي 🤖\n3- قريباً: تحميل الفيديوهات 📥")

# ميزة الحماية: حذف الروابط (لو أضفت البوت لمجموعة وعملته أدمن)
@bot.message_handler(func=lambda m: True)
def handle_all_messages(message):
    # كشف الروابط
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
    if urls:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, f"⚠️ ممنوع إرسال الروابط يا {message.from_user.first_name} لحماية الأعضاء!")
    
    # ردود ذكية بسيطة
    elif "السلام عليكم" in message.text:
        bot.reply_to(message, "وعليكم السلام يا غالي، كيف أقدر أساعدك؟")

bot.infinity_polling()

