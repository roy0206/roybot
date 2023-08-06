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


async def on_message(message):

    s = ['가위','바위','보']
    if message.content==('!가위'):
        r = random.choice(s)
        if r == '가위':
            await message.channel.send("봇의 선택:" + r + "\n비겼습니다. 다시한번 하세요")
        elif r == '바위':
            await message.channel.send("봇의 선택:" + r + "\n졌습니다.")
        elif r == '보':
            await message.channel.send("봇의 선택:" + r + "\n이겼습니다.")

    elif message.content==('!바위'):
        r = random.choice(s)
        if r == '바위':
            await message.channel.send("봇의 선택:" + r + "\n비겼습니다.")
        elif r == '보':
            await message.channel.send("봇의 선택:" + r + "\n졌습니다. 아쉬워")
        elif r == '가위':
            await message.channel.send("봇의 선택:" + r + "\n이겼습니다.")

    elif message.content==('!보'):
        r = random.choice(s)
        if r == '보':
            await message.channel.send("봇의 선택:" + r + "\n비겼습니다.")
        elif r == '가위':
            await message.channel.send("봇의 선택:" + r + "\n졌습니다.")
        elif r == '바위':
            await message.channel.send("봇의 선택:" + r + "\n이겼습니다.  정말로")



    
def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = ["!가위", "!바위", "!보"]
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = []


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}

