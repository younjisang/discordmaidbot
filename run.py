import asyncio,discord,os
from discord.ext import commands

token_path = os.path.dirname( os.path.abspath(__file__))+"/token.txt"
t = open(token_path, "r",encoding="utf-8")
token = t.read().split()[0]
print("Token_key : ", token)

game = discord.Game("도움")
bot = commands.Bot(command_prefix='',status=discord.Status.online,activity=game,help_command=None)

game = discord.Game("일")
bot = commands.Bot(command_prefix='',status=discord.Status.online,activity=game,help_command=None)
@bot.event
async def on_ready():
    print("시스템 가동")

@bot.command()
async def 메이드(ctx):
    await ctx.send("무엇을 도와드릴까요?")

@bot.command()
async def 인사(ctx):
    embed=discord.Embed(title=f"미친놈들 모음집에 오신 것을 환영해요!!", description=f"미친 놈들만을 위한 서버", color=0xf3bb76)
    embed.add_field(name=f"여기는요?", value=f"패드립 빼고 다 허용이랍니다")
    await ctx.send(embed=embed)


@bot.command()
async def on_member_join(ctx):
    embed=discord.Embed(title=f"미친놈들 모음집에 오신 것을 환영해요!!", description=f"미친 놈들만을 위한 서버", color=0xf3bb76)
    embed.add_field(name=f"여기는요?", value=f"패드립 빼고 다 허용이랍니다")
    await ctx.send(embed=embed)

@bot.command()
async def on_member_remove(ctx):
    await ctx.send("<@{}>은 임포스터가 아니였습니다")

bot.run(token)

