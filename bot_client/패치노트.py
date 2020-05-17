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

    if message.content.startswith("!패치노트"):
        embed = discord.Embed(title="로이봇 패치노트", description="""1.0.1 버전: 안녕->안녕하세요
        
1.0 2버젼:톡엔티 전용 특정 메시지&
   유튜버 소개(임베드)
   
1.0.3버전:'!계산기'&'!시간 추가'

1.0.4버전:'!대출','!대출상환','!톡출',
   '!로이봇'(듀토리얼) 추가
   
1.1.0버전:'!날씨','!검색','!이모티콘','!복권',
   '!가위,!바위,!보','주사위 추가
   기존 명령어 몇몇 수정&패치노트 추가""", color=0x00ff00)
        await message.channel.send(embed=embed)


    
def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = []
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!패치노트"]


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}

