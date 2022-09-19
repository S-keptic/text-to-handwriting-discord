import discord
from discord import app_commands
from discord.ext import commands
import pywhatkit as pw
import asyncio
bot= commands.Bot(command_prefix='?', intents=discord.Intents.all())
import requests


@bot.event
async def on_ready():
    print("bot is ready")
    try: 
        synced= await bot.tree.sync()
        print(f"synced {len(synced)} nodes")
    except Exception as e:
        print(f"error{e}")






@bot.tree.command(name="text_to_handwriting" , description="Enter text to convert it into handwritten")
async def pdff(interaction: discord.Interaction , enter:str):
    await interaction.response.send_message("`your output will be given shortly`")
    pw.text_to_handwriting(enter,'demo.png',(0,0,138))
    
    channel = bot.get_channel(1017445756275261513)
    await channel.send(file=discord.File('demo.png'))

    
   






bot.run("")

