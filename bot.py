import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

intents=discord.Intents.default()
intents.members=True
bot = commands.Bot(command_prefix='#', intents=intents)

@bot.event
async def on_ready():
    print('Bot is online')
@bot.command()
async def ping(ctx):
    await ctx.send(bot.latency)
 
bot.run(jdata['TOKEN'])
