from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, 'help')
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = [
        'Список команд: ',
        '/start - Начать диалог',
        '/help - Получить справку',
        '/game - Сыграй в прикольную игру',
        '/test - Пройди тестик и узнай кто ты на самом деле..',
        '/anegdot - Зацени анекдоты :D',
        '/menu - Сам хз, что это. Чисто для обучения..'
        '\n',
        'Если ты мне что-то напишешь, а я этого не знаю, то я просто повторю это.',
        '\n',
        'Ты можешь спросить меня:',
        '"Ты кто?",',
        '"Ау",',
        '"Герасименко",',
        '"Пельмеш",',
        '\n',
        'Скинь мне любую фотку, а я отвечу :D',
        '\n',
        'ps: Не оскарбляй меня..'

    ]
    await message.answer('\n'.join(text))
