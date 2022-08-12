#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K | @AbirHasan2005


import os

from bot import (
    APP_ID,7774029
    API_HASH,531dbf42d387514dc43da07db9f2dc8f
    AUTH_USERS,1654867043
    DOWNLOAD_LOCATION,
    LOGGER,
    TG_BOT_TOKEN,5264031481:AAElVQQ19zSav2s1WyoFfOtFt7QXuhdrReA
    BOT_USERNAME,videocompress1023bot
    SESSION_NAME,AHcompress
    DATABASE_URL,
)
from bot.plugins.new_join_fn import (	
    help_message_f	
)

from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler, CallbackQueryHandler

from bot.plugins.incoming_message_fn import (
    incoming_start_message_f,
    incoming_compress_message_f,
    incoming_cancel_message_f
)

from bot.plugins.admin import (
    sts,
    ban,
    unban,
    _banned_usrs
)

from bot.plugins.broadcast import (
    broadcast_
)

from bot.plugins.status_message_fn import (
    exec_message_f,
    upload_log_file
)

from bot.commands import Command
from bot.plugins.call_back_button_handler import button

if __name__ == "__main__" :
    # create download directory, if not exist
    if not os.path.isdir(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
    #
    
    app = Client(
        SESSION_NAME,AHcompress
        bot_token=TG_BOT_TOKEN,5264031481:AAElVQQ19zSav2s1WyoFfOtFt7QXuhdrReA
        api_id=APP_ID,7774029
        api_hash=API_HASH,531dbf42d387514dc43da07db9f2dc8f
        workers=2
    )
    #
    app.set_parse_mode("html")
    #
    # STATUS ADMIN Command
    incoming_status_command = MessageHandler(
        sts,
        filters=filters.command(["status"]) & filters.user(AUTH_USERS)
    )
    app.add_handler(incoming_status_command)

    # BAN Admin Command
    incoming_ban_command = MessageHandler(
        ban,
        filters=filters.command(["ban_user"]) & filters.user(AUTH_USERS)
    )
    app.add_handler(incoming_ban_command)

    # UNBAN Admin Command
    incoming_unban_command = MessageHandler(
        unban,
        filters=filters.command(["unban_user"]) & filters.user(AUTH_USERS)
    )
    app.add_handler(incoming_unban_command)

    # BANNED_USERS Admin Command
    incoming_banned_command = MessageHandler(
        _banned_usrs,
        filters=filters.command(["banned_users"]) & filters.user(AUTH_USERS)
    )
    app.add_handler(incoming_banned_command)

    # BROADCAST Admin Command
    incoming_broadcast_command = MessageHandler(
        broadcast_,
        filters=filters.command(["broadcast"]) & filters.user(AUTH_USERS) & filters.reply
    )
    app.add_handler(incoming_broadcast_command)
    
    # START command
    incoming_start_message_handler = MessageHandler(
        incoming_start_message_f,
        filters=filters.command(["start", f"start@{BOT_USERNAME}"])
    )
    app.add_handler(incoming_start_message_handler)
    
    # COMPRESS command
    incoming_compress_message_handler = MessageHandler(
        incoming_compress_message_f,
        filters=filters.command(["compress", f"compress@{BOT_USERNAME}"])
    )
    app.add_handler(incoming_compress_message_handler)
    
    # CANCEL command
    incoming_cancel_message_handler = MessageHandler(
        incoming_cancel_message_f,
        filters=filters.command(["cancel", f"cancel@{BOT_USERNAME}"]) & filters.chat(chats=AUTH_USERS)
    )
    app.add_handler(incoming_cancel_message_handler)

    # MEMEs COMMANDs
    exec_message_handler = MessageHandler(
        exec_message_f,
        filters=filters.command(["exec", f"exec@{BOT_USERNAME}"]) & filters.chat(chats=AUTH_USERS)
    )
    app.add_handler(exec_message_handler)
    
    # HELP command
    help_text_handler = MessageHandler(
        help_message_f,
        filters=filters.command(["help", f"help@{BOT_USERNAME}"])
    )
    app.add_handler(help_text_handler)
    
    # Telegram command to upload LOG files
    upload_log_f_handler = MessageHandler(
        upload_log_file,
        filters=filters.command(["log", f"log@{BOT_USERNAME}"]) & filters.chat(chats=AUTH_USERS)
    )
    app.add_handler(upload_log_f_handler)
    
    call_back_button_handler = CallbackQueryHandler(
        button
    )
    app.add_handler(call_back_button_handler)

    # run the APPlication
    app.run()
