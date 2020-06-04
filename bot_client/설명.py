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

async def on_message(message):
    if message.content == "!설명":
        embed = discord.Embed(title="설명서입니다.", description="""설명종류"
        1.계산기
        2.날씨
        3.번역
        4.내정보""", color=0x00f3ff)
        embed.set_image(url="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSIoC36iqWHZrhc5Hdi1k92IQoOTNzpgn65PCuEmmpebdwmfulR&usqp=CAU")
        embed.set_footer(text="!설명 (설명종류)로 해당 설명 내용 확인 가능")
        await message.channel.send(embed=embed)

    if message.content == "!설명 계산기":
        embed = discord.Embed(title="계산기 설명서입니다.", description="""= (계산식)
        1.= 뒤에 한칸 띄우고 식을 써주세요.
        2.더하기 빼기는 동일합니다.
        3.곱하기는 *, /로 해주세요
        4.분수,소수 계산 됩니다.
        5.혼합계산 됩니다.
        6.음수계산 됩니다.""", color=0x00f3ff)
        await message.channel.send(embed=embed)

    if message.content == "!설명 날씨":
        embed = discord.Embed(title="날씨 설명서입니다", description="""!날씨 (도시이름)
        1.도시이름에는 한국 도시만 적어주세요.
        2.북한의 도시정보는 안뜹니다.
        3.외국의 도시이름은 안됩니다.
        4.군,구 등은 안됩니다. ㅇㅇ시만 됩니다.""", color=0x00f3ff)
        await message.channel.send(embed=embed)

    if message.content == "!설명 번역":
        embed = discord.Embed(title="번역 설명서입니다.", description="""!번역 (한글)
        1.!번역 후 한칸 띄우고 내용을 적어주세요
        2.영한은 안됩니다.
        3.한영 번역만 됩니다.
        4.이 번역기는 파파고를 이용합니다.
        5.띄여쓰기는 마음대로 하실 수 있습니다.
        6.번역 결과가 늦게 나올 수 있습니다.""", color=0x00f3ff)
        await message.channel.send(embed=embed)

    if message.content == "!설명 내정보":
        embed = discord.Embed(title="내정보 설명서입니다.", description="""!내정보
        1.당신의 디스코드 가입일이 표시됩니다.
        2.프사가 크게 표시됩니다.
        3.디스코드 정보 노출이 싫으시다면 
        이 명령어를 사용하지 마십시오.""", color=0x00f3ff)
        await message.channel.send(embed=embed)

def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    content_key = ["!설명", "!설명 날씨"]
    startswith_key = []

    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}