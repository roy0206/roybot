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

    if message.content.startswith("="):
        global calcResult
        command, question = message.content.split(maxsplit=1)
        await message.channel.send("값 : " + str(eval(question)))


def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    content_key = []
    startswith_key = ["="]

    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}