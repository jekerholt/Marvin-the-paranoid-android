import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send('Hello!')
    if message.content.startswith('!jan'):
        await message.channel.send('Jan er flink i BF')

client.run('NjM0NDE1MjgyMTE4NTkwNDg0.XaiLsA._vzo0tIgqppS0kZToKbeQ35OlFs')

