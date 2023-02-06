from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime



def calcrun(usrerexp):
    return eval(usrerexp)

def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = open('db.csv', 'a')
    file.write(f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()    


def days2NY():
    now = datetime.today()
    NY = datetime(now.year + 1, 1, 1)
    d = NY-now
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    return ('До нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss))

