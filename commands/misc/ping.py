

# //made by @yxzhin with <3
# //#hellokittysupremacy #finelcomeback #yxzhinsave


from discord.ext.commands import Cog, guild_only, command, Context, Bot


class Command(Cog):

    def __init__(self, bot: Bot):

        self.__cog_name__ = "Ping"

        self.bot = bot

    @guild_only()
    @command(aliases=["ping"])
    async def __ping(self, ctx: Context):

        await ctx.reply(f"`pong! speed: {self.bot.latency}s`")
