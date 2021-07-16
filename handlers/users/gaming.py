from aiogram.dispatcher import FSMContext

from aiogram.types import ReplyKeyboardRemove
import random
from keyboards.default import game
from keyboards.default.gamebut import game1, game2
from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command

from states import Game


@dp.message_handler(Command("game"))
async def enter_test(message: types.Message):
    await message.answer("-.-.-.-.-.-.-.-.-ИГРА-.-.-.-.-.-.-.-.- \n"
                         "Камень/ножницы\бумага \n \n"
                         "Делайте свой выбор..", reply_markup=game)
    await Game.q1.set()


@dp.message_handler(state=Game.q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    bot = ""
    comp = str(random.randint(1, 3))  # 1 - Камень, 2 - Ножницы, 3 - Бумага
    if comp == "1":
        bot = "Камень 🗿"
    elif comp == "2":
        bot = "Ножницы ✂️"
    elif comp == "3":
        bot = "Бумагу 📃"
    if answer == "Закончить игру..":
        await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
        await state.reset_state()
    elif answer == "Камень 🗿" and comp == "1":
        await message.answer(f"Пельмеш выбрал - {bot} \n \n"
                             "-=-=-=-=-=- Ничья! :/ -=-=-=-=-=- \n \n")
        await message.answer("Сыграем еще раз?", reply_markup=game1)
        await Game.next()

        @dp.message_handler(state=Game.q2)
        async def answer_q1(message: types.Message, state: FSMContext):
            if message.text == "Нет":
                await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
                await state.reset_state()
            else:
                await state.reset_state()
                await message.answer("Окей", reply_markup=game2)
    elif answer == "Камень 🗿" and comp == "2":
        await message.answer(f"Пельмеш выбрал - {bot} \n \n"
                             "-=-=-=-=-=- Вы выиграли! :D -=-=-=-=-=-")
        await message.answer("Сыграем еще раз?", reply_markup=game1)
        await Game.next()

        @dp.message_handler(state=Game.q2)
        async def answer_q1(message: types.Message, state: FSMContext):
            if message.text == "Нет":
                await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
                await state.reset_state()
            else:
                await state.reset_state()
                await message.answer("Окей", reply_markup=game2)
    elif answer == "Камень 🗿" and comp == "3":
        await message.answer(f"Пельмеш выбрал - {bot} \n \n"
                             "-=-=-=-=-=- Проигрыш :( -=-=-=-=-=-")
        await message.answer("Сыграем еще раз?", reply_markup=game1)
        await Game.next()

        @dp.message_handler(state=Game.q2)
        async def answer_q1(message: types.Message, state: FSMContext):
            if message.text == "Нет":
                await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
                await state.reset_state()
            else:
                await state.reset_state()
                await message.answer("Окей", reply_markup=game2)
    elif answer == "Ножницы ✂" and comp == "1":
        await message.answer(f"Пельмеш выбрал - {bot} \n \n"
                             "-=-=-=-=-=- Проигрыш :( -=-=-=-=-=-")
        await message.answer("Сыграем еще раз?", reply_markup=game1)
        await Game.next()

        @dp.message_handler(state=Game.q2)
        async def answer_q1(message: types.Message, state: FSMContext):
            if message.text == "Нет":
                await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
                await state.reset_state()
            else:
                await state.reset_state()
                await message.answer("Окей", reply_markup=game2)
    elif answer == "Ножницы ✂" and comp == "2":
        await message.answer(f"Пельмеш выбрал - {bot} \n \n"
                             "-=-=-=-=-=- Ничья! :/ -=-=-=-=-=- \n \n")
        await message.answer("Сыграем еще раз?", reply_markup=game1)
        await Game.next()

        @dp.message_handler(state=Game.q2)
        async def answer_q1(message: types.Message, state: FSMContext):
            if message.text == "Нет":
                await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
                await state.reset_state()
            else:
                await state.reset_state()
                await message.answer("Окей", reply_markup=game2)
    elif answer == "Ножницы ✂" and comp == "3":
        await message.answer(f"Пельмеш выбрал - {bot} \n \n"
                             "-=-=-=-=-=- Вы выиграли! :D -=-=-=-=-=-")
        await message.answer("Сыграем еще раз?", reply_markup=game1)
        await Game.next()

        @dp.message_handler(state=Game.q2)
        async def answer_q1(message: types.Message, state: FSMContext):
            if message.text == "Нет":
                await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
                await state.reset_state()
            else:
                await state.reset_state()
                await message.answer("Окей", reply_markup=game2)
    elif answer == "Бумага 📃" and comp == "1":
        await message.answer(f"Пельмеш выбрал - {bot} \n \n"
                             "-=-=-=-=-=- Вы выиграли! :D -=-=-=-=-=-")
        await message.answer("Сыграем еще раз?", reply_markup=game1)
        await Game.next()

        @dp.message_handler(state=Game.q2)
        async def answer_q1(message: types.Message, state: FSMContext):
            if message.text == "Нет":
                await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
                await state.reset_state()
            else:
                await state.reset_state()
                await message.answer("Окей", reply_markup=game2)
    elif answer == "Бумага 📃" and comp == "2":
        await message.answer(f"Пельмеш выбрал - {bot} \n \n"
                             "-=-=-=-=-=- Проигрыш :( -=-=-=-=-=-")
        await message.answer("Сыграем еще раз?", reply_markup=game1)
        await Game.next()

        @dp.message_handler(state=Game.q2)
        async def answer_q1(message: types.Message, state: FSMContext):
            if message.text == "Нет":
                await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
                await state.reset_state()
            else:
                await state.reset_state()
                await message.answer("Окей", reply_markup=game2)
    elif answer == "Бумага 📃" and comp == "3":
        await message.answer(f"Пельмеш выбрал - {bot} \n \n"
                             "-=-=-=-=-=- Ничья! :/ -=-=-=-=-=- \n \n")
        await message.answer("Сыграем еще раз?", reply_markup=game1)
        await Game.next()

        @dp.message_handler(state=Game.q2)
        async def answer_q1(message: types.Message, state: FSMContext):
            if message.text == "Нет":
                await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
                await state.reset_state()
            else:
                await state.reset_state()
                await message.answer("Окей", reply_markup=game2)
    else:
        await message.answer("Жду правильного ответа!!")

# await message.answer("By, by.. Ждем тебя снова)", reply_markup=ReplyKeyboardRemove())
# await state.reset_state()  # await state.reset_state(with data=False) - без очистки даты
