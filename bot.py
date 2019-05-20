# coding=utf-8
# Archivo: bot
# Descripción: el bot se ejecutará desde este archivo. Aquí se asignarán las funciones handler del archivo handlers.py
# a una llamada de la API.

import logging
import handlers
from telegram.ext import Updater, InlineQueryHandler, ChosenInlineResultHandler, CallbackQueryHandler,\
    CommandHandler, MessageHandler, Filters, PreCheckoutQueryHandler
from bot_tokens import BOT_TOKEN

# Console logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def stop_bot(updater):
    # Función que da la señal al updater para que deje de hacer pooling
    logger.info("Apagando bot...")
    updater.stop()
    logger.info("Bot apagado")


def main():
    updater = Updater(BOT_TOKEN)
    h = updater.dispatcher.add_handler

    # Asignación de hanlders
    h(CommandHandler('start', handlers.start))
    h(CommandHandler('help', handlers.help))
    h(CommandHandler('more', handlers.more))
    h(CommandHandler('donate', handlers.donate))
    h(InlineQueryHandler(handlers.inline_query))

    # Iniciar bot, comenzar a hacer pooling
    updater.start_polling()

    # CONSOLA
    while True:
        inp = raw_input("")
        if inp:
            input_c = inp.split()[0]
            args = inp.split()[1:]
            strig = ""
            for e in args:
                strig = strig + " " + e

            if input_c == "stop":
                stop_bot(updater)
                break

            else:
                print "Comando desconocido"


if __name__ == '__main__':
    main()
