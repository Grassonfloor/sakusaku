# This example requires the 'message_content' intent.
import discord
import asyncio
import os
import random
import ast
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
bot1 = discord.Client(intents=intents)
prefix = os.getenv('prefix')
logch = int(os.getenv('logch'))
uptch = int(os.getenv('uptch'))

wlsave = os.getenv('wlsave')

def wl(serverid,check):
  serverid = str(serverid)
  try:
    with open(wlsave, mode='x') as jsonmake:
       jsonmake.write("[]")
       jsonmake.close()
  except FileExistsError:
    pass
  data = open(wlsave, "r")
  data2 = ast.literal_eval(data.read())
  if data2 == "":
    data.close()
    data = open(wlsave, "w")
    data.write("[]")
  data.close()
  if check == "check":
    data = open(wlsave, "r")
    data2 = ast.literal_eval(data.read())
    if serverid in data2:
      data.close()
      return False
    else:
      data.close()
      return True
  else:
    if check == "plus":
      if wl(serverid,"check") == False:
        wl(serverid,"del")
        return False
      else:
        data = open(wlsave, "r")
        data2 = ast.literal_eval(data.read())
        data2.append(serverid)
        data.close()
        data = open(wlsave, "w")
        data.write(str(data2))
        data.close()
        return True
    else:
      if check == "del":
        data = open(wlsave, "r")
        data2 = ast.literal_eval(data.read())
        data2.remove(serverid)
        data.close()
        data = open(wlsave, "w")
        data.write(str(data2))
        data.close()

@bot1.event
async def on_ready():
    print(f'We have logged in as {bot1.user}')
    print(f'Bot ID: {bot1.user.id}')
    channel = bot1.get_channel(uptch)
    await channel.send('Botが起動しました！')

@bot1.event
async def on_message(message):
    if message.author.id == bot1.user.id:
        return
    try:
        id = str(message.guild.id)
    except:
        return
	
    # 以下、登録済みサーバーでのみ反応
    if wl(id,"check") == False:
        if message.content == 'ボカッドカッ' or message.content == 'ボカッ' or message.content == 'ドカッ':
            if not message.channel.nsfw:
                embed = discord.Embed(title="あの",description="nsfwチャンネルでy.meschしてね")
                await message.reply(embed=embed)
            else:
                barie = ["ご、ごめんなさい.....痛い....やめて.....\n-# またあざ残っちゃった、、、","い゛た゛い゛!!!!や゛め゛て゛！","いやっ、、い、、いや、、、\n-# ｼﾞｭｰｰｰ\nあづい！！いだいよぉ！！！！",".......(へんじがないただのしかばねのようだ)","あれ、、、なにもきこえ、、、、\n**ﾊﾞﾀﾝ！**\n(倒れてしまった、体には多くの痣があり、長袖を着ている、、)","ごめんなさい、、服汚れましたよね、、、洗いますから、、怒らないで、、、","い、、いいなりに、、なれ、、、？\nい、、いやで、いや！\n**ベチン！**\nな、、な、、なりますから、、、殴らないで、、、らいたーはやめて、、、","いやっ…もうやめて…","[ﾄﾞｺﾞﾝ！]え、、あっえっ、、なんで包丁が、、、","んにゃ～ぽわぽわ。。。うぅっ、、、きもちわるい、、オエェ、、、[ﾊﾟﾁﾝ!]\nあっ、、あっ、、ごめんなさい、、、うぅっ、、オエェ、、、"]
                hewokoke = random.choice(barie)
                await message.reply(f"||{hewokoke}||", mention_author=False)
                return

        if message.content == 'グサッ' or message.content == 'グサ':
            await message.reply('うっ......', mention_author=False)
            await asyncio.sleep(10)
            await message.reply('蘇生しました')
            return
            
#----------------------------------------------------------------------------------------------------------------------------------
    # y.mesch コマンド
    if message.content == f'{prefix}mesch':
        if not message.guild:
            await message.reply('だからdmで実行して何に、、、', mention_author=False)
            return
        if not message.author.guild_permissions.administrator:
            await message.reply('管理者持ってから来てね。', mention_author=False)
            return
        try:
          id = str(message.guild.id)
        except:
          return
        if wl(id,"plus") == True:
            await message.reply("meschをおんにしたよ！")
        else:
            await message.reply("meschをおふにしたよ！")

    # ボットがメンションに含まれているかチェック
    if bot1.user in message.mentions:
        naiyo = ["よーんだ？え？よんでないの？","ふぇっ、急によばないでよぉ!","Googleアシスタントに朝7:00にサクサクを呼ぶって設定した？","うわっ!ﾊﾟﾘｰﾝ....ブロンの瓶割っちゃったじゃないですか!","呼んでもブロンは出てきませんよ?、え?手に持ってるブロン30錠よこせ?嫌ですよ!","なんですか眠剤飲んだばっかなのに..."]
        hoinara = random.choice(naiyo)
        await message.reply(hoinara,mention_author=False)

# インポート時は実行せず、直接実行時のみbotを起動
if __name__ == '__main__':
    bot1.run(os.getenv('token'))
