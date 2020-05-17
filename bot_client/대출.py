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


def range(money):
    if money<5000:
        return "5000 미만"
    elif money>=5000 and money<10000:
        return "5000 이상"
    elif money>=10000:
        return "10000 이상"

def penalty(money):
    if money<5000:
        return "-10"
    elif money>=5000 and money<10000:
        return "-30"
    elif money>=10000 and money<50000:
        return "-50"
    elif money>=50000:
        return "-90"


async def on_message(message):
    learn = message.content.split(" ")
    money = learn[1]
    money_int = int(money)
    print(roy_money)


    if money_int <= 100000:
        embed = discord.Embed(title=money + "대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                             "\n주의사항:" + range(money_int) + " 대출시 월급보너스" + penalty(money_int) + "%가 됩니다(전체)", color=0x00ff00)
        await message.channel.send(embed=embed)


    if message.content.startswith('!대출 상환') or message.content.startswith('!대출상환'):
        embed = discord.Embed(title="대출 상환되셨습니다.", description="잠시만 기다리십시오 상환중입니다.", color=0x00ff00)
        embed.set_footer(text="돈을 다 값으셨다면 - 월급이 원상복귀 됩니다.")
        await message.channel.send(embed=embed)

        


    
def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = []
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!대출"]


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}

