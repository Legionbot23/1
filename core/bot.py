import discord
import os

from discord.ext.commands import Bot

class Hikki(Bot):
  def __init__(self):
    super().__init__(command_prefix="!")
    self.init()
    
    
  def init(self):
    self.token = os.getenv("TOKEN")
    self.color = (34, 255, 145)
    
    for file in os.listdir('./cogs'):
      if file[-3:] == '.py':
        try:
          self.load_extension(f'cogs.{file[0:-3]}')
          print(f'[+] cogs.{file[0:-3]}')
        except BaseException as err:
          print(f'[!] cogs.{file[0:-3]} error: `{err}`')
    print('-' * 30)
    
    
  def startup(self):
    super().run(self.token)
      
  async def on_ready(self):
    print("ready")

    game = discord.Game(name='Привет')
    await self.change_presence(status=discord.Status.idle, activity=game)
      
bot = Hikki()

