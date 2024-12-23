

# //made by @yxzhin with <3
# //#hellokittysupremacy #finelcomeback #yxzhinsave


import config.conf as config
from discord import Intents, Status, Activity, ActivityType
from discord.ext.commands import Bot, Context
from lib.error_handler import ErrorHandler
from lib.yaf_honeylib10 import getTime
from importlib import import_module


def main():

    bot = Bot(
        command_prefix=config.prefix,
        intents=Intents.all(),
        help_command=None,
    )

    @bot.event
    async def on_ready():

        __globals = dict()

        await bot.add_cog(ErrorHandler(bot))

        for command in config.commands:

            await bot.add_cog(import_module(
                f"commands.{command}").Command(bot))
            print(f"loaded command: {command}")

        await bot.change_presence(status=Status.online, activity=Activity(type=ActivityType.listening, name="вас, молодой человек."))

        print(f"{getTime()} started as {bot.user}")

    @bot.before_invoke
    async def __before_invoke(ctx: Context):

        print(
            f"{getTime()} {ctx.author} issued command: {ctx.message.content}")

    bot.run(config.token)


if __name__ == "__main__":

    main()
