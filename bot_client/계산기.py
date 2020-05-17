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

    if message.content.startswith("!계산기"):
        global calcResult
        command, operator, number1, number2 = message.content.split(' ')
        if operator == "+":
            calcResult = int(number1) + int(number2)
            await message.channel.send("값 : " + str(calcResult))

        if operator == "-":
            calcResult = int(number1) - int(number2)
            await message.channel.send("값 : " + str(calcResult))

        if operator == "*":
            calcResult = int(number1) * int(number2)
            await message.channel.send("값 : " + str(calcResult))

        if operator == "/":
            calcResult = int(number1) / int(number2)
            await message.channel.send("값 : " + str(calcResult))


def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    content_key = []
    startswith_key = ["!계산기"]

    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}