import discord
from discord.ext import commands

prefix = '!'
token =  'MTI1NDE2MDMzNjYyMjQ1MjgyNw.Gz-mHA.lJlAzvjRHRbUw48iWZyh2mbiva9kwCan8Y33rA'

intent = discord.Intents().all()

bot = commands.Bot(command_prefix=prefix, intents=intent)

@bot.command()

async def hello(ctx):
    await ctx.reply("я гитлер")
    
    
    
    
    
    
    
    
    
bot.run(token)