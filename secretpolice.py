# 3.7.2
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$', description='To Enforce the Rule of the Supreme Leader')

@bot.command()
async def test(ctx):
    await ctx.send("time to end free speech")

