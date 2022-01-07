from os import system,name
import json
import os
import sys
def install(package):
  if os.name == "nt":
    os.system(f"{sys.executable} -m pip install {package}")
  if os.name == "posix":
    os.system(f"pip install {package}")

try:
  import discord
except ModuleNotFoundError:
  install("discord.py-self")
import discord
try:
  import datetime
except ModuleNotFoundError:
  install("datetime")
import datetime
try:
  import time
except ModuleNotFoundError:
  install("time")
import time
try:
  import asyncio
except ModuleNotFoundError:
  install("asyncio")
import asyncio
try:
  import requests
except ModuleNotFoundError:
  install("requests")
import requests
try:
  import aiohttp
except ModuleNotFoundError:
  install("aiohttp")
import aiohttp
try:
  import proxyscrape
except ModuleNotFoundError:
  install("proxyscrape")
import proxyscrape
from proxyscrape import create_collector
import pathlib
try:
  import random
except ModuleNotFoundError:
  install("random")
import random
from random import choice
from discord import Webhook, AsyncWebhookAdapter
try:
  import re
except ModuleNotFoundError:
  install("re")
import re
try:
  import numpy
except ModuleNotFoundError:
  install("numpy")
import numpy
from colorama import Fore, init
from numpy import random
from discord.ext import commands
from discord.ext.commands import MissingPermissions
from time import sleep
        
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'


bot = commands.Bot(command_prefix='.', self_bot=True)

@bot.command()
async def bump(ctx):
  channel = ctx.channel
  guild= ctx.guild
  if guild.get_member(302050872383242240) is not None:
    await ctx.send('Bump Bot starting! :tada:')
    while True:
      await channel.send('!d bump')
      await ctx.send('Bumped,next bump is 2 hours :tada:')
      time.sleep(7200)

  else:
    await ctx.send('Disboard Bot is not in the server,please invite it to start! :rage:')
@bot.event
async def on_ready():
  print(bcolors.OKBLUE + 'Selfbot is fully ready!')


try:
  bot.run("TOKEN")
  print(bcolors.OKCYAN + 'Logged into Discord.')



except Exception as e:
    if "improper token" in str(e).lower():
        print("bad token.")
    else:
        print(e)
    if os.name == "nt":
        os.system("pause")
    if os.name == "posix":
        input("Press enter to close . . .")

        
        
