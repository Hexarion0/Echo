import discord
from discord.ext import commands

class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, message="No reason"):
        try:
            await member.send(f"You have been kicked from {ctx.guild} by {ctx.author}. Reason: {message}")
        except discord.Forbidden:
            pass  # couldn't DM them, continue anyway
        await member.kick()
        await ctx.reply(f"{member} was kicked by {ctx.author}.")

async def setup(bot):
    await bot.add_cog(Kick(bot))