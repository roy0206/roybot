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


    if message.content.startswith('!번역'):
        command, text = message.content.split(maxsplit=1)

        client_id = "UZBA4BAXuxx4hWLwQMKD"
        client_secret = "kiI0nYPW0z"

        url = "https://openapi.naver.com/v1/papago/n2mt"
        encText = urllib.parse.quote(text)
        data = "source=ko&target=en&text=" + encText

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)

        response = urllib.request.urlopen(request, data=data.encode("utf-8"))

        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            data = response_body.decode('utf-8')
            data = json.loads(data)
            tranText = data['message']['result']['translatedText']
        else:
            print("Error Code:" + rescode)

        print('번역된 내용 :', tranText)

        embed = discord.Embed(
            title='한글->영어 번역결과',
            description=tranText,
            colour=discord.Colour.green()
        )
        await message.channel.send(embed=embed)
        


    
def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = []
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!번역"]


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}

