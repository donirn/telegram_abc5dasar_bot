#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.

"""
This Bot uses the Updater class to handle the bot.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging, secret

# Essential part of the class
def create(bot, update):
    bot.sendMessage(update.message.chat_id, text='Ayo /ikut game-nya!\nLalu kita /mulai pertarungan ini!')

def join(bot, update):
    bot.sendMessage(update.message.chat_id, text=update.message.from_user.first_name + ' dah gabung, lo kaga ikut?')

def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='Permainan dimulai!')

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def hej(bot, update):
    if update.message.chat_id == -110624104 or update.message.chat_id == 164707028:
        bot.sendMessage(update.message.chat_id, text='Hej, ' + update.message.from_user.first_name + '!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(secret.token)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addHandler(CommandHandler("hej", hej))
    dp.addHandler(CommandHandler("help", help))
    dp.addHandler(CommandHandler("buat", create))
    dp.addHandler(CommandHandler("ikut", join))
    dp.addHandler(CommandHandler("mulai", start))

    # log all errors
    dp.addErrorHandler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
