from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from handlers.payments import create_payment_link, check_payment
from config import COURSE_LINK

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Для оплаты курса отправьте команду /pay.")

def pay(update: Update, context: CallbackContext) -> None:
    user_id = update.message.chat_id
    payment_link = create_payment_link(user_id, "usdt")
    if payment_link:
        update.message.reply_text(f"Перейдите по ссылке для оплаты: {payment_link}")
    else:
        update.message.reply_text("Ошибка при создании ссылки оплаты.")

def check(update: Update, context: CallbackContext) -> None:
    user_id = update.message.chat_id
    if check_payment(user_id):
        update.message.reply_text(f"✅ Оплата подтверждена! Доступ: {COURSE_LINK}")
    else:
        update.message.reply_text("Платеж не найден. Попробуйте позже.")

def register_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("pay", pay))
    dispatcher.add_handler(CommandHandler("check", check))
