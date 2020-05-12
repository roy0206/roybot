import discord
import datetime
import urllib
# import requests
import bs4
from selenium import webdriver
import random
from urllib.request import Request
import os
# import sys
import json
import asyncio



searchYoutubeHref={} # 유튜브 하이퍼링크 모음

client = discord.Client()
count = 0


@client.event
async def on_ready():
    print(client.user.id)
    print("GOGO")
    game = discord.Game("로이스톱모션 구독")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_member_join(member):
    role= ""
    for i in member.server.roles:
        if i.name == "평민":
            role = i
            break
    await client.add_roles(member, role)



@client.event
async def on_message(message):


    if message.content.startswith("!패치노트"):
        embed = discord.Embed(title="로이봇 패치노트", description="""1.0.1 버전: 안녕->안녕하세요
        
1.0 2버젼:톡엔티 전용 특정 메시지&
   유튜버 소개(임베드)
   
1.0.3버전:'!계산기'&'!시간 추가'

1.0.4버전:'!대출','!대출상환','!톡출',
   '!로이봇'(듀토리얼) 추가
   
1.1.0버전:'!날씨','!검색','!이모티콘','!복권',
   '!가위,!바위,!보','주사위 추가
   기존 명령어 몇몇 수정&패치노트 추가""", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith("!업뎃"):
        embed = discord.Embed(title="로이봇이 업데이트가 되였습니다.", description="공지사항 채널에서 없데이트 사항을 확인하세요", color=0x00ff00)
        await message.channel.send(embed=embed)



    if message.content.startswith("!화사멍청이"):
        await message.channel.send("영어 열심히 해라ㅗㅗ")

    if message.content.startswith("!강희수"):
        await message.channel.send("그는 유튜브에서 축튜버란 채널을 운영하고 있습니다")

    if message.content.startswith("!끝"):
        await message.channel.send("다음 끝말잇기 시작시간:다음날 오전 8시[게임 시작전 끝말잇기방에서 채팅 금지]")
        await message.channel.send("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    if message.content.startswith("!원기별명1"):
        await message.channel.send("원기옥")

    if message.content.startswith("!원기별명2"):
        await message.channel.send("one key")

    if message.content.startswith("톡출"):
        await message.channel.send("출석이 확인되였습니다.관리자가 적립을 완료하면 적립완료라고 보내게 됩니다")

    if message.content.startswith("!화사본명"):
        await message.channel.send("배.선.욱")

    if message.content.startswith("!go"):
        await message.channel.send("오늘 톡엔티 오는 사람?")

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

    if message.content.startswith("!로이봇"):
        embed = discord.Embed(title="로이봇 듀토리얼", description="로이봇의 듀토리얼입니다", color=0x00ff00)
        embed.add_field(name="1. '!핼로'이라고 치면 안녕하세요로 대답", value=".", inline=True)
        embed.add_field(name="2. '!로이스톱모션' 이라고 치면 로이스톱모션 소개", value=".", inline=True)
        embed.add_field(name="3. '!축튜버' 라고 치면 축튜버 소개", value=".", inline=True)
        embed.add_field(name="4. '!계산기' (더하기or빼기or곱하기or나누기) 숫자 숫자 입력하면 계산해줌", value=".", inline=True)
        embed.add_field(name="5. '!시간' 이러고 치면 현제시간 알려줌", value=".", inline=True)
        embed.add_field(name="6. '!톡앤티' 라고 치면 톡엔티 소개", value=".", inline=True)
        embed.add_field(name="7. '!도박(확률:10~70)' 이라고 치면 50%확률 도박 시행", value=".", inline=True)
        embed.add_field(name="8. '!이모티콘' 이라 치면 랜덤 이모티콘 보냄", value=".", inline=True)
        embed.add_field(name="9. '!검색 ** '으로 원하는 것을 유튜브에서 검색", value=".", inline=True)
        embed.add_field(name="10. '!날씨 (도시이름)'으로 해당 도시의 이름 알려줌", value=".", inline=True)
        embed.add_field(name="11. '!복권'으로 1~46까지의 수 중 7개 랜덤 수 뽑기", value=".", inline=True)
        embed.add_field(name="12. '!대출' 1000~50000(톡) 으로 대출 가능(자세한건 은행 공지)", value=".", inline=True)
        embed.add_field(name="13. '!대출상환' 으로 돈 값기", value=".", inline=True)
        embed.add_field(name="14. '!주사위' 로 1~6까지의' 수 중 랜덤으로 하나 뽑아줌", value=".", inline=True)
        embed.add_field(name="15. '!go' 하면 톡엔티 오는사람 메세지 보내짐", value=".", inline=True)
        embed.add_field(name="16. '!이미지 (**)' 으로 **관련 이미지를 보여줌", value=".", inline=True)
        embed.add_field(name="17. '가위'or'바위'or'보' 로 봇과 가위바위보를 함", value=".", inline=True)
        embed.add_field(name="18. '!끝'으로 끝말잇기를 끝냄", value=".", inline=True)
        embed.add_field(name="19. '!톡사공 주식목록' 으로 주식 목록 확인 가능", value=".", inline=True)
        embed.add_field(name="20. '!주식(주식번호)' 으로 주식 구매 예약/구매 완료되면 자료실에 없대이트", value=".", inline=True)
        embed.add_field(name="기타:톡앤티 멤버 명령어", value=".", inline=True)

        await message.channel.send(embed=embed)

    elif message.content == "!시간":
        now = datetime.datetime.now()
        await message.channel.send((str(now.year) + "년" + str(now.month) + "월" + str(now.day) + "일" + str(now.hour) + "시" + str(now.minute) + "분 입니다"))

    elif message.content == "!도박70":
        await message.channel.send(random.choice(["올~~성공이얏!!","축하해!!","굿","이걸 실패하면 호구지!","대단해!","ㄷㄷ 성공","내가 졌어 축하한다 친구여","그걸 실패하냐 더러운 자식","개못하누","실패야.. 무튼 그런거임 수고 ㅂ",]))

    elif message.content == "!도박60":
        await message.channel.send(random.choice(["이걸?","성공","대단해","럭키 가이","젠장 너가 이겼어!","축하한다 친구여","실패야ㅜ 그러게 잘좀 하지","오늘도 실패 ㅋ","꽝!꽝!"]))

    elif message.content == "!도박50":
        await message.channel.send(random.choice(["성공!!", "다음 기회에..."]))

    elif message.content == "!도박40":
        await message.channel.send(random.choice(["이걸?","성공","대단해","럭키 가이","다음 기회에...","훗 넌 졌어","실패야ㅜ 그러게 잘좀 하지","오늘도 실패 ㅋ","꽝!꽝!","불쌍한 자식",]))

    elif message.content == "!도박30":
        await message.channel.send(random.choice(["성공이닷!","이게 바로 나의 운!","thiis is me","다음 기회에...","그게 될거라 생각하니?","안타깝군","망했네연","왤케 못하니?","...실패다..","매뤙 실패쥐뤙",]))

    elif message.content == "!도박20":
        await message.channel.send(random.choice(["올~~성공이얏!!","축하해!!","꽝!","망했네여 ㅜㅜ","다음 기회에...","에휴","어림도 없지","쯧쯧","잘 해봐..","그것도 못하는 바보같은이",]))

    elif message.content == "!도박10":
        await message.channel.send(random.choice(["1/10을 돌파하다니 ㄷㄷ 미친 놈이구만","그걸 될거라 생각한 너의 잘못이다","꽝!","망했네여 ㅜㅜ","빠가 자식","에휴","어림도 없지","쯧쯧","잘 해봐..","그것도 못하는 바보같은이",]))


    if message.content.startswith("!계산기"):
        global calcResult
        command, operator, number1, number2 =  message.content.split(' ')
        if operator == "+" :
            calcResult = int(number1) + int(number2)
            await message.channel.send("값 : "+str(calcResult))

        if operator == "-":
            calcResult = int(number1) - int(number2)
            await message.channel.send("값 : "+str(calcResult))

        if operator == "*":
            calcResult = int(number1) * int(number2)
            await message.channel.send("값 : "+str(calcResult))

        if operator == "/":
            calcResult = int(number1) / int(number2)
            await message.channel.send("값 : "+str(calcResult))

    if message.content.startswith('!대출 1000') or message.content.startswith('!대출 1000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다.*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 2000') or message.content.startswith('!대출 2000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다.*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 3000') or message.content.startswith('!대출 3000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다.*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 4000') or message.content.startswith('!대출 4000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다.*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 5000') or message.content.startswith('!대출 5000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다.*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 6000') or message.content.startswith('!대출 6000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다.*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 7000') or message.content.startswith('!대출 7000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "**주의사항:대출중에는 톡출이 불가합니다.*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 8000') or message.content.startswith('!대출 8000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다.*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 9000') or message.content.startswith('!대출 9000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다.*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 10000') or message.content.startswith('!대출 10000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다. 10000t이상 대출 시에는 사유 필수&2주안에 다 값아야 합니다*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 20000') or message.content.startswith('!대출 20000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다. 10000t이상 대출 시에는 사유 필수&2주안에 다 값아야 합니다*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 30000') or message.content.startswith('!대출 30000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다. 10000t이상 대출 시에는 사유 필수&2주안에 다 값아야 합니다*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 40000') or message.content.startswith('!대출 40000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다. 10000t이상 대출 시에는 사유 필수&2주안에 다 값아야 합니다*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 50000') or message.content.startswith('!대출 50000톡'):
        embed = discord.Embed(title="대출 완료되셨습니다", description="잠시만 기다려주십시오 곧 입금됩니다"
                                                              "*주의사항:대출중에는 톡출이 불가합니다. 10000t이상 대출 시에는 사유 필수&2주안에 다 값아야 합니다*", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith('!대출 상환') or message.content.startswith('!대출상환'):
        embed = discord.Embed(title="대출 상환되셨습니다.", description="잠시만 기다리십시오 상환중입니다.", color=0x00ff00)
        embed.set_footer(text="돈을 다 값으셨다면 톡출이 가능합니다.")
        await message.channel.send(embed=embed)


    if message.content.startswith("!날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        # req = requests(url, headers=hdr)
        html = urllib.request.urlopen(url)
        # html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)
        embed.add_field(name='현재상태', value=todayValue, inline=False)
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)



        await message.channel.send(embed=embed)
        # client.send_message(message.channel,embed=embed)

    if message.content.startswith("!복권"):
        count=0
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 숫자!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(embed=embed)



    if message.content.startswith('!검색'):
        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        encText = Text

        chromedriver_dir = r'C:\Users\battl\AppData\Local\Programs\Python\chromedriver.exe' #크롬드라이버 경로
        driver = webdriver.Chrome(chromedriver_dir)
        driver.get('https://www.youtube.com/results?search_query='+encText) #유튜브 검색링크
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'}) # a태그에서 video title 이라는 id를 찾음

        embed = discord.Embed(
            title="영상들!",
            description="검색한 영상 결과",
            colour=discord.Color.blue())

        for i in range(0, 4):
            entireNum = entire[i]
            entireText = entireNum.text.strip()  # 영상제목
            print(entireText)
            test1 = entireNum.get('href')  # 하이퍼링크
            print(test1)
            rink = 'https://www.youtube.com'+test1
            embed.add_field(name=str(i+1)+'번째 영상',value=entireText + '\n링크 : '+rink)
        await message.channel.send(embed=embed)


    if message.content.startswith('!이모티콘'):
        emoji = [" ꒰⑅ᵕ༚ᵕ꒱ ", " ꒰◍ˊ◡ˋ꒱ ", " ⁽⁽◝꒰ ˙ ꒳ ˙ ꒱◜⁾⁾ ", " ༼ つ ◕_◕ ༽つ ", " ⋌༼ •̀ ⌂ •́ ༽⋋ ",
                 " ( ･ิᴥ･ิ) ", " •ө• ", " ค^•ﻌ•^ค ", " つ╹㉦╹)つ ", " ◕ܫ◕ ", " ᶘ ͡°ᴥ͡°ᶅ ", " ( ؕؔʘ̥̥̥̥ ه ؔؕʘ̥̥̥̥ ) ",
                 " ( •́ ̯•̀ ) ",
                 " •̀.̫•́✧ ", " '͡•_'͡• ", " (΄◞ิ౪◟ิ‵) ", " ˵¯͒ བ¯͒˵ ", " ͡° ͜ʖ ͡° ", " ͡~ ͜ʖ ͡° ", " (づ｡◕‿‿◕｡)づ ",
                 " ´_ゝ` ", " ٩(͡◕_͡◕ ", " ⁄(⁄ ⁄•⁄ω⁄•⁄ ⁄)⁄ ", " ٩(͡ï_͡ï☂ ", " ௐ ", " (´･ʖ̫･`) ", " ε⌯(ง ˙ω˙)ว ",
                 " (っ˘ڡ˘ς) ", "●▅▇█▇▆▅▄▇", "╋╋◀", "︻╦̵̵̿╤──", "ー═┻┳︻▄", "︻╦̵̵͇̿̿̿̿══╤─",
                 " ጿ ኈ ቼ ዽ ጿ ኈ ቼ ዽ ጿ ", "∑◙█▇▆▅▄▃▂", " ♋♉♋ ", " (๑╹ω╹๑) ", " (╯°□°）╯︵ ┻━┻ ",
                 " (///▽///) ", " σ(oдolll) ", " 【o´ﾟ□ﾟ`o】 ", " ＼(^o^)／ ", " (◕‿‿◕｡) ", " ･ᴥ･ ", " ꈍ﹃ꈍ "
                                                                                                 " ˃̣̣̣̣̣̣︿˂̣̣̣̣̣̣ ",
                 " ( ◍•㉦•◍ ) ", " (｡ì_í｡) ", " (╭•̀ﮧ •́╮) ", " ଘ(੭*ˊᵕˋ)੭ ", " ´_ゝ` ", " (~˘▾˘)~ "]  # 이모티콘 배열입니다.

        randomNum = random.randrange(0, len(emoji))  # 0 ~ 이모티콘 배열 크기 중 랜덤숫자를 지정합니다.
        print("랜덤수 값 :" + str(randomNum))
        print(emoji[randomNum])

        await message.channel.send(embed=discord.Embed(description=emoji[randomNum]))

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



    if message.content.startswith('!이미지'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip())  # 입력한 명령어

        randomNum = random.randrange(0, 40) # 랜덤 이미지 숫자

        location = Text
        enc_location = urllib.parse.quote(location) # 한글을 url에 사용하게끔 형식을 바꿔줍니다. 그냥 한글로 쓰면 실행이 안됩니다.
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + enc_location # 이미지 검색링크+검색할 키워드
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser") # 전체 html 코드를 가져옵니다.
        # print(bsObj)
        imgfind1 = bsObj.find('div', {'class': 'photo_grid _box'}) # bsjObj에서 div class : photo_grid_box 의 코드를 가져옵니다.
        # print(imgfind1)
        imgfind2 = imgfind1.findAll('a', {'class': 'thumb _thumb'}) # imgfind1 에서 모든 a태그 코드를 가져옵니다.
        imgfind3 = imgfind2[randomNum]  # 0이면 1번째사진 1이면 2번째사진 형식으로 하나의 사진 코드만 가져옵니다.
        imgfind4 = imgfind3.find('img') # imgfind3 에서 img코드만 가져옵니다.
        imgsrc = imgfind4.get('data-source') # imgfind4 에서 data-source(사진링크) 의 값만 가져옵니다.
        print(imgsrc)
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed.set_image(url=imgsrc) # 이미지의 링크를 지정해 이미지를 설정합니다.
        await message.channel.send(embed=embed)

    if message.content==('!가위'):
        str1 = ['가위','바위','보']
        r = random.choice(str1)
        if r == '가위':
            await message.channel.send("봇의 선택:" + r + "\n비겼습니다.")
        elif r == '바위':
            await message.channel.send("봇의 선택:" + r + "\n졌습니다.")
        elif r == '보':
            await message.channel.send("봇의 선택:" + r + "\n이겼습니다.")

    elif message.content==('!바위'):
        str1 = ['가위','바위','보']
        r = random.choice(str1)
        if r == '바위':
            await message.channel.send("봇의 선택:" + r + "\n비겼습니다.")
        elif r == '보':
            await message.channel.send("봇의 선택:" + r + "\n졌습니다.")
        elif r == '가위':
            await message.channel.send("봇의 선택:" + r + "\n이겼습니다.")

    if message.content==('!보'):
        str1 = ['가위','바위','보']
        r = random.choice(str1)
        if r == '보':
            await message.channel.send("봇의 선택:" + r + "\n비겼습니다.")
        elif r == '가위':
            await message.channel.send("봇의 선택:" + r + "\n졌습니다.")
        elif r == '바위':
            await message.channel.send("봇의 선택:" + r + "\n이겼습니다.")



    if message.content.startswith('!삭제 '):
        if type(message.channel) == discord.channel.Channel:
            if message.author.server_permissions.administrator:
                den = int(message.content[13:])
                if den > 0:
                    try:
                        async for m in client.logs_from(message.channel, limit=den + 1):
                            await client.delete_message(m)
                        returnmsg = await client.send_message(message.channel, str(den) + "개의 메시지를 삭제하였습니다.")
                        await asyncio.sleep(2)
                        await client.delete_message(returnmsg)

                    except discord.errors.Forbidden:
                        await client.send_message(message.channel, '봇이 권한을 가지고 있지 않습니다.')
                        raise Exception

                    except discord.errors.HTTPException:
                        await  client.send_message(message.channel, '알 수 없는 오류가 발생했습니다')
                        raise Exception
                else:
                    await message.channel.send("1개 이상의 메시지만 삭제할 수 있습니다!")
            else:
                await message.channel.send('당신은 관리자 권한을 가지고 있지 않습니다.')
        else:
            await message.channel.send('서버 채널에서만 이 명령어를 사용할 수 있습니다.')

    if message.content.startswith('!영화순위'):
        # http://ticket2.movie.daum.net/movie/movieranklist.aspx 크롤링한 사이트
        i1 = 0  # 랭킹 string값
        embed = discord.Embed(
            title="영화순위",
            description="영화순위입니다.",
            colour=discord.Color.red()
        )
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        moviechartBase = bsObj.find('div', {'class': 'main_detail'})
        moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
        moviechart2 = moviechart1.find_all('li')

        for i in range(0, 20):
            i1 = i1 + 1
            stri1 = str(i1)  # i1은 영화랭킹을 나타내는데 사용됩니다
            print()
            print(i)
            print()
            moviechartLi1 = moviechart2[i]  # i번째 LI ------------------------- ?등랭킹 영화---------------------------
            moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div
            moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
            moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목
            print(moviechartLi1MovieName)

            moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
            moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
            moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점
            print(moviechartLi1Ratting)

            moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
            moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임
            moviechartLi1openDay3 = moviechartLi1openDay2[0]
            moviechartLi1Yerating1 = moviechartLi1openDay2[1]
            moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜
            print(moviechartLi1openDay)
            moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동
            print(moviechartLi1Yerating)  # ------------------------- ?등랭킹 영화---------------------------
            print()
            embed.add_field(name='---------------랭킹' + stri1 + '위---------------',
                            value='\n영화제목 : ' + moviechartLi1MovieName + '\n영화평점 : ' + moviechartLi1Ratting + '점' + '\n개봉날짜 : ' + moviechartLi1openDay + '\n예매율,랭킹변동 : ' + moviechartLi1Yerating,
                            inline=False)  # 영화랭킹

        await message.channel.send(embed=embed)

    if message.content.startswith('!번역'):
        learn = message.content.split(" ")
        command, text = message.content.split(' ')

        client_id = "UZBA4BAXuxx4hWLwQMKD"
        client_secret = "kiI0nYPW0z"

        url = "https://openapi.naver.com/v1/papago/n2mt"
        print(len(learn))
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            text = text + " " + learn[i]
        encText = urllib.parse.quote(text)
        data = "source=ko&target=en&text=" + encText

        request = urllib.request.Request(url)
        request.add_header("X-Naver-Client-Id", client_id)
        request.add_header("X-Naver-Client-Secret", client_secret)

        response = urllib.request.urlopen(request, data=data.encode("utf-8"))

        rescode = response.getcode()
        if (rescode == 200):
            response_body = response.read()
            data = response_body.decode('utf-8')
            data = json.loads(data)
            tranText = data['message']['result']['translatedText']
        else:
            print("Error Code:" + rescode)

        print('번역된 내용 :', tranText)

        embed = discord.Embed(
            title='한글->영어 번역결과',
            description=tranText,
            colour=discord.Colour.green()
        )
        await message.channel.send(embed=embed)


    if message.content.startswith("!톡사공 주식목록"):
        embed = discord.Embed(title="주식 목록", description="주식 구매를 원하시면 !주식 (주식번호)를 처주시기 바랍니다.", color=0x00ff00)
        embed.add_field(name="1톡사공 도로공사", value="5000t(10개)", inline=True)
        embed.add_field(name="2톡앤티 스피킹", value="5000t(30개)", inline=True)
        embed.add_field(name="3톡앤티 리딩", value="1800t(30개)", inline=True)
        embed.add_field(name="4톡앤티 봇 전자", value="13000t(10개)", inline=True)
        embed.add_field(name="5톡앤티 과학연구소", value="28000t(5개)", inline=True)
        await message.channel.send(embed=embed)

    if message.content.startswith("!주식1"):
        embed = discord.Embed(title="톡사공 도로공사 주식 구매가 예약셨습니다.", description="주식 구매 가능 여부를 확인하고 주식 구매 완료시 구매 완료라고 보내집니다", color=0x00ff00)
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



    if message.content.startswith('!실시간검색어') or message.content.startswith('!실검'):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = "https://www.naver.com/"
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')


        embed = discord.Embed(
            title='네이버 실시간 검색어',
            description='실시간검색어',
            colour=discord.Colour.green()
        )
        for i in range(0,20):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query='+realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i+1)+'위', value='\n'+'[%s](<%s>)' % (realTimeSerach, realURL), inline=False) # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다

        await message.channel.send(embed=embed)


    messages = [f'{len(client.guilds)}개의 서버 | {len(client.users)}명의 유저', "이 메세지는 10초마다 바뀝니다."]
    while True:
       await client.change_presence(status=discord.Status.online, activity=discord.Game(name=messages[0]))
       messages.append(messages.pop(0))
       await asyncio.sleep(10)


@client.event
async def on_guild_join(server):
    print(server,"서버에 접속했습니다!")

@client.event
async def on_guild_remove(server):
    print(server,"서버에서 연결이 끊겼습니다..")






client.run("NjkyNjczNzIwNTAxNjY1ODIy.XrqXnA.QKnxJ-xUkXNqEYNJXTLApr91DyY")
