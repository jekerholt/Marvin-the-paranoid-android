import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if any([keyword in message.content() for keyword in('bush','quote','tiss')]):
        await message.channel.send('Heres a quote')

client.run('NjEzMzcxNTc1Mzc4NTA5ODM0.XZnMYQ.tLXYV4B0IWd1E7n2wS9HsVgsL10')
