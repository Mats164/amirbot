# bot.py
from asyncio import events
from operator import add
import os
import discord
import random
# from dotenv import load_dotenv

intents = discord.Intents.all()
client = discord.Client(intents=intents)

# load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

@client.event
async def on_ready():
    number_of_guilds = len(client.guilds)
    guild = discord.utils.get(client.guilds, name = GUILD)
    print(
        f'{client.user} is connected to the following {number_of_guilds} guild:\n'
        f'{guild.name} (id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hei {member.name}, er det teori eller hypotese?'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    amirQuotes = [
        'Er det teori eller hypotese da?', 'Jeg skal grille deg!', 
    ]

    if random.randint(0, 5) == 2:
        response = random.choice(amirQuotes)
        await message.channel.send(response)

    if message.content == '!grill':
        response = random.choice(amirQuotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

client.run(TOKEN)