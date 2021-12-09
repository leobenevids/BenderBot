import datetime
import discord
from discord.ext import commands, tasks
import random

bot = commands.Bot(command_prefix = ">", case_insensitive = True)

@bot.event
async def on_ready():
    print('Entramos como {0.user.name}'.format(bot))
    current_time.start()

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if "palavrão" in message.content:
        await message.channel.send(f'Ó o palavrão, {message.author.name}!!')

        await message.delete()
    
    await bot.process_commands(message)

@bot.command(name="oi")
async def ola(ctx):
    await ctx.send(f'Olá, {ctx.author.name}!')

@bot.command()
async def dado(ctx, numero):
    variavel = random.randint(1, int(numero))
    await ctx.send(f'O número que saiu no dado é {variavel}')

@tasks.loop(seconds=10)
async def current_time():
    now = datetime.datetime.now()

    now = now.strftime("%d/%m/%Y às %H:%M:%S")

    channel = bot.get_channel(918567213772984361)

    await channel.send("Data atual: " + now)



bot.run('OTE4NTQzMjg0ODUzNDIwMTIz.YbIyGA.Xp17yyygKfDvf8A8tEznNhrAqYg')