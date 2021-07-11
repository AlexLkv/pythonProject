from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Помощь"),
        types.BotCommand("game", "Игра"),
        types.BotCommand("test", "Тестик"),
        types.BotCommand("anegdot", "Анегдотики от юморного :D"),
        types.BotCommand("menu", "Неведомое говно 0_о"),
    ])
