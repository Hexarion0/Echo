from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="help")
    async def help(self, ctx):
        await ctx.send("Pong!")

async def setup(bot):
    await bot.add_cog(Help(bot))