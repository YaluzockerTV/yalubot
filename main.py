import discord
from discord.ext import commands
from discord.ext import Bot
import asyncio
import random
import requests
import os

client = discord.Client()


@client.event
async def on_message(message):
    if message.authoer == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.servermessage(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print('client.user.name')
    print('chekc my website to start www.website.com')
    print('------')

client.run(str(os.environ.get('BOT_TOKEN')))
