

# //made by @yxzhin with <3
# //#hellokittysupremacy #finelcomeback #yxzhinsave


from discord.ext.commands import Cog, guild_only, command, Context, Bot


class Command(Cog):

    def __init__(self, bot: Bot):

        self.__cog_name__ = ""

        self.bot = bot

    @guild_only()
    @command(aliases=[""])
    async def __(self, ctx: Context):

        ...
