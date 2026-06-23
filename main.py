import os
import re
from telethon import TelegramClient, events

# 1. مفاتيح المطور البرمجية الخاصة بحسابك (تم تثبيتها)
API_ID = 36188162
API_HASH = '3bf395c70bd1dde0546287ddccd3dacf'

# 2. القنوات الأربعة الكبرى التي سيراقبها حسابك آلياً في نفس الثانية
SOURCE_CHANNELS = ['deals_me', 'Mego_Reviews', 'Sal7lyEgypt', 'Discontly']

# 3. معرف قناتك العامة "أكواد كوم" لاستلام الكود نظيفاً فوراً
TARGET_CHANNEL = 'MySamrtCodes' 

client = TelegramClient('hunter_session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=SOURCE_CHANNELS))
async def my_event_handler(event):
    if event.message.text:
        # البحث الفوري عن أكواد أمازون (8 خانات فما فوق حروف كابيتال وأرقام متصلة)
        match = re.search(r'[A-Z0-9]{8,}', event.message.text)
        if match:
            clean_code = match.group(0)
            # قذف الكود منفرداً ونظيفاً تماماً داخل قناتك
            await client.send_message(TARGET_CHANNEL, clean_code)

print("⚡ صائد الأكواد الآلي التلقائي 100% يعمل الآن في الخلفية مجاناً للأبد...")
client.start()
client.run_until_disconnected()
