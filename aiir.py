import discord
import logging
import asyncio
import time
import aiohttp

import config

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




@bot.event
async def on_ready():
    print(discord.__version__)
    print("Alright bitches, she's all yours.")

@bot.command(pass_context=True)
async def accept(ctx, afterlimit=7):
    role = discord.utils.get(ctx.message.server.roles, name='Full Access')
    if role in ctx.message.author.roles:
        themsg = await bot.send_message(ctx.message.channel, 'You already have full access.')

        await asyncio.sleep(afterlimit)
        await bot.delete_message(ctx.message)
        await bot.delete_message(themsg)
    else:
        await bot.add_roles(ctx.message.author, role)
        themsg = await bot.send_message(ctx.message.channel, 'You have been granted full access to JAM.S! Please follow the rules at all times.')

        await asyncio.sleep(afterlimit)
        await bot.delete_message(ctx.message)
        await bot.delete_message(themsg)

@bot.command(pass_context=True)
async def animetiddy(ctx):
    bleh = discord.Embed(title="Gross...", color=0xFF69B4)
    bleh.set_image(url="https://xenorealms.com/rem/botmedia/bleh.gif")
    await bot.send_message(ctx.message.channel, embed=bleh)

bot.run(config.token)
