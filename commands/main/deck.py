

# //made by @yxzhin with <3
# //#hellokittysupremacy #finelcomeback #yxzhinsave


from discord.ext.commands import Cog, guild_only, command, Context, Bot
from requests import get
import config.conf as config
from lib.yaf_honeylib10 import emb
from lib.error_getter import error_getter
from lib.ExploitPatch_v1_0_CGI import ExploitPatch
from json import loads
from discord import Color, Interaction, ButtonStyle, Message
from discord.ui import View, Button
from random import choice


class Command(Cog):

    def __init__(self, bot: Bot):

        self.__cog_name__ = "Deck"

        self.bot = bot

        self.pages, self.sides = dict(), dict()

    @guild_only()
    @command(aliases=["deck"])
    async def __deck(self, ctx: Context, id_):

        if self.pages.get(ctx.author.id):

            await error_getter(ctx, -17)

            return

        if ExploitPatch.containsString(id_):

            strings = ExploitPatch.clearNumbers(id_)

            await error_getter(ctx, -4, args=[strings])
            return

        embed = emb(
            ctx,
            "Загрузка...",
        )

        message: Message = await ctx.reply(embed=embed)

        result = get(fr"{config.api_url}/deck/{id_}?secret={config.secret}")

        if not result.ok:

            await error_getter(ctx, -1)
            return

        if result.text == "-1":

            embed = emb(
                ctx,
                fr"**:x: Колода с id {id_} не найдена!**",
            )

            await ctx.reply(embed=embed)
            return

        self.pages[ctx.author.id] = 1
        self.sides[ctx.author.id] = "front"

        def check(interaction: Interaction):

            return interaction.user == ctx.author and interaction.channel == ctx.channel

        async def rotate_callback(interaction):

            self.sides[ctx.author.id] = "front" if self.sides[ctx.author.id] == "back" else "back"

        async def back_callback(interaction):

            self.pages[ctx.author.id] -= 1

        async def next_callback(interaction):

            self.pages[ctx.author.id] += 1

        rotate = Button(
            style=ButtonStyle.blurple,
            custom_id="rotate",
            label="🔁",
        )

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

        rotate.callback, back.callback, next_.callback = rotate_callback, back_callback, next_callback

        deck_dict: dict = loads(result.text)

        deck_name = deck_dict["deck_name"]
        deck_author = deck_dict["user_created_name"]

        splt = deck_dict["time_changed"].split()
        splt1, splt2 = splt[0].split("-"), splt[1].split("-")
        y, mt, d, h, mn, s = splt1[0], splt1[1], splt1[2], splt2[0], splt2[1], splt2[2]
        deck_creation = fr"{d}.{mt}.{y}. {h}:{mn}:{s}"

        cards_count = len(deck_dict["cards"])

        while True:

            color = choice(
                [
                    Color.red, Color.orange, Color.yellow, Color.green, Color.blue, Color.blurple, Color.pink,
                ]
            )

            embed = emb(
                ctx,
                fr"**~Колода {id_}~** Карточка #{self.pages[ctx.author.id]}/{cards_count}",
                color(),
            )

            embed.add_field(
                name="Название:",
                value=fr"`„{deck_name}“`;",
                inline=False,
            )

            embed.add_field(
                name="Автор:",
                value=fr"`~{deck_author}~`;",
                inline=False,
            )

            embed.add_field(
                name="Создано:",
                value=fr"`{deck_creation}`;",
                inline=False,
            ),

            card = deck_dict["cards"][self.pages[ctx.author.id]-1]
            side = "верхняя" if self.sides[ctx.author.id] == "front" else "обратная"
            side_text = card[self.sides[ctx.author.id]]

            embed.add_field(
                name=fr"Сторона: {side}",
                value=fr"`{side_text}`",
                inline=False,
            )

            back.disabled, next_.disabled = False, False

            if self.pages[ctx.author.id] == 1:

                back.disabled = True

            if self.pages[ctx.author.id] == cards_count:

                next_.disabled = True

            await message.edit(embed=embed, view=View().add_item(rotate).add_item(back).add_item(next_))

            try:

                await self.bot.wait_for("interaction", check=check, timeout=60)

            except TimeoutError:

                embed = emb(
                    ctx,
                    "Закрыто из-за бездействия пользователя."
                )

                await message.edit(embed=embed, view=None)

                del self.pages[ctx.author.id]
                del self.sides[ctx.author.id]

                return
