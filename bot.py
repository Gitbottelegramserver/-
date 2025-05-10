from telegram.ext import Updater
from config import TELEGRAM_TOKEN
from handlers import register_handlers

def main():
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    register_handlers(dispatcher)
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
