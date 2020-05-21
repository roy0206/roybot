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

    if message.content.startswith("!지진이벤트 약"):
        await message.channel.send(random.choice(["지진에 너무 놀랐다", "집의 벽이 파손되었다! 수리비:가격의10%", "지진구덩이에 빠져서 치료비 100톡이 부과된다", "진동때문에 어지러워서 토를 했다","지진이 너무 약하여 아무런 피해도 없없다"]))

    if message.content.startswith("!지진이벤트 중"):
        await message.channel.send(random.choice(["지진때문에 창문이 깨졌다. 수리비100톡", "집의 벽이 파손되었다! 수리비:가격의30%", "진동때문에 넘어져서 다쳤다. 수술비 1500톡", "진동을 힘들게 견디고 있다","당신의 사는 집의 지붕이 무너져내렸다 수리비:집 가격의 50%"]))

    if message.content.startswith("!지진이벤트 강"):
        await message.channel.send(random.choice(["지진으로 인하여 댐이 무너져서 마을에 홍수가 일어났다 복구비:20000톡", "집의 벽이 파손되었다! 수리비:가격의60%", "지진구덩이에 빠져서 치료비 3000톡이 부과된다", "(가장 저럼한 시설)이 완파되었다","떨어지는 간판에 머리를 맞아서 머리가 깨졌다. 수술비:10000톡"]))

    if message.content.startswith("!태풍이벤트 약"):
        await message.channel.send(random.choice(["비를 맞으면서 집을 갔다.", "비를 맞으면서 집을 갔다. 너무 추워서 감기에 걸렸다 약값:200톡", "쓰고 있는 우산이 망가졌다. 재구메 비용:300톡", "태풍으로 인하여 현수막이 날라갔다. 제설치:100톡", "집에서 배그나 하고 쉰다"]))

    if message.content.startswith("!태풍이벤트 중"):
        await message.channel.send(random.choice(["바람이 차가웟지만 멀정하다", "비를 맞으면서 집을 갔다. 너무 추워서 저체온증에 걸렸다 약값:1000톡", "당신의 집에 유리창이 깨졋다. 수리비:1000톡", "태풍으로 인하여 간판이 나라가서 당신에 머리에 꽃혓다. 수술비:8000톡", "(가장 저렴한 시설)이 바람에 일부가 날라갔다 복구비:가격의 50%"]))

    if message.content.startswith("!태풍이벤트 강"):
        await message.channel.send(random.choice(["바람에 날라갔다. 수술비:20000톡", "마을(도시)가 쑥대밭이 되었다. 복구비:50000톡", "대부분의 나무와 식물이 뽑혔다. 다시 심기:20000톡", "태풍으로 인하여 집 지붕이 날아갔다. 수리비:집 비용의80%", "비와 강풍을 맞아서 동상에 걸렸다. 수술비:10000톡"]))

    if message.content.startswith("!지진 강도"):
        await message.channel.send(random.choice(["약", "중", "강"]))

    if message.content.startswith("!태풍 강도"):
        await message.channel.send(random.choice(["약", "중", "강"]))

def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = ["!강도잡기", "!강도잡기 파출소", "!강도잡기 경찰서"]
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!천둥이벤트", "!지진이벤트", "!태풍이벤트", "!지진 강도", "!태풍 강도"]


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}