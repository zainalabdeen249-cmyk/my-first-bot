import telebot
from telebot import types # عشان نستخدم الأزرار
import re

# توكن بوتك الخاص
API_TOKEN = '8661170375:AAGpYfM9EkgSn6jn_crmCI92pRlmoaebDoc'
bot = telebot.TeleBot(API_TOKEN)

print("تم تشغيل بوت زين الأسطورة المطور... 🚀")

# أمر البداية مع أزرار احترافية
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("خدمات البوت 🛠️", callback_data='services')
    btn2 = types.InlineKeyboardButton("قناتي على GitHub 💻", url='https://github.com/zainalabdeen249-cmyk')
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, f"أهلاً بك يا {message.from_user.first_name} في نظام Zain Guard 🛡️\nأنا بوت حماية وخدمات متطور.", reply_markup=markup)

# الرد على ضغطة الزر
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "services":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text="خدماتنا حالياً:\n1- حماية المجموعات (حذف الروابط) 🛡️\n2- الرد التلقائي 🤖\n3- قريباً: تحميل الفيديوهات 📥")

# ميزة الحماية: حذف أي رابط يرسل في الشات
@bot.message_handler(func=lambda m: True)
def auto_guard(message):
    urls = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', message.text)
    if urls:
        try:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, f"⚠️ عذراً {message.from_user.first_name}، الروابط ممنوعة هنا لدواعي الأمان! 🛡️")
        except:
            bot.reply_to(message, "⚠️ ممنوع الروابط! (ارفعني أدمن في المجموعة لتفعيل الحذف التلقائي)")
    
    elif "السلام عليكم" in message.text:
        bot.reply_to(message, "وعليكم السلام ورحمة الله وبركاته! كيف أخدمك اليوم؟")

bot.infinity_polling()

