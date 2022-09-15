import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

    channel = client.get_channel(1019261795531235390)
    await channel.send('Bot is ONLINE')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    hitchhiker_quotes = [
        'There is an art, it says, or rather, a knack to flying. The knack lies in learning how to throw yourself at the ground and miss.',
        'It is a mistake to think you can solve any major problems just with potatoes.',
        'In the beginning the Universe was created. This has made a lot of people very angry and been widely regarded as a bad move.',
        'A common mistake that people make when trying to design something completely foolproof is to underestimate the ingenuity of complete fools.',
    ]

    spongebob_quotes = [
        'Once upon a time there was an ugly barnacle. He was so ugly that everyone died. The end!',
        'Want to know something funnier than 24?....25!',
        'I’ll have you know that I stubbed my toe last week and only cried for 20 minutes.',
        'We\'re not cavemen....we have technology',
        'The inner machinations of my mind are an enigma.',
    ]

    if message.content == '!spongequote':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(spongebob_quotes)
        await message.channel.send(response)

client.run(TOKEN)
