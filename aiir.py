import discord
import logging
import asyncio
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

from discord.ext import commands
from discord.ext.commands import Bot

bot = commands.Bot(command_prefix="!")

message = discord.Message


# @bot.event
# async def on_ready():
    # print('Private Voice Channel Bot connected. User: {0}'.format(bot.user))

@bot.event
async def on_ready():
    print(discord.__version__)

@bot.command(pass_context=True)
async def accept(ctx):
    role = discord.utils.get(ctx.message.server.roles, name='Full Access')
    if role in ctx.message.author.roles:
        await bot.send_message(ctx.message.channel, "You already have full access.")
    else:
        await bot.add_roles(ctx.message.author, role)
        await bot.send_message(ctx.message.author, 'You have been granted full access to JAM.S! Please follow the rules at all times.')

bot.run('insert token here')
