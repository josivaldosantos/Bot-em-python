import discord
import json
import random
import os
from discord.ext import commands
import asyncio

client = discord.Client()

with open('config.json') as e:
    config = json.load(e)
    TOKEN = config['token']
    prefixo = config['prefixo']
    owner_id = config['owner_id']

client = commands.Bot(command_prefix=prefixo)

# Evento pra informar que o bot está online
@client.event
async def on_ready():
    activity = discord.Game(name='Em desenvolvimento', type=3)
    await client.change_presence(status=discord.Status.online, activity=activity)
    print('Conectado como: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    print(f'Ping: {round (client.latency * 1000)}')

# Evento que avisa ao usúario se ele digitar um comando que não existe
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
            title='Ops! 😥',
            description='Error: {}'.format(error),
            colour=discord.Colour.from_rgb(0, 255, 0)
        )
        await ctx.send(embed=embed, delete_after=10.0)
    
## comandos

# Hello World
@client.command(name='hello')
async def HelloWorld(ctx):
    await ctx.send('Hello World!')

# Apenas um comando de teste
@client.command(name='gift')
async def GIFT(ctx):
    try:
        await ctx.author.send('Use: ``4gshb3b4b`` para resgatar seu premio')
    except discord.errors.Forbidden:
        await ctx.send('Infelizmente não consigo lhe enviar mensagens privadas!')


#comando de clear
@client.command(name="clear")
async def Clear(ctx, number=None):
    if number==None:
        await ctx.send('Você precisa informar um número de mensagens para serem apagadas Exp: `$clear 50`.')
    else:
        await ctx.channel.purge(limit= int(number)+1)
        await ctx.send(f'foram apagadas {number} mensagens!')

#comando de ping
@client.command(name="ping")
async def p(ctx):
    await ctx.send(f'🏓Pong! Meu ping é de: `{round (client.latency * 1000)} ms` ')

#comando de dado pra rpg
@client.command(name="roll")
async def roll(ctx, numero):
    numero = int(numero)
    if numero > 100:
        while numero > 100:
            numero = int(numero)
    dado = random.randint(1,100)
    v1 = (dado*100)/numero
    if v1 >= 1 and v1 <= 5:
        await ctx.send(f'Valor do dado é: ``{dado}`` \nExtremo')
    if v1 >= 6 and v1 <= 20:
        await ctx.send(f'Valor do dado é: ``{dado}`` \nBom')
    if v1 >= 21 and v1 <=100:
        await ctx.send(f'Valor do dado é: ``{dado}`` \nNormal')
    if v1 >=100:
        await ctx.send(f'Valor do dado é: ``{dado}`` \nFracasso')
    


client.run(TOKEN)
