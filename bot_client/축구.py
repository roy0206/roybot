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
    if message.content.startswith("!경기시작"):
        embed = discord.Embed(title="축구 경기를 시작합니다.", description="""경기규칙
    1.경기는 총 전반 15턴 후반 15턴으로 진행됩니다.
    2.경기중 채팅시 '-어쩌구' 식으로 해주세요""", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith("드리블1"):
        await message.channel.send(random.choice(["화려한 드리블!! 모두 재치고 바로 슛!", "무난한 드리블 그리고 패스.", "드리블이 걸렸지만 라인 밖으로 나갑니다!! 드로잉!!", "빠른 드리블 후 패스합니다.", "아 아쉽게 막힙니다. 상대 선수가 드리블 합니다!!", "아 막힙니다... 상대선수의 패스!", "아 수비수에 걸리네요. 상대의 슈팅찬스입니다!!", "공이 흘렀네요.. 상대의 드로잉!"]))
    if message.content.startswith("드리블2"):
        await message.channel.send(random.choice(["화려한 드리블!! 모두 재치고 바로 슛!", "무난한 드리블 그리고 패스.", "드리블이 걸렸지만 라인 밖으로 나갑니다!! 드로잉!!", "빠른 드리블 후 패스합니다.!", "아 아쉽게 막힙니다. 상대 선수가 드리블 합니다!!" "아 막힙니다... 상대선수의 패스!", "아 수비수에 걸리네요. 상대의 슈팅찬스입니다!!", "공이 흘렀네요.. 상대의 드로잉!"]))
    if message.content.startswith("드리블3"):
        await message.channel.send(random.choice(["화려한 드리블!! 모두 재치고 바로 슛!", "무난한 드리블 그리고 패스.", "드리블이 걸렸지만 라인 밖으로 나갑니다!! 드로잉!!", "빠른 드리블 후 패스합니다.", "오오!! 빠르게 달려나간뒤 패스", "아 아쉽게 막힙니다. 상대 선수가 드리블 합니다!!", "아 막힙니다... 상대선수의 패스!", "아 수비수에 걸리네요. 상대의 슈팅찬스입니다!!", "공이 흘렀네요.. 상대의 드로잉!"]))
    if message.content.startswith("드리블4"):
        await message.channel.send(random.choice(["화려한 드리블!! 모두 재치고 바로 슛!", "무난한 드리블 그리고 패스.", "드리블이 걸렸지만 라인 밖으로 나갑니다!! 드로잉!!", "빠른 드리블 후 패스합니다.", "오오!! 빠르게 달려나간뒤 패스", "아 아쉽게 막힙니다. 상대 선수가 드리블 합니다!!", "아 막힙니다... 상대선수의 패스!", "아 수비수에 걸리네요. 상대의 슈팅찬스입니다!!", "공이 흘렀네요.. 상대의 드로잉!"]))
    if message.content.startswith("드리블5"):
        await message.channel.send(random.choice(["화려한 드리블!! 모두 재치고 바로 슛!", "무난한 드리블 그리고 패스.", "드리블이 걸렸지만 라인 밖으로 나갑니다!! 드로잉!!", "빠른 드리블 후 패스합니다.", "오오!! 빠르게 달려나간뒤 패스", "안정적인 드리블 후 슈팅!", "아 아쉽게 막힙니다. 상대 선수가 드리블 합니다!!", "아 막힙니다... 상대선수의 패스!", "아 수비수에 걸리네요. 상대의 슈팅찬스입니다!!", "공이 흘렀네요.. 상대의 드로잉!"]))
    if message.content.startswith("드리블6"):
        await message.channel.send(random.choice(["화려한 드리블!! 모두 재치고 바로 슛!", "무난한 드리블 그리고 패스.", "드리블이 걸렸지만 라인 밖으로 나갑니다!! 드로잉!!", "빠른 드리블 후 패스합니다.", "오오!! 빠르게 달려나간뒤 패스", "안정적인 드리블 후 슈팅!", "아 아쉽게 막힙니다. 상대 선수가 드리블 합니다!!", "아 막힙니다... 상대선수의 패스!", "아 수비수에 걸리네요. 상대의 슈팅찬스입니다!!", "공이 흘렀네요.. 상대의 드로잉!"]))
    if message.content.startswith("드리블7"):
        await message.channel.send(random.choice(["화려한 드리블!! 모두 재치고 바로 슛!", "무난한 드리블 그리고 패스.", "드리블이 걸렸지만 라인 밖으로 나갑니다!! 드로잉!!", "빠른 드리블 후 패스합니다.", "오오!! 빠르게 달려나간뒤 패스", "안정적인 드리블 후 슈팅!", "엄청난 돌파력!! 전부 제치고 강슛!", "아 아쉽게 막힙니다. 상대 선수가 드리블 합니다!!", "아 막힙니다... 상대선수의 패스!", "아 수비수에 걸리네요. 상대의 슈팅찬스입니다!!", "공이 흘렀네요.. 상대의 드로잉!"]))
    if message.content.startswith("드리블8"):
        await message.channel.send(random.choice(["화려한 드리블!! 모두 재치고 바로 슛!", "무난한 드리블 그리고 패스.", "드리블이 걸렸지만 라인 밖으로 나갑니다!! 드로잉!!", "빠른 드리블 후 패스합니다.", "오오!! 빠르게 달려나간뒤 패스", "안정적인 드리블 후 슈팅!", "엄청난 돌파력!! 전부 제치고 강슛!", "아 아쉽게 막힙니다. 상대 선수가 드리블 합니다!!", "아 막힙니다... 상대선수의 패스!", "아 수비수에 걸리네요. 상대의 슈팅찬스입니다!!", "공이 흘렀네요.. 상대의 드로잉!"]))
    if message.content.startswith("드리블9"):
        await message.channel.send(random.choice(["화려한 드리블!! 모두 재치고 바로 슛!", "무난한 드리블 그리고 패스.", "드리블이 걸렸지만 라인 밖으로 나갑니다!! 드로잉!!", "빠른 드리블 후 패스합니다.", "오오!! 빠르게 달려나간뒤 패스", "안정적인 드리블 후 슈팅!", "엄청난 돌파력!! 전부 제치고 강슛!", "아 아쉽게 막힙니다. 상대 선수가 드리블 합니다!!", "아 막힙니다... 상대선수의 패스!", "아 수비수에 걸리네요. 상대의 슈팅찬스입니다!!", "공이 흘렀네요.. 상대의 드로잉!"]))
    if message.content.startswith("드리블10"):
        await message.channel.send(random.choice(["화려한 드리블!! 모두 재치고 바로 슛!", "무난한 드리블 그리고 패스.", "드리블이 걸렸지만 라인 밖으로 나갑니다!! 드로잉!!", "빠른 드리블 후 패스합니다.", "오오!! 빠르게 달려나간뒤 패스", "안정적인 드리블 후 슈팅!", "엄청난 돌파력!! 전부 제치고 강슛!", "아 아쉽게 막힙니다. 상대 선수가 드리블 합니다!!", "아 막힙니다... 상대선수의 패스!", "아 수비수에 걸리네요. 상대의 슈팅찬스입니다!!", "공이 흘렀네요.. 상대의 드로잉!"]))

    if message.content.startswith("패스1"):
        await message.channel.send(random.choice(["패스 미스를 합니다. 상대편이 돌파해요!!", "패스 방향이 이상하네요... 상대의 드로잉", "패스가 막혔어요.. 상대의 패스", "장거리 패스 시도하지만 실패합니다. 상대의 패스!", "연속패스 합니다", "패스후 빠르게 돌파!", "장거리 패스! 안정적으로 받고 패스!", "완벽한 패스입니다! 슈팅기회!"]))
    if message.content.startswith("패스2"):
        await message.channel.send(random.choice(["패스 미스를 합니다. 상대편이 돌파해요!!", "패스 방향이 이상하네요... 상대의 드로잉", "패스가 막혔어요.. 상대의 패스", "장거리 패스 시도하지만 실패합니다. 상대의 패스!", "연속패스 합니다", "패스후 빠르게 돌파!", "장거리 패스! 안정적으로 받고 패스!", "완벽한 패스입니다! 슈팅기회!"]))
    if message.content.startswith("패스3"):
        await message.channel.send(random.choice(["패스 미스를 합니다. 상대편이 돌파해요!!", "패스 방향이 이상하네요... 상대의 드로잉", "패스가 막혔어요.. 상대의 패스", "장거리 패스 시도하지만 실패합니다. 상대의 패스!", "연속패스 합니다", "패스후 빠르게 돌파!", "장거리 패스! 안정적으로 받고 패스!", "완벽한 패스입니다! 슈팅기회!", "패스 받고 돌진합니다!"]))
    if message.content.startswith("패스4"):
        await message.channel.send(random.choice(["패스 미스를 합니다. 상대편이 돌파해요!!", "패스 방향이 이상하네요... 상대의 드로잉", "패스가 막혔어요.. 상대의 패스", "장거리 패스 시도하지만 실패합니다. 상대의 패스!", "연속패스 합니다", "패스후 빠르게 돌파!", "장거리 패스! 안정적으로 받고 패스!", "완벽한 패스입니다! 슈팅기회!", "패스 받고 돌진합니다!"]))
    if message.content.startswith("패스5"):
        await message.channel.send(random.choice(["패스 미스를 합니다. 상대편이 돌파해요!!", "패스 방향이 이상하네요... 상대의 드로잉", "패스가 막혔어요.. 상대의 패스", "장거리 패스 시도하지만 실패합니다. 상대의 패스!", "연속패스 합니다", "패스후 빠르게 돌파!", "장거리 패스! 안정적으로 받고 패스!", "완벽한 패스입니다! 슈팅기회!", "패스 받고 돌진합니다!", "패스 공이 상대 발에 걸려 라인 밖으로 나갑니다. 우리팀의 드로잉!"]))
    if message.content.startswith("패스6"):
        await message.channel.send(random.choice(["패스 미스를 합니다. 상대편이 돌파해요!!", "패스 방향이 이상하네요... 상대의 드로잉", "패스가 막혔어요.. 상대의 패스", "장거리 패스 시도하지만 실패합니다. 상대의 패스!", "연속패스 합니다", "패스후 빠르게 돌파!", "장거리 패스! 안정적으로 받고 패스!", "완벽한 패스입니다! 슈팅기회!", "패스 받고 돌진합니다!", "패스 공이 상대 발에 걸려 라인 밖으로 나갑니다. 우리팀의 드로잉!"]))
    if message.content.startswith("패스7"):
        await message.channel.send(random.choice(["패스 미스를 합니다. 상대편이 돌파해요!!", "패스 방향이 이상하네요... 상대의 드로잉", "패스가 막혔어요.. 상대의 패스", "장거리 패스 시도하지만 실패합니다. 상대의 패스!", "연속패스 합니다", "패스후 빠르게 돌파!", "장거리 패스! 안정적으로 받고 패스!", "완벽한 패스입니다! 슈팅기회!", "패스 받고 돌진합니다!", "패스 공이 상대 발에 걸려 라인 밖으로 나갑니다. 우리팀의 드로잉!", "찔러주는 패스! 우리팀 빠르게 달려나갑니다!"]))
    if message.content.startswith("패스8"):
        await message.channel.send(random.choice(["패스 미스를 합니다. 상대편이 돌파해요!!", "패스 방향이 이상하네요... 상대의 드로잉", "패스가 막혔어요.. 상대의 패스", "장거리 패스 시도하지만 실패합니다. 상대의 패스!", "연속패스 합니다", "패스후 빠르게 돌파!", "장거리 패스! 안정적으로 받고 패스!", "완벽한 패스입니다! 슈팅기회!", "패스 받고 돌진합니다!", "패스 공이 상대 발에 걸려 라인 밖으로 나갑니다. 우리팀의 드로잉!", "찔러주는 패스! 우리팀 빠르게 달려나갑니다!"]))
    if message.content.startswith("패스9"):
        await message.channel.send(random.choice(["패스 미스를 합니다. 상대편이 돌파해요!!", "패스 방향이 이상하네요... 상대의 드로잉", "패스가 막혔어요.. 상대의 패스", "장거리 패스 시도하지만 실패합니다. 상대의 패스!", "연속패스 합니다", "패스후 빠르게 돌파!", "장거리 패스! 안정적으로 받고 패스!", "완벽한 패스입니다! 슈팅기회!", "패스 받고 돌진합니다!", "패스 공이 상대 발에 걸려 라인 밖으로 나갑니다. 우리팀의 드로잉!", "찔러주는 패스! 우리팀 빠르게 달려나갑니다!", "완벽한 패스! 바로 슈팅!"]))
    if message.content.startswith("패스10"):
        await message.channel.send(random.choice(["패스 미스를 합니다. 상대편이 돌파해요!!", "패스 방향이 이상하네요... 상대의 드로잉", "패스가 막혔어요.. 상대의 패스", "장거리 패스 시도하지만 실패합니다. 상대의 패스!", "연속패스 합니다", "패스후 빠르게 돌파!", "장거리 패스! 안정적으로 받고 패스!", "완벽한 패스입니다! 슈팅기회!", "패스 받고 돌진합니다!", "패스 공이 상대 발에 걸려 라인 밖으로 나갑니다. 우리팀의 드로잉!", "찔러주는 패스! 우리팀 빠르게 달려나갑니다!", "완벽한 패스! 바로 슈팅!"]))

    if message.content.startswith("드로잉1"):
        await message.channel.send(random.choice(["드로잉 파울을 저지르네요... 상대의 드로잉", "드로잉을 어디다가 하는거죠? 상대팀이 돌파합니다.", "드로잉을 어디다가 하는거죠? 상대팀이 받고 패스합니다.", "드로잉으로 우리팀 드리블 찬스를 만듭니다.", "드로잉으로 우리팀 패스 기회를 만듭니다.", "완벽한 드로잉으로 슈팅기회를 만듭니다."]))
    if message.content.startswith("드로잉2"):
        await message.channel.send(random.choice(["드로잉 파울을 저지르네요... 상대의 드로잉", "드로잉을 어디다가 하는거죠? 상대팀이 돌파합니다.", "드로잉을 어디다가 하는거죠? 상대팀이 받고 패스합니다.", "드로잉으로 우리팀 드리블 찬스를 만듭니다.", "드로잉으로 우리팀 패스 기회를 만듭니다.", "완벽한 드로잉으로 슈팅기회를 만듭니다."]))
    if message.content.startswith("드로잉3"):
        await message.channel.send(random.choice(["드로잉 파울을 저지르네요... 상대의 드로잉", "드로잉을 어디다가 하는거죠? 상대팀이 돌파합니다.", "드로잉을 어디다가 하는거죠? 상대팀이 받고 패스합니다.", "드로잉으로 우리팀 드리블 찬스를 만듭니다.", "드로잉으로 우리팀 패스 기회를 만듭니다.", "완벽한 드로잉으로 슈팅기회를 만듭니다.", "안정적인 드로잉 후 패스!"]))
    if message.content.startswith("드로잉4"):
        await message.channel.send(random.choice(["드로잉 파울을 저지르네요... 상대의 드로잉", "드로잉을 어디다가 하는거죠? 상대팀이 돌파합니다.", "드로잉을 어디다가 하는거죠? 상대팀이 받고 패스합니다.", "드로잉으로 우리팀 드리블 찬스를 만듭니다.", "드로잉으로 우리팀 패스 기회를 만듭니다.", "완벽한 드로잉으로 슈팅기회를 만듭니다.", "안정적인 드로잉 후 패스!"]))
    if message.content.startswith("드로잉5"):
        await message.channel.send(random.choice(["드로잉 파울을 저지르네요... 상대의 드로잉", "드로잉을 어디다가 하는거죠? 상대팀이 돌파합니다.", "드로잉을 어디다가 하는거죠? 상대팀이 받고 패스합니다.", "드로잉으로 우리팀 드리블 찬스를 만듭니다.", "드로잉으로 우리팀 패스 기회를 만듭니다.", "완벽한 드로잉으로 슈팅기회를 만듭니다.", "안정적인 드로잉 후 패스!", "안정적인 드로잉으로 드리블 기회를 만듭니다."]))
    if message.content.startswith("드로잉6"):
        await message.channel.send(random.choice(["드로잉 파울을 저지르네요... 상대의 드로잉", "드로잉을 어디다가 하는거죠? 상대팀이 돌파합니다.", "드로잉을 어디다가 하는거죠? 상대팀이 받고 패스합니다.", "드로잉으로 우리팀 드리블 찬스를 만듭니다.", "드로잉으로 우리팀 패스 기회를 만듭니다.", "완벽한 드로잉으로 슈팅기회를 만듭니다.", "안정적인 드로잉 후 패스!", "안정적인 드로잉으로 드리블 기회를 만듭니다."]))
    if message.content.startswith("드로잉7"):
        await message.channel.send(random.choice(["드로잉 파울을 저지르네요... 상대의 드로잉", "드로잉을 어디다가 하는거죠? 상대팀이 돌파합니다.", "드로잉을 어디다가 하는거죠? 상대팀이 받고 패스합니다.", "드로잉으로 우리팀 드리블 찬스를 만듭니다.", "드로잉으로 우리팀 패스 기회를 만듭니다.", "완벽한 드로잉으로 슈팅기회를 만듭니다.", "안정적인 드로잉 후 패스!", "안정적인 드로잉으로 드리블 기회를 만듭니다.", "안정적인 드로잉 후 패스!", "안정적인 드로잉으로 드리블 기회를 만듭니다."]))
    if message.content.startswith("드로잉8"):
        await message.channel.send(random.choice(["드로잉 파울을 저지르네요... 상대의 드로잉", "드로잉을 어디다가 하는거죠? 상대팀이 돌파합니다.", "드로잉을 어디다가 하는거죠? 상대팀이 받고 패스합니다.", "드로잉으로 우리팀 드리블 찬스를 만듭니다.", "드로잉으로 우리팀 패스 기회를 만듭니다.", "완벽한 드로잉으로 슈팅기회를 만듭니다.", "안정적인 드로잉 후 패스!", "안정적인 드로잉으로 드리블 기회를 만듭니다.", "안정적인 드로잉 후 패스!", "안정적인 드로잉으로 드리블 기회를 만듭니다."]))
    if message.content.startswith("드로잉9"):
        await message.channel.send(random.choice(["드로잉 파울을 저지르네요... 상대의 드로잉", "드로잉을 어디다가 하는거죠? 상대팀이 돌파합니다.", "드로잉을 어디다가 하는거죠? 상대팀이 받고 패스합니다.", "드로잉으로 우리팀 드리블 찬스를 만듭니다.", "드로잉으로 우리팀 패스 기회를 만듭니다.", "완벽한 드로잉으로 슈팅기회를 만듭니다.", "안정적인 드로잉 후 패스!", "안정적인 드로잉으로 드리블 기회를 만듭니다.", "안정적인 드로잉 후 패스!", "안정적인 드로잉으로 드리블 기회를 만듭니다.", "드로잉을 오버헤드킥으로 넣어버립니다!!"]))
    if message.content.startswith("드로잉10"):
        await message.channel.send(random.choice(["드로잉 파울을 저지르네요... 상대의 드로잉", "드로잉을 어디다가 하는거죠? 상대팀이 돌파합니다.", "드로잉을 어디다가 하는거죠? 상대팀이 받고 패스합니다.", "드로잉으로 우리팀 드리블 찬스를 만듭니다.", "드로잉으로 우리팀 패스 기회를 만듭니다.", "완벽한 드로잉으로 슈팅기회를 만듭니다.", "안정적인 드로잉 후 패스!", "안정적인 드로잉으로 드리블 기회를 만듭니다.", "안정적인 드로잉 후 패스!", "안정적인 드로잉으로 드리블 기회를 만듭니다.", "드로잉을 오버헤드킥으로 넣어버립니다!!"]))

    if message.content.startswith("코너킥1"):
        await message.channel.send(random.choice(["감아차기를 해보지만 라인 밖으로 나가네요... 골킥", "불안한 코너킥으로 간신히 패스 기회를 만듭니다.", "짧은 코너킥으로 우리팀의 패스 기회를 만듭니다."]))
    if message.content.startswith("코너킥2"):
        await message.channel.send(random.choice(["감아차기를 해보지만 라인 밖으로 나가네요... 골킥", "불안한 코너킥으로 간신히 패스 기회를 만듭니다.", "짧은 코너킥으로 우리팀의 패스 기회를 만듭니다."]))
    if message.content.startswith("코너킥3"):
        await message.channel.send(random.choice(["감아차기를 해보지만 라인 밖으로 나가네요... 골킥", "해딩을 노려보지만 실패합니다.", "짧은 코너킥으로 우리팀의 패스 기회를 만듭니다.", "코너킥으로 우리팀의 드리블 기회를 만듭니다."]))
    if message.content.startswith("코너킥4"):
        await message.channel.send(random.choice(["감아차기를 해보지만 라인 밖으로 나가네요... 골킥", "해딩을 노려보지만 실패합니다.", "짧은 코너킥으로 우리팀의 패스 기회를 만듭니다.", "코너킥으로 우리팀의 드리블 기회를 만듭니다."]))
    if message.content.startswith("코너킥5"):
        await message.channel.send(random.choice(["가마차기가 아슬하게 라인아웃되네요.. 골킥", "해딩 시도를 해보지만 막힙니다. 튀어나오는 볼을 슈팅!", "짧은 코너킥으로 우리팀의 패스 기회를 만듭니다.", "코너킥으로 우리팀의 드리블 기회를 만듭니다."]))
    if message.content.startswith("코너킥6"):
        await message.channel.send(random.choice(["가마차기가 아슬하게 라인아웃되네요.. 골킥", "해딩 시도를 해보지만 막힙니다. 튀어나오는 볼을 슈팅!", "짧은 코너킥으로 우리팀의 패스 기회를 만듭니다.", "코너킥으로 우리팀의 드리블 기회를 만듭니다."]))
    if message.content.startswith("코너킥7"):
        await message.channel.send(random.choice(["가마차기를 성공시킵니다!! 엄청난 골!!", "해딩 시도를 해보지만 막힙니다. 튀어나오는 볼을 슈팅!", "짧은 코너킥으로 우리팀의 패스 기회를 만듭니다.", "코너킥으로 우리팀의 드리블 기회를 만듭니다.", "키퍼의 선방! 그리고 역습을 합니다. 상대 선수가 미친듯이 달려나가는군요!"]))
    if message.content.startswith("코너킥8"):
        await message.channel.send(random.choice(["가마차기를 성공시킵니다!! 엄청난 골!!", "해딩 시도를 해보지만 막힙니다. 튀어나오는 볼을 슈팅!", "짧은 코너킥으로 우리팀의 패스 기회를 만듭니다.", "코너킥으로 우리팀의 드리블 기회를 만듭니다.", "키퍼의 선방! 그리고 역습을 합니다. 상대 선수가 미친듯이 달려나가는군요!"]))
    if message.content.startswith("코너킥9"):
        await message.channel.send(random.choice(["가마차기를 성공시킵니다!! 엄청난 골!!", "해딩 시도를 해보지만 막힙니다. 튀어나오는 볼을 슈팅!", "짧은 코너킥으로 우리팀의 패스 기회를 만듭니다.", "코너킥으로 우리팀의 드리블 기회를 만듭니다.", "키퍼의 선방! 그리고 역습을 합니다. 상대 선수가 미친듯이 달려나가는군요!", "오버해드킥으로 화려한 골을 넣어버립니다!!"]))
    if message.content.startswith("코너킥10"):
        await message.channel.send(random.choice(["가마차기를 성공시킵니다!! 엄청난 골!!", "해딩 시도를 해보지만 막힙니다. 튀어나오는 볼을 슈팅!", "짧은 코너킥으로 우리팀의 패스 기회를 만듭니다.", "코너킥으로 우리팀의 드리블 기회를 만듭니다.", "키퍼의 선방! 그리고 역습을 합니다. 상대 선수가 미친듯이 달려나가는군요!", "오버해드킥으로 화려한 골을 넣어버립니다!!"]))

    if message.content.startswith("골킥1"):
        await message.channel.send(random.choice(["하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 패스하네요", "하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 드리블합니다", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 패스하네요!", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 드리블합니다!", "아.... 어디다가 차나요??? 라인을 넘겨 상대의 드로잉입니다."]))
    if message.content.startswith("골킥2"):
        await message.channel.send(random.choice(["하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 패스하네요", "하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 드리블합니다", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 패스하네요!", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 드리블합니다!", "아.... 어디다가 차나요??? 라인을 넘겨 상대의 드로잉입니다."]))
    if message.content.startswith("골킥3"):
        await message.channel.send(random.choice(["하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 패스하네요", "하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 드리블합니다", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 패스하네요!", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 드리블합니다!", "아.... 어디다가 차나요??? 라인을 넘겨 상대의 드로잉입니다."]))
    if message.content.startswith("골킥4"):
        await message.channel.send(random.choice(["하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 패스하네요", "하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 드리블합니다", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 패스하네요!", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 드리블합니다!", "아.... 어디다가 차나요??? 라인을 넘겨 상대의 드로잉입니다."]))
    if message.content.startswith("골킥5"):
        await message.channel.send(random.choice(["하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 패스하네요", "하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 드리블합니다", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 패스하네요!", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 드리블합니다!", "아.... 어디다가 차나요??? 라인을 넘겨 상대의 드로잉입니다.", "초장거리 골킥으로 우리팀에게 슈팅기회를 줍니다!"]))
    if message.content.startswith("골킥6"):
        await message.channel.send(random.choice(["하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 패스하네요", "하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 드리블합니다", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 패스하네요!", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 드리블합니다!", "아.... 어디다가 차나요??? 라인을 넘겨 상대의 드로잉입니다.", "초장거리 골킥으로 우리팀에게 슈팅기회를 줍니다!"]))
    if message.content.startswith("골킥7"):
        await message.channel.send(random.choice(["하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 패스하네요", "하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 드리블합니다", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 패스하네요!", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 드리블합니다!", "아.... 어디다가 차나요??? 라인을 넘겨 상대의 드로잉입니다.", "초장거리 골킥으로 우리팀에게 슈팅기회를 줍니다!"]))
    if message.content.startswith("골킥8"):
        await message.channel.send(random.choice(["하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 패스하네요", "하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 드리블합니다", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 패스하네요!", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 드리블합니다!", "아.... 어디다가 차나요??? 라인을 넘겨 상대의 드로잉입니다.", "초장거리 골킥으로 우리팀에게 슈팅기회를 줍니다!", "구석으로 찔러넣습니다. 결정 스킬을 사용하네요!"]))
    if message.content.startswith("골킥9"):
        await message.channel.send(random.choice(["하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 패스하네요", "하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 드리블합니다", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 패스하네요!", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 드리블합니다!", "아.... 어디다가 차나요??? 라인을 넘겨 상대의 드로잉입니다.", "초장거리 골킥으로 우리팀에게 슈팅기회를 줍니다!", "구석으로 찔러넣습니다. 결정 스킬을 사용하네요!"]))
    if message.content.startswith("골킥10"):
        await message.channel.send(random.choice(["하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 패스하네요", "하프라인을 넘겨 보지만 상대 수비수한테 넘어갑니다. 상대선수! 드리블합니다", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 패스하네요!", "하프라인을 넘겨 우리팀 공격수한테 공이 도착합니다. 드리블합니다!", "아.... 어디다가 차나요??? 라인을 넘겨 상대의 드로잉입니다.", "초장거리 골킥으로 우리팀에게 슈팅기회를 줍니다!", "구석으로 찔러넣습니다. 결정 스킬을 사용하네요!"]))


    if message.content.startswith('슈팅1'):
        randomNum = random.randrange(1, 9)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="간당간당하게 들어갔군요", color=discord.Color.blue()))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="강슛입니다! 골!!!", color=discord.Color.blue()))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="장거리 슛! 아아아 들어갑니다!!!", color=discord.Color.blue()))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="아 골대맞고 나갑니다.. 골킥!", color=discord.Color.blue()))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="아 수비수 발에 막힙니다!! 상대선수가 치고 나가요!", color=discord.Color.blue()))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="골키퍼가 막습니다!! 코너킥!", color=discord.Color.blue()))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="아.... 대기권돌파슛! 골킥입니다.", color=discord.Color.blue()))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="수비수가 받아서 패스합니다!", color=discord.Color.blue()))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="골입니다!!", color=discord.Color.blue()))

    if message.content.startswith('슈팅2'):
        randomNum = random.randrange(1, 10)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="간당간당하게 들어갔군요", color=discord.Color.blue()))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="강슛입니다! 골!!!", color=discord.Color.blue()))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="장거리 슛! 아아아 들어갑니다!!!", color=discord.Color.blue()))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="아 골대맞고 나갑니다.. 골킥!", color=discord.Color.blue()))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="아 수비수 발에 막힙니다!! 상대선수가 치고 나가요!", color=discord.Color.blue()))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="골키퍼가 막습니다!! 코너킥!", color=discord.Color.blue()))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="아.... 대기권돌파슛! 골킥입니다.", color=discord.Color.blue()))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="수비수가 받아서 패스합니다!", color=discord.Color.blue()))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="화려한 골입니다!!", color=discord.Color.blue()))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="골입니다!!", color=discord.Color.blue()))

    if message.content.startswith('슈팅3'):
        randomNum = random.randrange(1, 11)
        if randomNum==1:
            await message.channel.send(embed=discord.Embed(title="간당간당하게 들어갔군요", color=discord.Color.blue()))
        if randomNum==2:
            await message.channel.send(embed=discord.Embed(title="강슛입니다! 골!!!", color=discord.Color.blue()))
        if randomNum==3:
            await message.channel.send(embed=discord.Embed(title="장거리 슛! 아아아 들어갑니다!!!", color=discord.Color.blue()))
        if randomNum==4:
            await message.channel.send(embed=discord.Embed(title="아 골대맞고 나갑니다.. 골킥!", color=discord.Color.blue()))
        if randomNum==5:
            await message.channel.send(embed=discord.Embed(title="아 수비수 발에 막힙니다!! 상대선수가 치고 나가요!", color=discord.Color.blue()))
        if randomNum==6:
            await message.channel.send(embed=discord.Embed(title="골키퍼가 막습니다!! 코너킥!", color=discord.Color.blue()))
        if randomNum==7:
            await message.channel.send(embed=discord.Embed(title="아.... 대기권돌파슛! 골킥입니다.", color=discord.Color.blue()))
        if randomNum==8:
            await message.channel.send(embed=discord.Embed(title="수비수가 받아서 패스합니다!", color=discord.Color.blue()))
        if randomNum==9:
            await message.channel.send(embed=discord.Embed(title="화려한 골입니다!!", color=discord.Color.blue()))
        if randomNum==10:
            await message.channel.send(embed=discord.Embed(title="상대편의 파울! 프리킥입니다!", color=discord.Color.blue()))
        if randomNum==11:
            await message.channel.send(embed=discord.Embed(title="골입니다!!", color=discord.Color.blue()))


def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = []
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!축구", "!경기시작", "드리블1", "드리블2", "드리블3", "드리블4", "드리블5", "드리블6", "드리블7", "드리블8", "드리블9", "드리블10", "패스1", "패스2", "패스3", "패스4", "패스5", "패스6", "패스7", "패스8", "패스9", "패스10", "드로잉1", "드로잉2", "드로잉3", "드로잉4", "드로잉5", "드로잉6", "드로잉7", "드로잉8", "드로잉9", "드로잉10", "코너킥1", "코너킥2", "코너킥3", "코너킥4", "코너킥5", "코너킥6", "코너킥7", "코너킥8", "코너킥9", "코너킥10", "골킥1", "슈팅1", "슈팅2"]

    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys': content_key, 'func': on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys': startswith_key, 'func': on_message}