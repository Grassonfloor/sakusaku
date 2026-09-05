import discord 
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong!:ping_pong:\nBotのPing値は{latency}です。")

async def setup(bot: commands.Cog):
    await bot.add_cog(Ping(bot))