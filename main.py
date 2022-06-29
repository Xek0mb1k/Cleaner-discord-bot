import discord
from discord.ext import commands
TOKEN = '' # There should be a secret code here

bot = commands.Bot(command_prefix='%')
@bot.command(pass_context=True)
async def hello(m):
    await m.send('Hi, i`m bot')

@bot.command(pass_context=True)
async def wash(ctx):
    await ctx.channel.purge()
    

@bot.command(pass_context=True)
async def clean(s,k):
    await s.channel.purge(limit = int(k))
    

@bot.command(pass_context=True)
async def spam(m,op):
    for i in range(int(op)):
        await m.send(i)

@bot.command(pass_context=True)
async def spamone(m,op,heh):
    for opops in range(int(op)):
        await m.send(heh)
bot.run(TOKEN)
