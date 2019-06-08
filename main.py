import discord

TOKEN = 'NTg2NTc0MDA2NTM5Mzg2OTU1.XPqKCg.NPcGoo5ZoW4VE82GgF2z5EUcers'
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
    print('client.user-id')
    print('------')

client.run('TOKEN')
