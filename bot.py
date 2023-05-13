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
async def 我吃草喔(ctx):
        await ctx.send('操你媽郭玉米')
@client.command()
async def kd(ctx):
        await ctx.send('嗝~~~')
@client.command()
async def 檸檬汁(ctx):
        await ctx.send('我真的是操你嗎')
@client.command()
async def 捏哈哈(ctx):
        await ctx.send('嘻嘻嘻嘻嘻嘻')
@client.command()
async def 母親節(ctx):
        await ctx.send('母親，您是生命的源泉，是愛的載體，是生命的慈母。您用母愛澆灌每個生命，用堅強和智慧撐起一片天。        您辛勤耕耘，不求回報，用您的智慧和勞動換取家庭的安寧和幸福。您的懷裡，我們感受到了溫暖，在您的指引下，我們走過了茫茫黑暗。在您身上，我看到了堅毅與柔軟，您是家庭的支柱，是事業的助力。在您的懷抱中，我們得到了力量，在您的教誨中，我們學會了做人的道理。        母親，您的偉大無法言喻，您是我們生命中最重要的人。今天，讓我們為您歌頌，為您的偉大和付出喝彩。        母親，您是我們生命中的太陽，是我們前進的方向和信仰。我們永遠愛您，感激您的偉大，願您永遠幸福，身體健康，平安愉快！')
@client.command()
async def 早安(ctx):
        await ctx.send('親愛的朋友，早晨是一天中最美好的時光，它代表著新的開始和機會。我知道有時候起床可能會很困難，但是讓我提醒你一下，你是如此的珍貴和重要，這個世界需要你的存在。在這個美好的早晨，我希望你能夠感受到我的關心和祝福。我祝願你擁有一個美好的一天，充滿著喜悅和幸福。請記得在你開始今天的工作之前，給自己足夠的時間來做好身心的準備。可以透過拉伸、慢跑或靜坐冥想來提升身心的能量和活力。最後，我想再次祝你早安！讓我們為今天的每一刻感到興奮和期待，共同迎接一個美好的新的一天!')
@client.command()
async def 晚安(ctx):
        await ctx.send('親愛的朋友，你知道嗎？每晚充足的睡眠是保持身心健康的重要關鍵。如果你經常熬夜，睡眠不足可能會對你的身體產生負面影響，包括疲勞、焦慮、壓力、注意力不集中等等。我知道現在可能有很多事情需要你去處理，但請不要忘記，身體健康才是你能夠繼續追求夢想和成就目標的基礎。所以，在這裡，我真心希望你能夠儘早休息，享受高質量的睡眠，讓你明天早上醒來時感覺充滿活力，精神煥發。如果你需要一些幫助來改善睡眠質量，這裡有一些建議：創造一個舒適的環境：確保房間安靜、黑暗和涼爽，使用舒適的床單和枕頭。建立一個固定的睡眠時間表：嘗試每晚在相同的時間入睡和醒來，即使在周末也要盡量保持一致。放鬆身心：嘗試透過冥想、深呼吸、聽輕音樂等方法來放鬆身心，減少熬夜對身體的壓力。減少咖啡因和酒精的攝入：這些飲料可能會影響你的睡眠質量，盡量減少飲用量。最後，我希望你能夠照顧好自己，保持健康的生活方式。謝謝你聆聽我的建議，晚安！')
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
@client.command()
async def c(ctx):
    folder_path = 'C:/Users/nick6/Documents/GitHub/Tut_Bot/pic' # 將 "your/folder/path" 替換為你的資料夾路徑
    images = os.listdir(folder_path)
    image_path = os.path.join(folder_path, images[3]) # 取得第一張圖片的路徑
    with open(image_path, 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)
client.run(jdata['TOKEN'])
