from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot_commands import*

app = ApplicationBuilder().token("5867080974:AAH3Jxx3lH8vCjwisHXrKMaC82jWUG9HLwM").build()
app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))

print('ok')
app.run_polling()
