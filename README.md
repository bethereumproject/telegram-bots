[![Contributing GitHub](/img/Contributing-github.png)](https://www.bethereum.com)

With positive feedback we've received in our [Bitcoitalk thread](https://bitcointalk.org/index.php?topic=2849232.0), the developers of [Bethereum](https://www.bethereum.com) would like to share their first guide.

*To stay up-to-date with our contributions to the crypto-community join our [Telegram group](https://t.me/bethereum)*

## Table of contents
- [Introduction](https://github.com/bethereumproject/telegram-bots/#introduction)
- [Installing](https://github.com/bethereumproject/telegram-bots/#installing)
- [Use-cases](https://github.com/bethereumproject/telegram-bots/#use-cases)
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

## Use-cases
Telegram is one of the most used messengers in the crypto-community and therefore it's a crucial asset for any Cryptocurrency related group. These bots provide the following functionality:

### CommandBot
Simple way to communicate the most important information to your members and supporters, such as:
- Social Media links
- News
- PR contacts
- Any repetative questions
- Telegram user verification

**Getting started with your CommandBot code**
```
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
```






