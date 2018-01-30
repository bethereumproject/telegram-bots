import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters

updater = Updater(token='692394:IEWIWJ23828') # Insert the token of your bot here
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

def start_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="What can this bot do? \n \n Welcome to the Bethereum Bot, click on the commands to get a response from bot. \n\n Bethereum communities: \n /telegram - Bethereum telegram \n /reddit - Bethereum reddit \n /twitter - Bethereum twitter \n /facebook - Bethereum facebook \n /instagram - Bethereum instagram \n /blog - Bethereum medium \n \n Usefull links: \n /website - The official Bethereum website \n /whitepaper - Bethereum whitepaper \n /introvideo - Blockchain-powered social betting \n /news - Get the latest news about Bethereum \n \n /contact - Contact the Bethereum team")

def telegram_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="https://t.me/bethereum")

def reddit_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="reddit.com/r/bethereum")

def twitter_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="https://twitter.com/bethereumteam")

def facebook_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="https://www.facebook.com/bethereumproject/")

def instagram_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="https://www.instagram.com/bethereum/")
    
def blog_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="https://medium.com/@bethereum")
    
def website_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="https://www.bethereum.com/")
    
def whitepaper_func(bot, update):
    bot.send_document(chat_id=update.message.chat_id, document='IHFEUHEU32239EJE') # Insert document_id of your whitepaper
    
def introvideo_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="https://www.youtube.com/watch?v=10l0kxPf3iE")
    
def news_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="1. Bethereum has been chosen as the only blockchain betting project to present at the ICE Totally Gaming conference in London on February 7th 2018! \n \n 2. Bethereum is a Platinum partner at the Blockchain & Bitcoin Conference on February 13th, 2018 in St. Petersburg, Russia!")
    
def contact_func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=" @robertadmin on telegram \n team@bethereum.com")

start_handler = CommandHandler('start', start_func)
telegram_handler = CommandHandler('telegram', telegram_func)
reddit_handler = CommandHandler('reddit', reddit_func)
twitter_handler = CommandHandler('twitter', twitter_func)
facebook_func = CommandHandler('facebook', facebook_func)
instagram_func = CommandHandler('instagram', instagram_func)
blog_func = CommandHandler('blog', blog_func)
website_func = CommandHandler('website', website_func)
whitepaper_func = CommandHandler('whitepaper', whitepaper_func)
introvideo_func = CommandHandler('introvideo', introvideo_func)
news_func = CommandHandler('news', news_func)
contact_func = CommandHandler('contact', contact_func)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(telegram_handler)
dispatcher.add_handler(reddit_handler)
dispatcher.add_handler(twitter_handler)
dispatcher.add_handler(facebook_func)
dispatcher.add_handler(instagram_func)
dispatcher.add_handler(blog_func)
dispatcher.add_handler(website_func)
dispatcher.add_handler(whitepaper_func)
dispatcher.add_handler(introvideo_func)
dispatcher.add_handler(news_func)
dispatcher.add_handler(contact_func)

updater.start_polling()