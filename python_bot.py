import logging

# from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputTextMessageContent, KeyboardButton, \
#     ReplyKeyboardMarkup
# from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, \
#     CallbackQueryHandler, CallbackContext
from scrape import get_course_dollar_hoy, get_blue_dollar, get_blue_dollar_value
from scrape_rub import get_rub_value
from scrape_tenge import get_kzt_value

from telegram import *
from telegram.ext import *

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
default_ars_course = 315
default_rub_course = 65
default_kzt_course = 460

ars_course = default_ars_course
rub_course = default_rub_course
kzt_course = default_kzt_course
num_keys_string = []


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


# func to calculate peso without /command
async def message_ars(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(update.message.text)
    input_ars = int(update.message.text[3:])
    output_ars_usd = round(input_ars / ars_course, 2)
    output_ars_rub = round(input_ars / ars_course * rub_course, 2)
    output_ars_kzt = round(input_ars / ars_course * kzt_course, 2)
    text_ars = str(output_ars_usd) + ' USD\n' + str(output_ars_rub) + ' RUB\n' + str(output_ars_kzt) + ' KZT\n'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_ars)


# func to print actual blue peso rate from dolarhoy
async def dollar_hoy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=get_course_dollar_hoy())


# print all peso rates
async def dollar_blue(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=get_blue_dollar())


# noinspection PyUnusedLocal
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Get rates ars", callback_data=get_blue_dollar()),
            InlineKeyboardButton("Get rates rub", callback_data="this section coming soon"),
            InlineKeyboardButton("Get rates kzt", callback_data='test_test'),
        ],
        # [InlineKeyboardButton("Calc usd", callback_data="this section coming soon")],
        # [InlineKeyboardButton("Calc ars", callback_data="this section coming soon")],
        # [InlineKeyboardButton("Calc rub", callback_data="this section coming soon")],
        # [InlineKeyboardButton("Calc ktz", callback_data="this section coming soon")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Please choose:", reply_markup=reply_markup)


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"{query.data}")


async def main_keyboard(update: Update, context: CallbackContext):
    num_keys = [
        [KeyboardButton("1"), KeyboardButton("2"), KeyboardButton("3"), KeyboardButton("ARS")],
        [KeyboardButton("4"), KeyboardButton("5"), KeyboardButton("6"), KeyboardButton("USD")],
        [KeyboardButton("7"), KeyboardButton("8"), KeyboardButton("9"), KeyboardButton("RUB")],
        [KeyboardButton("<"), KeyboardButton("0"), KeyboardButton("."), KeyboardButton("KZT")]
    ]
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Input value',
                                   reply_markup=ReplyKeyboardMarkup(num_keys))


async def num_keys_recorder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(update.message.text) == 1:
        if update.message.text == '.': #and '.' not in num_keys_string:
            if '.' not in num_keys_string:
                if len(num_keys_string) != 0:
                    num_keys_string.append('.')
                else:
                    num_keys_string.extend(['0', '.'])
            else:
                update.message.text = ''
        elif update.message.text == '<':
            if len(num_keys_string) != 0:
                num_keys_string.pop(len(num_keys_string)-1)
            else:
                update.message.text = ''
        elif int(update.message.text) in range(10):
            num_keys_string.append(update.message.text)
    print(''.join(num_keys_string))
    await update.message.delete()


async def keyboard_calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == 'ARS':
        input_ars = int(''.join(num_keys_string))
        output_ars_usd = round(input_ars / ars_course, 2)
        output_ars_rub = round(input_ars / ars_course * rub_course, 2)
        output_ars_kzt = round(input_ars / ars_course * kzt_course, 2)
        num_keys_string.clear()
        text_ars = str(input_ars) + ' ARS=\n' + str(output_ars_usd) + ' USD\n' + str(output_ars_rub) + ' RUB\n' + str(output_ars_kzt) + ' KZT\n'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text_ars)
    elif update.message.text == 'USD':
        input_usd = int(''.join(num_keys_string))
        output_usd_ars = round(input_usd * ars_course, 2)
        output_usd_rub = round(input_usd * rub_course, 2)
        output_usd_kzt = round(input_usd * kzt_course, 2)
        num_keys_string.clear()
        text_usd = str(input_usd) + ' USD=\n' + str(output_usd_ars) + ' ARS\n' + str(output_usd_rub) + ' RUB\n' + str(output_usd_kzt) + ' KZT\n'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text_usd)
    elif update.message.text == 'RUB':
        input_rub = int(''.join(num_keys_string))
        output_rub_usd = round(input_rub / rub_course, 2)
        output_rub_ars = round(input_rub / rub_course * ars_course, 2)
        output_rub_kzt = round(input_rub / rub_course * kzt_course, 2)
        num_keys_string.clear()
        text_rub = str(input_rub) + ' RUB=\n' + str(output_rub_usd) + ' USD\n' + str(output_rub_ars) + ' ARS\n' + str(output_rub_kzt) + ' KZT\n'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text_rub)
    elif update.message.text == 'KZT':
        input_kzt = int(''.join(num_keys_string))
        output_kzt_usd = round(input_kzt / kzt_course, 2)
        output_kzt_rub = round(input_kzt / kzt_course * rub_course, 2)
        output_kzt_ars = round(input_kzt / kzt_course * ars_course, 2)
        num_keys_string.clear()
        text_kzt = str(input_kzt) + ' KZT=\n' + str(output_kzt_usd) + ' USD\n' + str(output_kzt_rub) + ' RUB\n' + str(output_kzt_ars) + ' ARS\n'
        await context.bot.send_message(chat_id=update.effective_chat.id, text=text_kzt)


async def real_time_rates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global ars_course, rub_course, kzt_course
    ars_course = get_blue_dollar_value()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='ARS updated, please, wait...')
    rub_course = get_rub_value()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='RUB updated, please, wait...')
    kzt_course = get_kzt_value()
    await context.bot.send_message(chat_id=update.effective_chat.id, text='KZT updated, please, wait...')
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Mode changed to real-time rates')


async def default_rates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global ars_course, rub_course, kzt_course
    ars_course = default_ars_course
    rub_course = default_rub_course
    kzt_course = default_kzt_course
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Mode changed to default rates')


async def all_rates(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if ars_course == default_ars_course and rub_course == default_rub_course and kzt_course == default_kzt_course:
        course_status = 'Default courses set'
    else:
        course_status = 'Real-time courses set'
    all_rates_str = f'ARS {ars_course}\nRUB {rub_course}\nKZT {kzt_course}\n{course_status}'
    await context.bot.send_message(chat_id=update.effective_chat.id, text=all_rates_str)


if __name__ == '__main__':
    application = ApplicationBuilder().token('5845321171:AAFNwP1u-ZuHDnwpk0VNjzl4bBZOeSSJAzY').build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('keyboard', main_keyboard))
    application.add_handler(CommandHandler('ars', ars))
    application.add_handler(CommandHandler('usd', usd))
    application.add_handler(CommandHandler('rub', rub))
    application.add_handler(CommandHandler('kzt', kzt))
    application.add_handler(CommandHandler('realtime', real_time_rates))
    application.add_handler(CommandHandler('default', default_rates))
    application.add_handler(CommandHandler('hoy', dollar_hoy))
    application.add_handler(CommandHandler('blue', dollar_blue))
    application.add_handler(CommandHandler('rates', all_rates))
    application.add_handler(CommandHandler('buttons', buttons))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(MessageHandler(filters.Regex(r"(?i)(ars)\s(\d+)"), message_ars))
    application.add_handler(MessageHandler(filters.Regex(r"[a-zA-Z]{3}"), keyboard_calc))
    application.add_handler(MessageHandler(filters.Regex(r"[0-9|<|\.]"), num_keys_recorder))

    application.run_polling()
