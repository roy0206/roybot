import discord
import datetime
import random
import urllib
import requests
import bs4
from selenium import webdriver
import random
from urllib.request import Request
import os
import sys
import json
import asyncio
import os
import datetime
from pytz import timezone, utc

async def on_message(message):
    if message.content == "!시간":
        KST = timezone('Asia/Seoul')
        now = datetime.datetime.now()
        now.replace(tzinfo=KST)
        await message.channel.send((str(now.year) + "년" + str(now.month) + "월" + str(now.day) + "일" + str(now.hour) + "시" + str(now.minute) + "분 입니다"))


def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    content_key = ["!시간"]
    startswith_key = []

    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}