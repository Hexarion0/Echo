import random
from discord.ext import commands

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def roll(self, ctx, sides=6):
        randomnum = random.randint(1, sides)
        await ctx.reply(f"The lucky number is {randomnum}!")

async def setup(bot):
    await bot.add_cog(Roll(bot))