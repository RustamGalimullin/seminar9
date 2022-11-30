from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

bot = Bot(token='5983929855:AAEau7gLvbrzJXkPkhyLFT513mNcNhInrZc')
updater = Updater(token='5983929855:AAEau7gLvbrzJXkPkhyLFT513mNcNhInrZc')
dispahather = updater.dispatcher

A = 0
B = 1

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет,\nКак у тебя дела?")
    return A



def howareyou(update, context):
    text = update.message.text
    if 'хор' in text.lower():
        context.bot.send_message(
            update.effective_chat.id, "Я рад что у тебя все хорошо")
    else:
        context.bot.send_message(
            update.effective_chat.id, "не переживай")      
    context.bot.send_message(
            update.effective_chat.id, "Как у тебя погода?") 
    return B


def weather(update, context):
    text = update.message.text
    if 'хор' in text.lower():
        context.bot.send_message(
            update.effective_chat.id, "Я рад что у тебя все хорошо")
    else:
        context.bot.send_message(
            update.effective_chat.id, "У меня тоже солнце")      
    context.bot.send_message(
            update.effective_chat.id, "У природы нет плохой погоды")
    
    return ConversationHandler.END   


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')


start_handler = CommandHandler("start", start)
massage_handler = MessageHandler(Filters.text, howareyou)
mes_weather_handler = MessageHandler(Filters.text, weather)
mes_canc_handler = MessageHandler(Filters.text, cancel)


#Conv_handler = ConversationHandler(entry_points=[start_handler],states={A: [massage_handler], B: [mes_weather_handler]}, fallbacks=[mes_canc_handler])

dispahather.add_handler(start_handler)
dispahather.add_handler(massage_handler)
dispahather.add_handler(mes_weather_handler)
dispahather.add_handler(mes_canc_handler)


updater.start_polling()
updater.idle()