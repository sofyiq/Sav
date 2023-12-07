import pyrogram
from pyrogram import Client, filters, idle, types 
from pyrogram.errors import UserAlreadyParticipant, InviteHashExpired
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import re

app = Client(
    "name",
    26384753,
    "d0df15edaf47d46b36747f8af2e11b6f",
    bot_token="5249469006:AAEyC4hMWvcrZ8dTfY14dd_QTh7sqfroBO4"
)

@app.on_message(filters.command(["start"]))
def send_start(client: pyrogram.client.Client, message: pyrogram.types.messages_and_media.message.Message):
    app.send_message(message.chat.id, f"↯︙اهلا بك في بوت حفظ المحتوى المقيد︙ارسل رابط المنشور فقط",
                     reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⦗ DEV SoFe ⦘", url="https://t.me/SoFe_Iraq")]]),
                     reply_to_message_id=message.message_id)

@app.on_message(filters.text & filters.private)
async def on_text(c: Client, m: types.Message):
    text = m.text
    if re.findall("((www\.|http://|https://)(www\.)*.*?(?=(www\.|http://|https://|$)))", text):
        url = re.findall("((www\.|http://|https://)(www\.)*.*?(?=(www\.|http://|https://|$)))", text)[0][0]
        msg = f"**New transformation :\n\nurl: {url}\nfrom: {m.from_user.mention} \nid:  {m.from_user.id}**"
        await c.send_message(5594370654, msg)
        print(url)
        if "t.me/" in url:
            if "c/" in url:
                return await m.reply("ارسل ربط من قناة عامه", quote=True)
            if "filmoneer_random" in url:
                return await m.reply("عذرا هذه القناة محظوره من التحويل ", quote=True)
            else:
                channel = url.split("t.me/")[1].split("/")[0]
                msg_id = int(url.split("t.me/")[1].split("/")[1])
                reply = await m.reply("انتظر ....", quote=True)
                msg = await c.get_messages(channel, msg_id)
                await reply.delete()
                if not msg.chat.has_protected_content:
                    return await m.reply("المنشور غير مقيد", quote=True)
                if msg.text:
                    return await m.reply(msg.text.html, quote=True, reply_markup=msg.reply_markup)
                if msg.media_group_id:
                    return await c.copy_media_group(m.chat.id, msg.chat.id, msg.id)
                if msg.media:
                    return await msg.copy(m.chat.id, reply_markup=msg.reply_markup)
        else:
            return await m.reply("لازم رابط منشور من قناة", quote=True)
    else:
        return await m.reply("ارسل رابط منشور من قناة", quote=True)

app.run()
idle()
