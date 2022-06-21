import discord
import asyncio

from discord.ext import commands

class Reactions(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    
  #@commands.Cog.listener()
  #async def on_ready(self):
  #  print("ready")
    
   # while True:
    #    ch = self.bot.get_guild(669063153950392320).get_channel(669070062069612559)
     #   print(ch)
        
      #  await asyncio.sleep(21600)
  


def setup(bot):
  bot.add_cog(Reactions(bot))