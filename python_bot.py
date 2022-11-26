import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes
from scrape import get_course_dollar_hoy, get_blue_dollar

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
ars_course = 289
rub_course = 65
kzt_course = 460


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Ready to convert you money!\nAvailable currency:\n/usd\n/ars\n/rub\n/kzt\n\n"
                                        "/hoy to get ars courses\n"
                                        "/blue to get blue course")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


# func to calculate peso
async def ars(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_ars = int(context.args[0])
    output_ars_usd = round(input_ars / ars_course, 2)
    output_ars_rub = round(input_ars / ars_course * rub_course, 2)
    output_ars_kzt = round(input_ars / ars_course * kzt_course, 2)
    text_ars = str(output_ars_usd) + ' USD\n' + str(output_ars_rub) + ' RUB\n' + str(output_ars_kzt) + ' KZT\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_ars)


# func to calculate dollar
async def usd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_usd = int(context.args[0])
    output_usd_ars = round(input_usd * ars_course, 2)
    output_usd_rub = round(input_usd * rub_course, 2)
    output_usd_kzt = round(input_usd * kzt_course, 2)
    text_usd = str(output_usd_ars) + ' ARS\n' + str(output_usd_rub) + ' RUB\n' + str(output_usd_kzt) + ' KZT\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_usd)


# func to calculate ruble
async def rub(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_rub = int(context.args[0])
    output_rub_usd = round(input_rub / rub_course, 2)
    output_rub_ars = round(input_rub / rub_course * ars_course, 2)
    output_rub_kzt = round(input_rub / rub_course * kzt_course, 2)
    text_rub = str(output_rub_usd) + ' USD\n' + str(output_rub_ars) + ' ARS\n' + str(output_rub_kzt) + ' KZT\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_rub)


# func to calculate tenge
async def kzt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_kzt = int(context.args[0])
    output_kzt_usd = round(input_kzt / kzt_course, 2)
    output_kzt_rub = round(input_kzt / kzt_course * rub_course, 2)
    output_kzt_ars = round(input_kzt / kzt_course * ars_course, 2)
    text_kzt = str(output_kzt_usd) + ' USD\n' + str(output_kzt_rub) + ' RUB\n' + str(output_kzt_ars) + ' ARS\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_kzt)


async def message_ars(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    input_ars = int(update.message.text[3:])
    output_ars_usd = round(input_ars / ars_course, 2)
    output_ars_rub = round(input_ars / ars_course * rub_course, 2)
    output_ars_kzt = round(input_ars / ars_course * kzt_course, 2)
    text_ars = str(output_ars_usd) + ' USD\n' + str(output_ars_rub) + ' RUB\n' + str(output_ars_kzt) + ' KZT\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_ars)


async def dollar_hoy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dollar_hoy_courses = get_course_dollar_hoy()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=dollar_hoy_courses)


async def dollar_blue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dollar_hoy_courses = get_blue_dollar()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=dollar_hoy_courses)


if __name__ == '__main__':
    application = ApplicationBuilder().token('5845321171:AAFNwP1u-ZuHDnwpk0VNjzl4bBZOeSSJAzY').build()
    start_handler = CommandHandler('start', start)
    # echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    ars_handler = CommandHandler('ars', ars)
    usd_handler = CommandHandler('usd', usd)
    rub_handler = CommandHandler('rub', rub)
    kzt_handler = CommandHandler('kzt', kzt)
    new_handler = MessageHandler(filters.Regex(r"(?i)(ars)\s(\d+)"), message_ars)
    dollar_hoy_handler = CommandHandler('hoy', dollar_hoy)
    dollar_blue_handler = CommandHandler('blue', dollar_blue)

    application.add_handler(start_handler)
    # application.add_handler(echo_handler)
    application.add_handler(ars_handler)
    application.add_handler(usd_handler)
    application.add_handler(rub_handler)
    application.add_handler(kzt_handler)
    application.add_handler(new_handler)
    application.add_handler(dollar_hoy_handler)
    application.add_handler(dollar_blue_handler)

    application.run_polling()
