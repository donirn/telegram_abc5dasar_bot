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

from telegram.ext import Updater, CommandHandler
import logging
import secret
from model.game import *

# Essential part of the file
game = Game()
currentChat_id = 0


def create(bot, update):
    if checkChatId(update.message.chat_id) and game.create():
        bot.sendMessage(update.message.chat_id, text='Ayo /ikut game-nya!\nLalu kita /mulai pertarungan ini!')


def join(bot, update):
    if checkChatId(update.message.chat_id) and game.join(update.message.from_user.username):
        bot.sendMessage(update.message.chat_id, text=update.message.from_user.first_name + ' sudah bergabung. Ayo /mulai permainannya!')


def start(bot, update):
    if checkChatId(update.message.chat_id) and game.start():
        bot.sendMessage(update.message.chat_id, text='Permainan dimulai! Ketik /j [jawaban] untuk menjawab.')
        bot.sendMessage(update.message.chat_id, text=game.question.getText())
        # TODO give information about answering command, it is /j

        global currentChat_id
        currentChat_id = update.message.chat_id
        updater.job_queue.put(end, interval=20, repeat=False)


def answer(bot, update):
    if checkChatId(update.message.chat_id) and game.isStarted:
        username = update.message.from_user.username
        answer_text = update.message.text[3:]
        # TODO user shouldn't answer if they already gave correct answer
        # TODO end question if every one already gave correct answers
        if game.answerQuestion(username, answer_text):
            bot.sendMessage(update.message.chat_id, text='Jawaban benar!')
        else:
            bot.sendMessage(update.message.chat_id, text='Jawaban salah!')


def end(bot):
    if game.endQuestion():
        bot.sendMessage(currentChat_id, text='Permainan berakhir!')
        winner = game.checkWinner()
        if winner is None:
            bot.sendMessage(currentChat_id, text='Tidak ada pemenang pada permainan ini.')
        else:
            bot.sendMessage(currentChat_id, text='Pemenangnya adalah @' + winner)
        game.end()
    else:
        # TODO game is not yet over, startQuestion again
        # TODO give elimination members notice if there is any
        pass


# Util function
def checkChatId(chat_id):
    return chat_id == -110624104 or chat_id == 164707028


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def hej(bot, update):
    if checkChatId(update.message.chat_id):
        bot.sendMessage(update.message.chat_id, text='Hej, ' + update.message.from_user.first_name + '!')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='Help!')


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


# Create the EventHandler and pass it your bot's token.
updater = Updater(secret.token)


def main():
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.addHandler(CommandHandler("hej", hej))
    dp.addHandler(CommandHandler("help", help))
    dp.addHandler(CommandHandler("buat", create))
    dp.addHandler(CommandHandler("ikut", join))
    dp.addHandler(CommandHandler("mulai", start))
    dp.addHandler(CommandHandler("j", answer))

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
