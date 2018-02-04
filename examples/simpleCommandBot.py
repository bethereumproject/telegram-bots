from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
import logging

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello ' + update.message.from_user['first_name'] + '!' '\nI am the *BethereumBot*, click on /help to find out how I can assist you.' , parse_mode = 'Markdown')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)
    
def unknown(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command, please click at /help to see a list of all available commands.")


"""Start the bot."""  

# Set up the Updater
updater = Updater(token='12345:AAABBCCDDEEFFGGHHIIJJJKKLLMMNN')
dp = updater.dispatcher

dp.add_handler(CommandHandler('start', start))
dp.add_handler(CommandHandler('help', help))
dp.add_handler(CommandHandler('telegram', telegram))
dp.add_handler(CommandHandler('reddit', reddit))
dp.add_handler(CommandHandler('twitter', twitter))
dp.add_handler(CommandHandler('facebook', facebook))
dp.add_handler(CommandHandler('instagram', instagram))
dp.add_handler(CommandHandler('blog', blog))
dp.add_handler(CommandHandler('website', website))
dp.add_handler(CommandHandler('whitepaper', whitepaper))
dp.add_handler(CommandHandler('introvideo', introvideo))
dp.add_handler(CommandHandler('news', news))
dp.add_handler(CommandHandler('contact', contact))
dp.add_handler(MessageHandler(Filters.command, unknown))
dp.add_error_handler(error)

updater.start_polling()
