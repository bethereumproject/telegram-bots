[![Contributing GitHub](/img/Contributing-github.png)](https://www.bethereum.com)

With positive feedback we've received in our [Bitcoitalk thread](https://bitcointalk.org/index.php?topic=2849232.0), the developers of [Bethereum](https://www.bethereum.com) would like to share their first guide.

*To stay up-to-date with our contributions to the crypto-community join our [Telegram group](https://t.me/bethereum)*

## Table of contents
- [Introduction](https://github.com/bethereumproject/telegram-bots/#introduction)
- [Installing](https://github.com/bethereumproject/telegram-bots/#installing)
- [CommandBot](https://github.com/bethereumproject/telegram-bots/#commandbot)
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

**Getting started with your CommandBot code**

The [python-telegram-bot](https://python-telegram-bot.org/) wrapper works the following way:
1. You **declare functions** to tell your bot what to do when someone writes a command beginning with "/" or a message.
2. By adding CommmandHandlers or MessageHandlers you **link these functions to the commands or messages** written by a user.


**Importing modules:**
```python
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
```

Setting up the logging module, this is not something users who interact with the bot will see. It's simply for **debugging**:
```python
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)
```

Declaring the start function:
```python
def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Hello ' + update.message.from_user['first_name'] + '!' '\nI am the *BethereumBot*, click on /help to find out how I can assist you.' , parse_mode = 'Markdown')
```

Logging possible errors, once again you'll see these messages and warnings in the terminal or console:
```python
def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"', update, error)
```

Defining the unkown function, or telling the bot what to do when a user sends an unkown command:
```python
def unknown(bot, update):
     bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command, please click at /help to see a list of all available commands.")
```

Setting up the Updater, this is where you'll add the Token you received from the Botfather:
```python
updater = Updater(token='12345:AAABBCCDDEEFFGGHHIIJJJKKLLMMNN') # Copy the Token from the Botfather here
dp = updater.dispatcher
```

As written above you have to link the functions declared above with commands or messages written by a user:
```python
dp.add_handler(CommandHandler('start', start)) # Runs the start function declared above when a user writes /start
dp.add_handler(MessageHandler(Filters.command, unknown)) # Runs the unkown function declared above when a user writes an unkown command
dp.add_error_handler(error) # Runs the error function declared above when there are any errors in the backend
```



