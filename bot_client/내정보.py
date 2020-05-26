import discord
import datetime



async def on_message(message):

    if message.content.startswith("!내정보"):
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f"{message.author}님입니다.", description=f"{str(date.year)}년{str(date.month)}월{str(date.day)}일에 가입하셨습니다.", color=0x2A2A2A)
        embed.set_image(url=message.author.avatar_url)
        embed.set_footer(text="당신의 정보입니다.")
        await message.channel.send(embed=embed)

def register(g_content_fun, g_startswith_fun):
    print('register : ', __name__)

    # message.content == "key" 로 비교할 key 등록
    content_key = []
    # message.content.startswith("key") 로 비교할 key 등록
    startswith_key = ["!내정보"]


    # key 에 대응하는 함수 등록
    if len(content_key):
        g_content_fun[__name__] = {'keys':content_key, 'func':on_message}
    if len(startswith_key):
        g_startswith_fun[__name__] = {'keys':startswith_key, 'func':on_message}