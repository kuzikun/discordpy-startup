from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

import random 
   if message.content == "樋□さんお話しして！":
　　　　　#↓
       hennnahuri = ["せんわ", "みんなでハワイ行きたいなぁ", "整地してるから黙って？", "あ", "そのフリはつまらん", "君はもう少し服にお金かけてもいいと思うよ", "無理"]
       choice = random.choice(hennnahuri)＃←
       await message.channel.send(choice)
   
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

        
bot.run(token)
