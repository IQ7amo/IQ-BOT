#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import sys

from pyrogram import Client

import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"دەستپێکردنی بۆت")
        super().__init__(
            "IQMusicbot",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        try:
            await self.send_message(
                config.LOG_GROUP_ID, "بۆت دەستی پێکرد"
            )
        except:
            LOGGER(__name__).error(
                "بۆت شکستی هێنا لە چوونە ژورەوەی گرووپی تۆمار. دڵنیابە لەوەی کە بۆتەکەت زیاد کردووە بۆ کەناڵەکەت و بەرزتکردۆتەوە وەك بەڕێوەبەر!"
            )
            sys.exit()
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != "سەرپەرشتیار":
            LOGGER(__name__).error(
                "تکایە بۆت بەرز بکەوە وەکو بەڕێوەر لە گرووپ"
            )
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"{self.name} بۆتی گۆرانی دەستی پێکرد")
