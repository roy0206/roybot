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

    if message.content.startswith("!톡사공 주식목록"):
        embed = discord.Embed(title="주식 목록", description="주식 구매를 원하시면 !주식 (주식번호)를 처주시기 바랍니다.", color=0x00ff00)
        embed.add_field(name="1톡사공 도로공사", value="5000t(10개)", inline=True)
        embed.add_field(name="2톡앤티 스피킹", value="5000t(30개)", inline=True)
        embed.add_field(name="3톡앤티 리딩", value="1800t(30개)", inline=True)
        embed.add_field(name="4톡앤티 봇 전자", value="13000t(10개)", inline=True)
        embed.add_field(name="5톡앤티 과학연구소", value="28000t(5개)", inline=True)
        embed.add_field(name="6왕립방송", value="5000t(10개)", inline=True)
        embed.add_field(name="7TPBS", value="5000t(10개)", inline=True)
        await message.channel.send(embed=embed)


    if message.content.startswith("!주식1"):
        embed = discord.Embed(title="톡사공 도로공사 주식 구매가 예약되셨습니다.", description="주식 구매 가능 여부를 확인하고 주식 구매 완료시 구매 완료라고 보내집니다", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith("!주식2"):
        embed = discord.Embed(title="톡앤티 스피킹 주식 구매가 예약되셨습니다.", description="주식 구매 가능 여부를 확인하고 주식 구매 완료시 구매 완료라고 보내집니다", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith("!주식3"):
        embed = discord.Embed(title="톡앤티 리딩 주식 구매가 예약되셨습니다.", description="주식 구매 가능 여부를 확인하고 주식 구매 완료시 구매 완료라고 보내집니다", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith("!주식4"):
        embed = discord.Embed(title="톡앤티 봇 전자 주식 구매가 예약되셨습니다.", description="주식 구매 가능 여부를 확인하고 주식 구매 완료시 구매 완료라고 보내집니다", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith("!주식5"):
        embed = discord.Embed(title="톡앤티 과학연구소 주식 구매가 예약되셨습니다.", description="주식 구매 가능 여부를 확인하고 주식 구매 완료시 구매 완료라고 보내집니다", color=0x00ff00)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!주식6"):
        embed = discord.Embed(title="왕립방송 주식 구매가 완료되었습니다.", description="주식 구매 가능 여부를 확인하고 주식 구매 완료시 구매 완료라고 보내집니다", color=0x00ff00)
        await message.channel.send(embed=embed)
        
    if message.content.startswith("!주식7"):
        embed = discord.Embed(title="TPBS 주식 구매가 완료되었습니다.", description="주식 구매 가능 여부를 확인하고 주식 구매 완료시 구매 완료라고 보내집니다", color=0x00ff00)
        await message.channel.send(embed=embed)

    
def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = []
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = []

    # startwith 로 비교할 키 입력
    for i in range(1, 6):
        startswith_key.append('!주식%d'%i)

    startswith_key.append('!톡사공 주식목록')

    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}

