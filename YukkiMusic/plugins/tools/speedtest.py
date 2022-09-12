#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import speedtest
from pyrogram import filters
from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("فەرمانی پێوانەکردنی خێرایی")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("دابەزاندنی پێوانەکردنی خێرایی")
        test.download()
        m = m.edit("نوێکردنەوەی پێوانەکردنی خێرایی")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("هاوبەشکردنی ئەنجامەکانی پێوانەکردنی خێرایی")
    except Exception as e:
        return m.edit(e)
    return result


@app.on_message(filters.command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("ڕاکردنی پێوانەکردنی خێرایی")
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, testspeed, m)
    output = f"""**ئەنجامەکانی پێوانەکردنی خێرایی**
    
<u>**Client:**</u>
**__دابینکەری خوزمەتگوزاری ئینتەرنێت:__** {result['client']['isp']}
**__وڵات:__** {result['client']['country']}
  
<u>**Server:**</u>
**__ناو:__** {result['server']['name']}
**__وڵات:__** {result['server']['country']}, {result['server']['cc']}
**__سپۆنسەر:__** {result['server']['sponsor']}
**__لێشاو:__** {result['server']['latency']}  
**__پینگ:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, 
        photo=result["هاوبەشکردن"], 
        caption=output
    )
    await m.delete()
