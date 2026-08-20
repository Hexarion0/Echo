import random
from discord.ext import commands

class Eightball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="8ball")
    async def eightball(self, ctx):
        eightballList = ["It is certain.", "Ask again later.", "Don't count on it."]
        await ctx.reply(random.choice(eightballList))

async def setup(bot):
    await bot.add_cog(Eightball(bot))