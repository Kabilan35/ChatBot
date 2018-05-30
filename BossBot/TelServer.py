import telepot
import time
import urllib3
from config import *
import json
import Bot
import tflearn
import tensorflow as tf
import subprocess
import Main
import sys
import _thread
from pymongo import MongoClient

proxy_url = "http://proxy.server:3128"
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

client = MongoClient("mongodb://admin:pass@bossdb-shard-00-00-w54dc.mongodb.net:27017,bossdb-shard-00-01-w54dc.mongodb.net:27017,bossdb-shard-00-02-w54dc.mongodb.net:27017/test?ssl=true&replicaSet=BOSSDB-shard-0&authSource=admin&retryWrites=true")
db = client.database

bot = telepot.Bot(BOT_TOKEN)
prevText = {}
prevReply = {}
permAdmin = [395906775]
people = []
admin = [395906775]

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)
    if content_type == 'text':
        if chat_id not in people:
            bot.sendMessage(chat_id, "Hello! I'm the BOSSBot. How can i help you?")
            people.append(chat_id)
        if chat_id:
            reply = Bot.response(msg["text"], chat_id)
            prevText[chat_id] = msg["text"]
            prevReply[chat_id] = reply
            if reply == "":
                Bot.databas(msg["text"]," ",chat_id)
                bot.sendMessage(chat_id, "Not trained to do that yet")
            else:
                bot.sendMessage(chat_id, reply)
            print(prevReply, prevText)
    

bot.message_loop(handle)

print('Listening ...')
while 1:
    time.sleep(10)
