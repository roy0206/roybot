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


    if message.content == "!강도잡기":
        await message.channel.send(random.choice(["강도를 잡었다!! 벌금을 물어서 100톡을 획득했다", "강도를 놓첬다!!", "강도가 이미 돈을 훔치고 가버렸다.. -300톡", "강도가 사람을 해쳤다!! 수술비400톡"]))

    elif message.content == "!강도잡기 파출소":
        await message.channel.send(random.choice(["강도를 잡었다!! 벌금을 물어서 200톡을 획득했다", "강도를 놓첬다!!", "강도가 이미 돈을 훔치고 가버렸다.. -200톡", "강도가 사람을 해쳤다!! 수술비 200톡"]))

    elif message.content == "!강도잡기 경찰서":
        await message.channel.send(random.choice(["강도를 잡었다!! 벌금을 물어서 500톡을 획득했다", "강도를 잡었다!! 벌금을 물어서 500톡을 획득했다", "강도를 놓첬다!!", "강도가 이미 돈을 훔치고 가버렸다.. -2000톡","강도가 사람을 해쳤다!! 수술비 100톡"]))

    if message.content.startswith("!천둥이벤트"):
        await message.channel.send(random.choice(["천둥을 맞을뻔했다!", "천둥이 집의 지붕을 파괴했다! 수리를 안하면 홍수가 나서 집이 파괴된다(수리비2000톡)", "정전이 일어났다. 정전을 틈타 강도가 처들어 와 1000톡을 훔쳤다","길가다가 천둥을 맞았다! 수술비 500톡", "천둥소리를 자장가 삼아 자고 있다."]))

    if message.content.startswith("!지진이벤트"):
        await message.channel.send(random.choice(["지진에 너무 놀랐다", "집의 벽이 파손되었다! 수리비:가격의30%", "지진구덩이에 빠져서 치료비 100톡이 부과된다", "(가장 저럼한 시설)이 완파되었다","지진이 너무 약하여 아무런 피해도 없없다"]))

def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = ["!강도잡기", "!강도잡기 파출소", "!강도잡기 경찰서"]
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!천둥이벤트", "!지진이벤트"]


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}