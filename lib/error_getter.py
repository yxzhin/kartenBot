

# //made by @yxzhin with <3
# //#hellokittysupremacy #finelcomeback #yxzhinsave


from lib.yaf_honeylib10 import emb


# type: ignore
async def error_getter(ctx, errorid: int, setAuthor: int = None, args: list = [None]):

    title = {

        # structure | errorid: message

        -1: "Неизвестная ошибка (-1). Обратитесь к овнеру.",
        -2: "Эта команда недоступна в этом канале!",
        -3: "Истекло время на ответ. Используйте команду снова.",
        -4: "Нельзя использовать эти символы: {}".format(args[0]),
        -5: "Некорректная длина! Принимается {}".format(args[0]),
        -6: "Некорректный ответ!",
        -7: "Команда {} отключена!".format(args[0]),
        -8: "Команда {} не найдена!".format(args[0]),
        -9: "Эту команду нельзя использовать в ЛС!",
        -10: "Подождите еще {} сек прежде чем использовать эту команду снова!".format(args[0]),
        -11: "У вас отсутствует роль: {}!".format(args[0]),
        -12: "У вас отсутствуют права: {}!".format(args[0]),
        -13: "Пользователь не найден: {}!".format(args[0]),
        -14: "Аргумент не указан: {}!".format(args[0]),
        -15: "Эту команду можно использовать только овнеру!",
        -16: "Некорректный аргумент(ы)!",
        -17: "Вы уже используете эту команду!",

    }.get(errorid)

    embed = emb(
        ctx,
        f":x: **{title}**",
        setAuthor=True if setAuthor else False,
        discordID=setAuthor if setAuthor else None,  # type: ignore
    )

    if errorid == -1:

        embed.add_field(
            name="output:",
            value=args[0],
        )

    await ctx.reply(embed=embed)
