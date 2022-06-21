import discord

from discord.ext import commands
from logging_files.information_logging import logger

class Info(commands.Cog):
    def __init__(self, bot):
      self.bot = bot
      self.color = bot.color
      self.status = {
        "online": "<:online:648014037010874419>",
        "idle": "<:idle:648014173543989261>",
        "offline": "<:offline:648014210525298688>",
        "dnd": "<:dnd:648014190417674250>"
      }
    
    @commands.group(invoke_without_command=True, aliases=["commands"])
    async def poly_commands(self, ctx):
        # ➜ ‣ —
        embed = discord.Embed(
            color= discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title= "➜ Bot Command Categories")
        
        embed.add_field(name= "‣ Moderation commands:", inline= False, value= "`!commands moderation`")
        embed.add_field(name= "‣ Utility commmands:", inline= False, value= "`!commands utility`")
        embed.add_field(name= "‣ Information commands:", inline= False, value= "`!commands information`")
        embed.add_field(name= "‣ Fun commands: (Coming Soon)", inline= False, value= "`!commands fun`")
        embed.add_field(name= "‣ Settings: (Coming Soon)", inline= False, value= "`!commands settings`")
        embed.add_field(name= "‣ Music commands: (Coming Soon)", inline= False, value= "`!commands music`")
        
        embed.set_thumbnail(url= ctx.guild.icon_url_as(size= 4096, format= None, static_format= "png"))
        embed.set_footer(icon_url= ctx.author.avatar_url_as(size= 4096, format= None, static_format= "png"), text= f"{ctx.author.name}")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Commands: {ctx.author}")

    @poly_commands.command()
    async def moderation(self, ctx):
        moderation = "`!purge`, `!warn`, `!kick`, `!ban`, `!forceban`, `!unban`, `!nickname`, `!resetnick`"

        embed = discord.Embed(
            color= discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title= "➜ Listing all commands",
            description= f"‣ All **Moderation** Commands \n—\n{moderation}")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Moderation Commands: {ctx.author}")

    @poly_commands.command()
    async def utility(self, ctx):
        utility = "`!suggest`"

        embed = discord.Embed(
            color= discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title= "➜ Listing all commands",
            description= f"‣ All **Utility** Commands \n—\n{utility}")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Utility Commands: {ctx.author}")

    @poly_commands.command()
    async def information(self, ctx):
        information = "`!whois`"

        embed = discord.Embed(
            color=discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title="➜ Listing all commands",
            description=f"‣ All **Information** Commands \n—\n{information}")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Information Commands: {ctx.author}")

    @commands.command(aliases=["whois"])
    async def userinfo(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]
        roles = f" ".join([f"@{role}, " for role in roles])
        activity = member.activity.name if member.activity else"No current activity."
        is_bot = ":robot:" if member.bot else ":no_entry_sign:"
        device = ":iphone:" if member.is_on_mobile() else ":no_mobile_phones:"
        joined = member.joined_at.strftime("%A %d, %B %Y")
        created = member.created_at.strftime("%A %d, %B %Y")
        status = self.status

        embed = discord.Embed(
            color= discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
            title= f"➜ Userinfo for: {member}",
            description= f"• Information will be displayed about the user below.")
        
        embed.set_thumbnail(url= member.avatar_url_as(size= 4096, format= None, static_format= "png"))
        embed.add_field(name= "‣ Account Name", value= str(member))
        embed.add_field(name= "‣ Discord ID", value= str(member.id))
        embed.add_field(name= "‣ Nickname", value= member.nick or "No nickname.")
        embed.add_field(name= "‣ Account Created At", value= created)
        embed.add_field(name= "‣ Account Joined At", value= joined)
        embed.add_field(name= "‣ Current Activity", value= activity)
        embed.add_field(name= "‣ Discord Bot? ", value= is_bot)
        embed.add_field(name= "‣ On Mobile Device? ", value= device)
        embed.add_field(name= "‣ Current Status", value= status[member.status.name])
        embed.add_field(name= "‣ Highest Role", inline= False, value= f"```@{member.top_role}```")
        # embed.add_field(name="‣ All Roles", inline=False, value=f"```{roles}```")

        await ctx.send(embed=embed)

        logger.info(f"Information | Sent Whois: {ctx.author} | To: {member}")

    @userinfo.error
    async def userinfo_error(self, ctx, error):
      
        if isinstance(error, commands.BadArgument):
            embed = discord.Embed(
                color = discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title = "➜ Passed Invalid Member",
                description = "‣ Please mention a valid member. Example: `!whois @user`")
            
            await ctx.send(embed=embed)
            
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                color = discord.Color.from_rgb(self.color[0], self.color[1], self.color[2]),
                title = "➜ Passed Invalid Argument",
                description = "‣ Please put a valid parameter. Example: `!whois @user`")
            
            await ctx.send(embed=embed)



def setup(bot):
    bot.add_cog(Info(bot))