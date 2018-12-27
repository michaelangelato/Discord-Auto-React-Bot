import discord
from discord.ext    import commands
from discord.ext.commands   import Bot
import asyncio
 
bot = commands.Bot(command_prefix='whatever_prefix_u_want_here')
 
@bot.event
async def on_ready():
    print ("whatever_text_u_want_here")
 
 
@bot.event
async def on_message(message):
    if(message.channel.id == "channel_id_here"):
        await bot.add_reaction(message, "discord_emote_id_here")
 
 
bot.run("bot_token_here")
