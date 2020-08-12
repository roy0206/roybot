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

    if message.content == "!기능":
        embed = discord.Embed(title="로이봇 튜토리얼", description="""로이봇의 튜토리얼입니다.
1. '!핼로'이라고 치면 안녕하세요로 대답
2. '= (식)'으로 게산 가능(자세한건 !설명 계산기)
3.'!시간'으로 현제시간 확인 가능(현제 사용 불가)
4.'!도박(10~90)'으로 입력 숫자 확률로 도박 시행
5.'!이모티콘' 이라 치면 랜덤 이모티콘 보냄
6.'!검색 **'으로 내용을 유튜브에서 검색(현제 불가)
7.'!날씨 (도시이름)'으로 해당 도시의 날씨 확인
8.'!복권'으로 1~46까지의 수 중 7개 랜덤 수 뽑기
9.'!주사위'로 1~6까지의 수 중 하나 뽑기
10.'!이미지 (**)' 으로 **관련 이미지를 보여줌
11.'!가위'or'!바위'or'!보' 로 봇과 가위바위보를 함
12.'!번역 (원하는 단어)' 로 한영 번역 가능
13.'!삭제 (숫자)' 로 메세지 삭제 가능
14.'!내정보'로 내정보와 프사 확인 가능
15.'!설명'으로 설명서 확인 가능
16.'업타임'으로 켜진 시간 확인 가능""", color=0xff0000)
        await message.author.send(embed=embed)
        await message.channel.send("DM으로 도움말을 전송했어요!")

    if message.content == "!기능전체":
        embed = discord.Embed(title="로이봇 튜토리얼", description="""로이봇의 튜토리얼입니다.
1. '!핼로'이라고 치면 안녕하세요로 대답
2. '= (식)'으로 게산 가능(자세한건 !설명 계산기)
3.'!시간'으로 현제시간 확인 가능(현제 사용 불가)
4.'!도박(10~90)'으로 입력 숫자 확률로 도박 시행
5.'!이모티콘' 이라 치면 랜덤 이모티콘 보냄
6.'!검색 **'으로 내용을 유튜브에서 검색(현제 불가)
7.'!날씨 (도시이름)'으로 해당 도시의 날씨 확인
8.'!복권'으로 1~46까지의 수 중 7개 랜덤 수 뽑기
9.'!주사위'로 1~6까지의 수 중 하나 뽑기
10.'!이미지 (**)' 으로 **관련 이미지를 보여줌
11.'!가위'or'!바위'or'!보' 로 봇과 가위바위보를 함
12.'!번역 (원하는 단어)' 로 한영 번역 가능
13.'!삭제 (숫자)' 로 메세지 삭제 가능
14.'!내정보'로 내정보와 프사 확인 가능
15.'!설명'으로 설명서 확인 가능
16.'업타임'으로 켜진 시간 확인 가능""", color=0xff0000)
        await message.channel.send(embed=embed)


    
def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = ["!기능", "!기능전체"]
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = []


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}

