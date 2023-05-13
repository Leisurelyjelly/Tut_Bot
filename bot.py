import discord
from discord.ext import commands

intents=discord.Intents.default()
intents.members=True
bot = commands.Bot(command_prefix='[', intents=intents)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(1106795534435504178)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(1106795534435504178)
    await channel.send(f'{member} leave!')

@bot.command()
async def ping(ctx):
    await ctx.send(f'{round(bot.latency*1000)}(ms)')
    print(f'{round(bot.latency*1000)}(ms)')
@bot.event
async def on_message(message):
    print(f'Received message: {message.content}')
    await bot.process_commands(message)

bot.run('MTEwNjg3MjQ2MjUzMDA3MjYyNg.GRRknR.qjy89NAqC-ULfYJQsh9MCK58h4SK_AqJBb3bfc')
