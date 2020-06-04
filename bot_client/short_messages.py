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

    if message.content.startswith("!업뎃"):
        embed = discord.Embed(title="로이봇이 업데이트가 되였습니다.", description="공지사항 채널에서 없데이트 사항을 확인하세요", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith("!화사멍청이"):
        await message.channel.send("영어 열심히 해라ㅗㅗ")

    if message.content.startswith("!강희수"):
        await message.channel.send("그는 유튜브에서 축튜버란 채널을 운영하고 있습니다")

    if message.content.startswith("!끝"):
        await message.channel.send("다음 끝말잇기 시작시간:다음날 오전 8시[게임 시작전 끝말잇기방에서 채팅 금지]")
        await message.channel.send("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

    if message.content.startswith("!원기별명1"):
        await message.channel.send("원기옥")

    if message.content.startswith("!원기별명2"):
        await message.channel.send("one key")

    if message.content.startswith("톡출"):
        await message.channel.send("출석이 확인되였습니다.관리자가 적립을 완료하면 적립완료라고 보내게 됩니다")

    if message.content.startswith("!화사본명"):
        await message.channel.send("배.선.욱")

    if message.content.startswith("!go"):
        await message.channel.send("오늘 톡엔티 오는 사람?")

    if message.content.startswith("왕 죄수 인정?"):
        await message.channel.send("왕 죄수 인정?")


    
def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = []
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!업뎃", "!화사멍청이", "!강희수", "!끝", "!원기별명1", "톡출", "!화사본명", "!go", "왕 죄수 인정?"]


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}

