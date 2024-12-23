

import traceback
import sys
from lib.yaf_honeylib10 import getTime
from discord.ext import commands
from discord.ext.commands import Context
from lib.error_getter import error_getter


class ErrorHandler(commands.Cog):

    def __init__(self, bot):

        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: Context, error):

        errors = {

            commands.errors.DisabledCommand: (-7, ctx.command),
            commands.errors.CommandNotFound: (-8, ctx.message.content),
            commands.errors.NoPrivateMessage: -9,
            commands.errors.CommandOnCooldown: (-10, error.retry_after if isinstance(error, commands.errors.CommandOnCooldown) else None),
            commands.errors.MissingRole: (-11, error.missing_role if isinstance(error, commands.errors.MissingRole) else None),
            commands.errors.MissingPermissions: (-12, error.missing_permissions if isinstance(error, commands.errors.MissingPermissions) else None),
            commands.errors.MemberNotFound: (-13, error.argument if isinstance(error, commands.errors.MemberNotFound) else None),
            commands.errors.MissingRequiredArgument: (-14, error.param if isinstance(error, commands.errors.MissingRequiredArgument) else None),
            commands.errors.NotOwner: -15,
            commands.errors.BadArgument: -16,

        }

        error_ = errors.get(type(error))

        if error_:

            error_code, args = error_, []

            error_code = error_[0] if isinstance(error_, tuple) else error_
            args = [error_[1]] if isinstance(error_, tuple) else []

            await error_getter(ctx, error_code, args=args)
            return

        print(
            f'[{getTime()}] Ignoring exception in command {ctx.command}:', file=sys.stderr)

        traceback.print_exception(
            type(error), error, error.__traceback__, file=sys.stderr)

        await error_getter(ctx, -1)
