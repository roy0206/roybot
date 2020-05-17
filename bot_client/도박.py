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

    if message.content == "!도박90":
        await message.channel.send(random.choice(["무난하게 성공!", "성공^_^", "대단해", "럭키 가이", "예상한 결과지 뭐", "축하한다 친구여", "역시나 성공!", "평균입니다!", "이런 개같은 쓰래기 자식 그걸 어떻게 실패하냐 더러운 짜슥"]))

    elif message.content == "!도박80":
        await message.channel.send(random.choice(["무난하게 성공!", "성공^_^", "대단해", "럭키 가이", "예상한 결과지 뭐", "축하한다 친구여", "역시나 성공!", "그걸 실패하냐 에휴", "더럽go 추악han"]))

    elif message.content == "!도박70":
        await message.channel.send(random.choice(["올~~성공이얏!!", "축하해!!", "굿", "이걸 실패하면 호구지!", "대단해!", "ㄷㄷ 성공", "내가 졌어 축하한다 친구여", "그걸 실패하냐 더러운 자식", "개못하누","실패야.. 무튼 그런거임 수고 ㅂ", ]))

    elif message.content == "!도박60":
        await message.channel.send(random.choice(["이걸?", "성공", "대단해", "럭키 가이", "젠장 너가 이겼어!", "축하한다 친구여", "실패야ㅜ 그러게 잘좀 하지", "오늘도 실패 ㅋ", "꽝!꽝!"]))

    elif message.content == "!도박50":
        await message.channel.send(random.choice(["성공!!", "다음 기회에..."]))

    elif message.content == "!도박40":
        await message.channel.send(random.choice(["이걸?", "성공", "대단해", "럭키 가이", "다음 기회에...", "훗 넌 졌어", "실패야ㅜ 그러게 잘좀 하지", "오늘도 실패 ㅋ", "꽝!꽝!", "불쌍한 자식", ]))

    elif message.content == "!도박30":
        await message.channel.send(random.choice(["성공이닷!", "이게 바로 나의 운!", "thiis is me", "다음 기회에...", "그게 될거라 생각하니?", "안타깝군", "망했네연", "왤케 못하니?", "...실패다..","매뤙 실패쥐뤙", ]))

    elif message.content == "!도박20":
        await message.channel.send(random.choice(["올~~성공이얏!!", "축하해!!", "꽝!", "망했네여 ㅜㅜ", "다음 기회에...", "에휴", "어림도 없지", "쯧쯧", "잘 해봐..", "그것도 못하는 바보같은이", ]))

    elif message.content == "!도박10":
        await message.channel.send(random.choice(["1/10을 돌파하다니 ㄷㄷ 미친 놈이구만", "그걸 될거라 생각한 너의 잘못이다", "꽝!", "망했네여 ㅜㅜ", "빠가 자식", "에휴", "어림도 없지", "쯧쯧", "잘 해봐..","그것도 못하는 바보같은이", ]))


def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = ["!도박10", "!도박20", "!도박30", "!도박40", "!도박50", "!도박60", "!도박70", "!도박80", "!도박90"]
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = []


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}