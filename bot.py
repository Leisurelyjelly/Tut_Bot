import discord
import os
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8')as jfile:
    jdata=json.load(jfile)

intents=discord.Intents.default()
intents.members=True
intents.message_content=True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print('bot ready')

@client.command()
async def hello(ctx):
        await ctx.send('hello wow')
@client.command()
async def luxin(ctx):
    folder_path = 'C:/Users/nick6/Documents/GitHub/Tut_Bot/pic' # 將 "your/folder/path" 替換為你的資料夾路徑
    images = os.listdir(folder_path)
    image_path = os.path.join(folder_path, images[0]) # 取得第一張圖片的路徑
    with open(image_path, 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
@client.command()
async def a(ctx):
    folder_path = 'C:/Users/nick6/Documents/GitHub/Tut_Bot/pic' # 將 "your/folder/path" 替換為你的資料夾路徑
    images = os.listdir(folder_path)
    image_path = os.path.join(folder_path, images[1]) # 取得第一張圖片的路徑
    with open(image_path, 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
@client.command()
async def b(ctx):
    folder_path = 'C:/Users/nick6/Documents/GitHub/Tut_Bot/pic' # 將 "your/folder/path" 替換為你的資料夾路徑
    images = os.listdir(folder_path)
    image_path = os.path.join(folder_path, images[2]) # 取得第一張圖片的路徑
    with open(image_path, 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
client.run(jdata['TOKEN'])
