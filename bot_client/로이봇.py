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

    if message.content.startswith("!로이봇"):
        embed = discord.Embed(title="로이봇 튜토리얼", description="로이봇의 튜토리얼입니다", color=0xff0000)
        embed.add_field(name="1. '!핼로'이라고 치면 안녕하세요로 대답", value=".", inline=True)
        embed.add_field(name="2. '!로이스톱모션' 이라고 치면 로이스톱모션 소개", value=".", inline=True)
        embed.add_field(name="3. '!축튜버' 라고 치면 축튜버 소개", value=".", inline=True)
        embed.add_field(name="4. '!계산기' (+or-or*or/) 숫자 숫자 입력하면 계산해줌", value=".", inline=True)
        embed.add_field(name="5. '!시간' 이러고 치면 현제시간 알려줌", value=".", inline=True)
        embed.add_field(name="6. '!톡앤티' 라고 치면 톡엔티 소개", value=".", inline=True)
        embed.add_field(name="7. '!도박(확률:10~90)' 이라고 치면 선택 숫자에 해당하는 확률로 도박 시행", value=".", inline=True)
        embed.add_field(name="8. '!이모티콘' 이라 치면 랜덤 이모티콘 보냄", value=".", inline=True)
        embed.add_field(name="9. '!검색 ** '으로 원하는 것을 유튜브에서 검색(현제 불가)", value=".", inline=True)
        embed.add_field(name="10. '!날씨 (도시이름)'으로 해당 도시의 이름 알려줌", value=".", inline=True)
        embed.add_field(name="11. '!복권'으로 1~46까지의 수 중 7개 랜덤 수 뽑기", value=".", inline=True)
        embed.add_field(name="12. '!대출' 1000~100000(톡 없이) 로 대출 가능", value=".", inline=True)
        embed.add_field(name="13. '!대출상환' 으로 돈 값기", value=".", inline=True)
        embed.add_field(name="14. '!주사위' 로 1~6까지의' 수 중 랜덤으로 하나 뽑아줌", value=".", inline=True)
        embed.add_field(name="15. '!go' 하면 톡엔티 오는사람 메세지 보내짐", value=".", inline=True)
        embed.add_field(name="16. '!이미지 (**)' 으로 **관련 이미지를 보여줌", value=".", inline=True)
        embed.add_field(name="17. '가위'or'바위'or'보' 로 봇과 가위바위보를 함", value=".", inline=True)
        embed.add_field(name="18. '!끝'으로 끝말잇기를 끝냄", value=".", inline=True)
        embed.add_field(name="19. '!톡사공 주식목록' 으로 주식 목록 확인 가능", value=".", inline=True)
        embed.add_field(name="20. '!주식(주식번호)' 으로 주식 구매 예약/구매 완료되면 자료실에 없대이트", value=".", inline=True)
        embed.add_field(name="21. '!번역 (원하는 단어)' 로 한영 번역 가능", value=".", inline=True)
        embed.add_field(name="21. '!삭제 (숫자)' 로 메세지 삭제 가능", value=".", inline=True)
        await message.channel.send(embed=embed)



    
def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = []
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!로이봇"]


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}

