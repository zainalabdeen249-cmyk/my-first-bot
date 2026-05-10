import telebot
from telebot import types
import yt_dlp
import os
import re

# توكن بوتك
API_TOKEN = '8661170375:AAGpYfM9EkgSn6jn_crmCI92pRlmoaebDoc'
bot = telebot.TeleBot(API_TOKEN)

print("نظام زين جارد الشامل شغال الآن... 🚀🛡️")

# دالة التحميل
def download_video(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',
        'quiet': True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# أمر البداية مع الأزرار
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("خدمات البوت 🛠️", callback_data='services')
    btn2 = types.InlineKeyboardButton("قناتي على GitHub 💻", url='https://github.com/zainalabdeen249-cmyk')
    markup.add(btn1, btn2)
    
    bot.send_message(message.chat.id, f"أهلاً بك يا {message.from_user.first_name} في Zain Guard 🛡️\nأرسل رابط فيديو للتحميل، أو اضغط على الخدمات.", reply_markup=markup)

# الرد على الأزرار
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "services":
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, 
                             text="قائمة الخدمات الذكية:\n1- تحميل فيديوهات (تيك توك/إنستا) 📥\n2- حماية المجموعات من الروابط 🛡️\n3- الرد التلقائي الذكي 🤖")

# معالجة الروابط والرسائل (الدمج)
@bot.message_handler(func=lambda m: True)
def handle_all(message):
    text = message.text
    
    # أولاً: ميزة التحميل (لو الرابط من تيك توك أو إنستا)
    if 'tiktok.com' in text or 'instagram.com' in text:
        msg = bot.reply_to(message, "جاري معالجة الفيديو للتحميل... ⏳")
        try:
            download_video(text)
            with open('video.mp4', 'rb') as video:
                bot.send_video(message.chat.id, video, caption="تم التحميل بواسطة زين الأسطورة 🛡️")
            os.remove('video.mp4')
            bot.delete_message(message.chat.id, msg.message_id)
        except:
            bot.edit_message_text("عذراً، فشل التحميل. تأكد من أن الحساب عام وليس خاص! ❌", message.chat.id, msg.message_id)
    
    # ثانياً: ميزة الحماية (حذف أي رابط آخر)
    elif re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text):
        try:
            bot.delete_message(message.chat.id, message.message_id)
            bot.send_message(message.chat.id, "⚠️ الروابط ممنوعة هنا لدواعي الأمان! 🛡️")
        except: pass

    # ثالثاً: الردود الذكية القديمة
    elif "السلام عليكم" in text:
        bot.reply_to(message, "وعليكم السلام يا غالي! كيف أخدمك؟")

bot.infinity_polling()

