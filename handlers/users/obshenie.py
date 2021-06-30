from aiogram import types

from loader import dp


@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def bot_echo(message: types.Message):
    await message.answer(text="Вау прикольно! o_o")


@dp.message_handler(text="Ау")
async def bot_echo(message: types.Message):
    await message.answer(text="Кукареку")


@dp.message_handler(text="Ты кто?")
async def bot_echo(message: types.Message):
    await message.answer(text="Чудо, созданное Лёхой")


@dp.message_handler(text="Герасименко")
async def bot_echo(message: types.Message):
    await message.answer(text="ОПЯТЬ ТЫ? УХХХ!!!")


@dp.message_handler(text="Пельмеш")
async def bot_echo(message: types.Message):
    await message.answer(text="А? Что? Я тут!")


@dp.message_handler(text="Лох")
async def bot_echo(message: types.Message):
    await message.answer(text="Сам такой.. Сейчас обижусь!")


@dp.message_handler(text="Дебил")
async def bot_echo(message: types.Message):
    await message.answer(text="Сам такой.. Сейчас обижусь!")


@dp.message_handler(text="Ты лох")
async def bot_echo(message: types.Message):
    await message.answer(text="Сам такой.. Сейчас обижусь!")


@dp.message_handler(text="Ты дебил")
async def bot_echo(message: types.Message):
    await message.answer(text="Сам такой.. Сейчас обижусь!")


@dp.message_handler(text="Дурак")
async def bot_echo(message: types.Message):
    await message.answer(text="Сам такой.. Сейчас обижусь!")


@dp.message_handler(text="Ты дурак")
async def bot_echo(message: types.Message):
    await message.answer(text="Сам такой.. Сейчас обижусь!")
