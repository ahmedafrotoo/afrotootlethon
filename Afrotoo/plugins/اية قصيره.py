#الملف بحقوق سورس سيدثون @NUNUU
import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from Afrotoo import l313l
from ..helpers.utils import reply_id


@l313l.on(admin_cmd(outgoing=True, pattern="ايه قصيره$"))
async def jepvois(vois):
  rl = random.randint(111,210)
  url = f"https://t.me/lUl_UI{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎊︙ BY : @soursafrotoo 🌺",parse_mode="html")
  await vois.delete()


@l313l.on(admin_cmd(outgoing=True, pattern="سوره الفاتحة$"))
async def jepvois(Voice):
  url = f"https://t.me/dev_bilal/108"
  await Voice.client.send_file(Voice.chat_id,url,caption="⎊︙ سوره الفاتحة\n⎊︙ بصوت القارئ ماهر المعيقلي\n⎊︙ BY : @soursafrotoo🌺",parse_mode="html")
  await Voice.delete()

@l313l.on(admin_cmd(outgoing=True, pattern="ايه قصيره$"))
async def jepvois(Voice):
  url = f"https://t.me/dev_bilal"
  await Voice.client.send_file(Voice.chat_id,url,caption="⎊︙ سورس عفرتو \n⎊︙ ايه جميلة ربما من نصيبك\n⎊︙ BY : @soursafrotoo🌺",parse_mode="html")
  await Voice.delete()
