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
    client = discord.Client()

    if message.content.startswith('!삭제'):
        # if type(message.channel) == discord.channel:
        if message.author._user.name == "ROY0206":
        # if message.author.role._name == "삭제권한":
            command, count = message.content.split(' ')
            den = int(count) + 1
            if den > 0:
                try:
                    client.get_all_channels()
                    async for message in message.channel.history(limit=den):
                        await message.delete()

                    # async for m in client.logs_from(message.channel, limit=den + 1):
                    #     await client.delete_message(m)
                    await message.channel.send(str(den) + "개의 메시지를 삭제하였습니다.")
                    await asyncio.sleep(2)
                    await client.delete_message()

                except discord.errors.Forbidden:
                    await message.channel.send('봇이 권한을 가지고 있지 않습니다.')
                    raise Exception

                except discord.errors.HTTPException:
                    await message.channel.send('알 수 없는 오류가 발생했습니다')
                    raise Exception
            else:
                await message.channel.send("1개 이상의 메시지만 삭제할 수 있습니다!")
        else:
            await message.channel.send('당신은 관리자 권한을 가지고 있지 않습니다.')
        # else:
        #     await message.channel.send('서버 채널에서만 이 명령어를 사용할 수 있습니다.')


    if message.content.startswith('!삭제'):
        # if type(message.channel) == discord.channel:
        if message.author._user.name == "stom":
        # if message.author.role._name == "삭제권한":
            command, count = message.content.split(' ')
            den = int(count) + 1
            if den > 0:
                try:
                    client.get_all_channels()
                    async for message in message.channel.history(limit=den):
                        await message.delete()

                    # async for m in client.logs_from(message.channel, limit=den + 1):
                    #     await client.delete_message(m)
                    await message.channel.send(str(den) + "개의 메시지를 삭제하였습니다.")
                    await asyncio.sleep(2)
                    await client.delete_message()

                except discord.errors.Forbidden:
                    await message.channel.send('봇이 권한을 가지고 있지 않습니다.')
                    raise Exception

                except discord.errors.HTTPException:
                    await message.channel.send('알 수 없는 오류가 발생했습니다')
                    raise Exception
            else:
                await message.channel.send("1개 이상의 메시지만 삭제할 수 있습니다!")
        else:
            await message.channel.send('당신은 관리자 권한을 가지고 있지 않습니다.')
        # else:
        #     await message.channel.send('서버 채널에서만 이 명령어를 사용할 수 있습니다.')


    if message.content.startswith('!삭제'):
        # if type(message.channel) == discord.channel:
        if message.author._user.name == "KR_soccerplayer":
        # if message.author.role._name == "삭제권한":
            command, count = message.content.split(' ')
            den = int(count) + 1
            if den > 0:
                try:
                    client.get_all_channels()
                    async for message in message.channel.history(limit=den):
                        await message.delete()

                    # async for m in client.logs_from(message.channel, limit=den + 1):
                    #     await client.delete_message(m)
                    await message.channel.send(str(den) + "개의 메시지를 삭제하였습니다.")
                    await asyncio.sleep(2)
                    await client.delete_message()

                except discord.errors.Forbidden:
                    await message.channel.send('봇이 권한을 가지고 있지 않습니다.')
                    raise Exception

                except discord.errors.HTTPException:
                    await message.channel.send('알 수 없는 오류가 발생했습니다')
                    raise Exception
            else:
                await message.channel.send("1개 이상의 메시지만 삭제할 수 있습니다!")
        else:
            await message.channel.send('당신은 관리자 권한을 가지고 있지 않습니다.')
        # else:
        #     await message.channel.send('서버 채널에서만 이 명령어를 사용할 수 있습니다.')



    
def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = []
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!삭제"]


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}

