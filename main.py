import discord


client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print('client.user.name')
    print('This Bot is still in Alpha')
    print('------')

client.run('NTg2NTc0MDA2NTM5Mzg2OTU1.XPqKCg.NPcGoo5ZoW4VE82GgF2z5EUcers')
