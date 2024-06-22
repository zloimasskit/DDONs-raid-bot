import discord
from discord.ext import commands

max = "10" #max send message

message_1 = ""
message_2 = ""


prefix = '/'
token =  ''

intents = discord.Intents.default()

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.listen('on_message')

async def hello(ctx):
    await ctx.channel.send(message_1)
    await ctx.channel.send(message_2)





bot.run(token)