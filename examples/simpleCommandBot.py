from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello ' + update.message.from_user['first_name'] + '!' '\nI am a *Bot*, click on /help to find out how I can assist you.' , parse_mode = 'Markdown')

def help(bot, update):
    update.message.reply_text("Currently I can't help you with anything, talk to my developers and tell them to add more functions and CommandHandlers!")

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)
    
def unknown(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command, please click at /help to see a list of all available commands.")


"""Start the bot."""  
updater = Updater(token='123456:AAABBCCDDEEEFFFGGHHHIIIJJKKLL') # Copy the Token from the Botfather here
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start)) # Runs the start function declared above when a user writes /start
dp.add_handler(CommandHandler('help', help)) # Runs the help function declared above when a user writes /help
dp.add_handler(MessageHandler(Filters.command, unknown)) # Runs the unkown function declared above when a user writes an unkown command
dp.add_error_handler(error) # Runs the error function declared above when there are any errors in the backend

updater.start_polling()
