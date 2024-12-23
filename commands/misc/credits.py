

# //made by @yxzhin with <3
# //#hellokittysupremacy #finelcomeback #yxzhinsave


from discord.ext.commands import Cog, guild_only, command, Context, Bot
from lib.yaf_honeylib10 import emb
from discord import Color


class Command(Cog):

    def __init__(self, bot: Bot):

        self.__cog_name__ = "Credits"

        self.bot = bot

    @guild_only()
    @command(aliases=["credits"])
    async def __credits(self, ctx: Context):

        embed = emb(
            ctx,
            "**made by `yxzhin`, `grygoryzach`, `dermann123`, `ronkly`.\ncopyright (c) bljinciki 2024. all rights reserved.**",
            Color.gold(),
        )

        await ctx.reply(embed=embed)
