from typing import List
import telebot
from telebot.types import Poll

from storage import BOT_TOKEN, CHANNEL, PROXY_USER, PROXY_PASS, PROXY_SERVER
from telebot import apihelper

apihelper.proxy = {'https': 'socks5h://{}:{}@{}'.format(PROXY_USER, PROXY_PASS, PROXY_SERVER)}


class ChannelPublisher:

    def __init__(self, token: str, channel: str):
        self.bot = telebot.TeleBot(token)
        self.channel = channel

    def send_text(self, text: str):
        self.bot.send_message(self.channel, text, parse_mode="markdown")

    def send_poll(self, question: str, options: List[str]):
        poll = Poll(question)
        for o in options:
            poll.add(o)

        self.bot.send_poll(self.channel, poll)
