from telegram import Update

def log(update: Update, title):
    with open('db.csv', 'a',encoding="utf8") as file: 
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}\n')
        file.close()
