# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime
from spy import *
#import play
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'/hi\n/time\n/sum\n/help')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split() # /sum 123 534543
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')

async def day2NewYear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'{days2NY()}')


# async def play_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     log(update, context)
#     mes = update.message.text.split()
#     #await update.message.reply_text(play.showMatrix())
#     await update.message.reply_text(int(mes[1]))
#     await update.message.reply_text(play.player(int(mes[1])))