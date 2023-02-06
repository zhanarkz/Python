
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("6042719914:AAHYTNKG33cCY3V31WxF1sn-KDnMJXWPIxc").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
#app.add_handler(CommandHandler("play", play_command))
app.add_handler(CommandHandler("day", day2NewYear))

print('server start')
app.run_polling()