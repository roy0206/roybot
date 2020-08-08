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
from Dtime import Uptime

async def on_message(message):
    if message.content == '!업타임':
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        await message.channel.send(f"{hours}시간 {minitues}분 {seconds}초 동안 켜져있었습니다.")

def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)
    Uptime.uptimeset();

    # message.content == "key" 로 비교할 key 등록
    content_key = ["!업타임"]
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = []

    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys': content_key, 'func': on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys': startswith_key, 'func': on_message}