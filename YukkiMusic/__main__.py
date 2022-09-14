#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from YukkiMusic import LOGGER, app, userbot
from YukkiMusic.core.call import Yukki
from YukkiMusic.plugins import ALL_MODULES
from YukkiMusic.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("IQmusic").error(
            "هیچ یاریدەدەرێکی کڕیارەکان پێناسە نەکراوە!.. پرۆسەی دەرچوون"
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("IQmusic").warning(
            "هیچ سپۆتیفای ڤار پێناسە نەکراوە. بۆتەکەت ناتوانێت کاربکات بۆ نیشانەکردنی پرسیارەکان"
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("IQmusic.plugins" + all_module)
    LOGGER("IQmusic.plugins").info(
        "بە سەرکەوتوویی هاوردەکرا "
    )
    await userbot.start()
    await Yukki.start()
    try:
        await Yukki.stream_call(
            "http://docs.evostream.com/sample_content/assets/sintel1m720p.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("IQmusic").error(
            "[ERROR] - \n\nPlease چاتی دەنگی logger  پێبکە. دڵنیابە لەوەی کە هەرگیز داناخەیت/کۆتایی ناهێنیت بە چاتی دەنگی گرووپی logger"
        )
        sys.exit()
    except:
        pass
    await Yukki.decorators()
    LOGGER("IQmusic").info("IQmusic بە سەرکەوتوویی دەستی پێکرد")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("IQmusic").info("وەستاندنی IQ مووزیک بۆت! خوات لەگەڵ")
