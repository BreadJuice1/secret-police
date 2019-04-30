# 3.7.2

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)



bot.run('NTcyNTY2OTYwMDE0MDk4NDcy.XMegcA.8td8bKrohhmd_7XXF5syGiqcHNA')
