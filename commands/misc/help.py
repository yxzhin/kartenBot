

# //made by @yxzhin with <3
# //#hellokittysupremacy #finelcomeback #yxzhinsave


from discord.ext.commands import Cog, guild_only, command, Context, Bot
from discord.ui import View, Button
from discord import ButtonStyle, Color, Message, Interaction
from lib.yaf_honeylib10 import emb
from config.conf import prefix, help_text
from lib.error_getter import error_getter


class Command(Cog):

    def __init__(self, bot: Bot):

        self.__cog_name__ = "Help"

        self.bot = bot

        self.pages = dict()

    @guild_only()
    @command(aliases=["help"])
    async def __help(self, ctx: Context):

        if self.pages.get(ctx.author.id):

            await error_getter(ctx, -17)

            return

        maxpages = len(help_text.keys())//4
        keys = list(help_text.keys())
        values = list(help_text.values())

        self.pages[ctx.author.id] = 1

        def check(interaction: Interaction):

            return interaction.user == ctx.author and interaction.channel == ctx.channel

        async def back_callback(interaction: Interaction):

            self.pages[ctx.author.id] -= 1

        async def next_callback(interaction: Interaction):

            self.pages[ctx.author.id] += 1

        back = Button(
            style=ButtonStyle.red,
            custom_id="back",
            label="⬅️",
        )

        next_ = Button(
            style=ButtonStyle.green,
            custom_id="next",
            label="➡️",
        )

        back.callback, next_.callback = back_callback, next_callback

        embed = emb(
            ctx,
            "Загрузка...",
        )

        message: Message = await ctx.reply(embed=embed)

        while True:

            embed = emb(
                ctx,
                f"Помощь | страница {self.pages[ctx.author.id]}/{maxpages}",
                Color.from_rgb(0, 255, 0),
            )

            to = self.pages[ctx.author.id]*4
            from_ = to-4

            for i in range(from_, to):

                embed.add_field(
                    name=f"`{prefix}{keys[i]}`",
                    value=f"`{values[i]}`",
                    inline=False,
                )

            back.disabled, next_.disabled = False, False

            if self.pages[ctx.author.id] == 1:

                back.disabled = True

            if self.pages[ctx.author.id] == maxpages:

                next_.disabled = True

            await message.edit(embed=embed, view=View().add_item(back).add_item(next_))

            try:

                await self.bot.wait_for("interaction", check=check, timeout=60)

            except TimeoutError:

                embed = emb(
                    ctx,
                    "Закрыто из-за бездействия пользователя."
                )

                await message.edit(embed=embed, view=None)

                del self.pages[ctx.author.id]

                return
