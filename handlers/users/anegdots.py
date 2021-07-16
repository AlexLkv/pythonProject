import random

from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp, bot


@dp.message_handler(Command("anegdot"))
async def show_men(message: Message):
    await message.answer("-.-.-.-.-.-.-.-.-АНЕКДОТЫ-.-.-.-.-.-.-.-.- \n")
    a = random.randint(1, 10)
    if a == 1:
        await message.answer("Девушка в темном переулке перепутала баллончики и вылечила грабителя от насморка.")
    elif a == 2:
        await message.answer("Встречаются два друга: \n"
                             "— Привет, что делаешь? \n"
                             "— Да вот, несу разные вещи. \n"
                             "— Чем же они несуразные? \n"
                             "— Сам ты несуразный! Несу разные вещи! Разные! Вот, например, — несу мел! \n"
                             "— Что ты не сумел? \n")
    elif a == 3:
        await message.answer("Мужик приходит к окулисту: \n"
                             "— Доктор, у меня болит глаз. Что делать? \n"
                             "Окулист спокойно отвечает: \n"
                             "— Знаете что, любезный, у меня недавно болел зуб — так я его вырвал, и всех делов! \n")
    elif a == 4:
        await message.answer("Когда я надолго уезжаю, я совершенно не переживаю, что мой мужик приведет к нам домой "
                             "другую женщину. Ведь для того, чтобы кого-то пригласить, сначала нужно убраться.")
    elif a == 5:
        await message.answer('Времена такие, что название романа "Три товарища" лучше писать с цифрой.')
    elif a == 6:
        await message.answer(
            'Был у меня попугайчик. Все ласково называли его Попка. К сожалению, на днях он умер. Слипся.')
    elif a == 7:
        await message.answer('Изюминка — это твое лицо с утра.')
    elif a == 8:
        await message.answer('Говорят, что те москвичи, которые не сделали прививки, будут выселены в Россию.')
    elif a == 9:
        await message.answer("Мне психолог сказал. \n"
                             "– Напиши письмо человеку, который тебя бесит и сожги его. \n"
                             "А с письмом что делать? \n")
    elif a == 10:
        await message.answer("Ты зачем взял новый пакетик с чаем? \n"
                             "– У старого уже ниточка стёрлась. \n"
                             "А новую пришить, что рук нет? \n")

