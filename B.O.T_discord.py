import discord
import datetime
import random
import urllib
import requests
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



def register_bot(g_content_fun, g_startswith_fun):
    top_dir = 'bot_client'
    file_list = os.listdir(top_dir)
    if '__init__.py' in file_list:
        file_list.remove('__init__.py')

    for i in range(len(file_list)):
        file_name = file_list[i]
        if file_name.endswith('.py'):
            file_name = file_name[:-3]
            exec('from %s.%s import register; register(g_content_fun, g_startswith_fun)'%(top_dir, file_name))

client = discord.Client()
count = 0
roy_money=0

# bot client 등록
g_content_fun = dict()
g_startswith_fun = dict()
register_bot(g_content_fun, g_startswith_fun)
print('start')



@client.event
async def on_ready():
    print(client.user.id)
    print("GOGO")
    print(client.user.name)
    messages = ["코드 수정", "명령어 실행"]
    while True:
       await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
       messages.append(messages.pop(0))
       await asyncio.sleep(10)
    await client.change_presence(status=discord.Status.online, activity=game)



# @client.event
# async def on_member_join(member):
#     role= ""
#     for i in member.server.roles:
#         if i.name == "평민":
#             role = i
#             break
#     await client.add_roles(member, role)



@client.event
async def on_message(message):

    ok = False
    for data in g_content_fun.values():
        for key in data['keys']:
            if message.content == key:
                await data['func'](message)
                ok = True
                break
        if ok : break

    if not ok:
        for data in g_startswith_fun.values():
            for key in data['keys']:
                if message.content.startswith(key):
                    await data['func'](message)
                    ok = True
                    break
            if ok : break



    if not ok:

        # if message.author.bot:
            # return None

        if message.content.startswith("!핼로"):
            embed = discord.Embed(title="안녕하세요", description="안녕하세요 전 고문 로이봇 입니다", color=0x00ff00)
            embed.set_footer(text="만나서 반가워요 ㅎㅎ")
            await message.channel.send(embed=embed)

        if message.content.startswith("!로이스톱모션"):
            embed = discord.Embed(title="로이스톱모션 소개", description="로이스톱모션은 레고로 찍은 스톱모션 영상을 올리는 채널입니다.", color=0x00ff00)
            embed.add_field(name="구독", value="눌러주세요", inline=True)
            embed.add_field(name="좋아요", value="눌러주세요", inline=True)
            embed.set_image(url="https://yt3.ggpht.com/a/AGF-l7-s4GhMfle-FSg2dou4XnfJ0WVIhEoIEOBc8w=s900-c-k-c0xffffffff-no-rj-mo")
            await message.channel.send(embed=embed)

        if message.content.startswith("!축튜버"):
            embed = discord.Embed(title="축튜버 소개", description="축튜버채널은 축구와 관련된 여러가지 정보들을 컨텐츠로한 유튜브 채널입니다", color=0x00ff00)
            embed.add_field(name="구독", value="눌러주세요", inline=True)
            embed.add_field(name="좋아요", value="눌러주세요", inline=True)
            embed.set_image(url="https://yt3.ggpht.com/a-/AOh14GiV9XfMqyf1O4O5IWf5Ax38_r48z_M1jMBtaagYaw=s288-c-k-c0xffffffff-no-rj-mo")
            await message.channel.send(embed=embed)

        if message.content.startswith("!톡앤티"):
            embed = discord.Embed(title="톡앤티", description="톡엔티는 서울시 강서구에 있는 영어 스터디카페이다", color=0x00ff00)
            embed.set_image(url="https://mblogthumb-phinf.pstatic.net/MjAxODA4MjJfMTc0/MDAxNTM0OTAxMTA4OTI1.9aXAOsH_MVB2OjndzmtnLzEttI5CWS1lysWdlNLrQBgg.8OMApyqy8COSgXioyK9Bn1DPQynN1r1QtjzEXLHeVl4g.JPEG.talkandtea/12121211.jpg?type=w800")
            await message.channel.send(embed=embed)



@client.event
async def on_member_join(member):
    fmt = '{1.name} 에 오신것을 환영합니다., {0.mention} 님'
    channel = member.guild.get_channel("channel_id_here")
    await channel.send(fmt.format(member, member.server))


@client.event
async def on_member_remove(member):
    fmt = '{0.mention} 님이 서버에서 나가셨습니다.'
    channel = member.guild.get_channel("channel_id_here")
    await channel.send(fmt.format(member, member.server))


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)



