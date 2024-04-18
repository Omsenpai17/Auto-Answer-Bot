import discord
import time
import json
import asyncio
from discord.ext import commands


bot = commands.Bot(command_prefix="!!")

with open('config.json',"r") as tkn:
	data = tkn["Token"]

@bot.event
async def on_ready():
	print(f"Ready bot {bot.user}")
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="NewbieWIRP"))

@bot.event
async def on_message(message):
	if message.author.id == bot.user.id:
			return
	if message.channel.id == 1149395231100387418 or message.channel.id == 1146083561141714965:
		if "ip" in message.content or "Ip" in message.content or "IP" in message.content:
			async with message.channel.typing():	
				await asyncio.sleep(2)
				await message.reply('<#1150809090805739541>', mention_author=True)


bot.run(token=data)