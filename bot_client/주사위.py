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

    if message.content.startswith('!주사위'):

        randomNum = random.randrange(1, 7)
        print(randomNum)
        if randomNum == 1:
            await  message.channel.send(embed=discord.Embed(description=':game_die: '+ ':one:'))
        if randomNum == 2:
            await  message.channel.send(embed=discord.Embed(description=':game_die: ' + ':two:'))
        if randomNum ==3:
            await  message.channel.send(embed=discord.Embed(description=':game_die: ' + ':three:'))
        if randomNum ==4:
            await  message.channel.send(embed=discord.Embed(description=':game_die: ' + ':four:'))
        if randomNum ==5:
            await  message.channel.send(embed=discord.Embed(description=':game_die: ' + ':five:'))
        if randomNum ==6:
            await  message.channel.send(embed=discord.Embed(description=':game_die: ' + ':six: '))




    
def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = []
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!주사위"]


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}

