[![Contributing GitHub](/img/Contributing-github.png)](https://www.bethereum.com)

With positive feedback we've received in our [Bitcoitalk thread](https://bitcointalk.org/index.php?topic=2849232.0), the developers of [Bethereum](https://www.bethereum.com) would like to share their first guide.

*To stay up-to-date with our contributions to the crypto-community join our [Telegram group](https://t.me/bethereum)*

## Table of contents
- [Introduction](https://github.com/bethereumproject/telegram-bots/#introduction)
- [Installing](https://github.com/bethereumproject/telegram-bots/#installing)
- [CommandBot](https://github.com/bethereumproject/telegram-bots/#commandbot)
    - [Before you begin](https://github.com/bethereumproject/telegram-bots/#before-you-begin)
    - [Getting started with your code](https://github.com/bethereumproject/telegram-bots/#getting-started-with-your-code)
    - [Defining the functions](https://github.com/bethereumproject/telegram-bots/#defining-the-functions)
    - [Setting up the bot API token](https://github.com/bethereumproject/telegram-bots/#setting-up-the-bot-api-token)
    - [Linking your functions](https://github.com/bethereumproject/telegram-bots/#linking-your-functions)
- [QueryBot](https://github.com/bethereumproject/telegram-bots/#querybot)
- [GroupButler](https://github.com/bethereumproject/telegram-bots/#groupmanager)

## Introduction
This is a guide for the crypto community, all current and future Crypto project developers and any other enthusiasts.
I'd like to credit [python-telegram-bot](https://python-telegram-bot.org/) for creating the wrapper used in the guides.

## Installing

You can install or upgrade python-telegram-bot with:
```
$ pip install python-telegram-bot --upgrade
```
Or you can install from source with:
```
$ git clone https://github.com/python-telegram-bot/python-telegram-bot --recursive
$ cd python-telegram-bot
$ python setup.py install
```

## CommandBot
Simple way to communicate the most important information to your members and supporters, such as:
- Social Media links
- News
- PR contacts
- Any repetative questions
- Telegram user verification

### Before you begin
Open up [@Botfather](https://telegram.me/BotFather) on Telegram to create your new bot and receive the **API token**.

### Getting started with your code

The [python-telegram-bot](https://python-telegram-bot.org/) wrapper we'll be using works the following way:
1. You **define functions** to tell your bot what to do when someone writes a command beginning with "/" or a message.
2. By adding CommmandHandlers or MessageHandlers you **link these functions to the commands or messages** written by a user.  
**Note:** see the documentation for [CommandHandlers](http://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.commandhandler.html) and [MessageHandlers](http://python-telegram-bot.readthedocs.io/en/latest/telegram.ext.messagehandler.html)

**Importing modules:**
```python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
```

**Setting up the logging module:**
```python
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
```

### Defining the functions
Defining the start function:
```python
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello ' + update.message.from_user['first_name'] + '!' '\nI am the *BethereumBot*, click on /help to find out how I can assist you.' , parse_mode = 'Markdown')
```

Function for possible errors caused by updates:
```python
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)
```

Defining the unkown function:
```python
def unknown(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command, please click at /help to see a list of all available commands.")
```
**Note:** Look at the following documentation for possible [Bot actions](http://python-telegram-bot.readthedocs.io/en/latest/telegram.bot.html#)

### Setting up the bot API token
Setting up the Updater:
```python
updater = Updater(token='12345:AAABBCCDDEEFFGGHHIIJJJKKLLMMNN') # Copy the Token from the Botfather here
dp = updater.dispatcher
```

### Linking your functions
You have to link the functions declared above with commands or messages written by a user:
```python
dp.add_handler(CommandHandler('start', start)) # Runs the start function declared above when a user writes /start
dp.add_handler(MessageHandler(Filters.command, unknown)) # Runs the unkown function declared above when a user writes an unkown command
dp.add_error_handler(error) # Runs the error function declared above when there are any errors in the backend
```

### Starting your bot
The following line of code will tell the bot to **start getting updates from Telegram:**
```python
updater.start_polling()
```


