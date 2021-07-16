from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Command

from states import Test


@dp.message_handler(Command("test"))
async def enter_test(message: types.Message):
    await message.answer("Вы начали тестик. \n"
                         "Вопрос 1.. \n \n"
                         "Вы пельмеш?? \n"
                         "Да / Нет")


    await Test.q1.set()


# await Test.first()

@dp.message_handler(state=Test.q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text

    # await state.update_data(answer1=answer)
    async with state.proxy() as data:
        data["answer1"] = answer
    await message.answer("Вопрос 2.. \n \n"
                         "Вы любите пельмени?? \n"
                         "Да / Нет")
    await Test.next()

    # await Test.q2.set()
    @dp.message_handler(state=Test.q2)
    async def answer_q1(message: types.Message, state: FSMContext):
        data = await state.get_data()
        answer1 = data.get("answer1")
        answer2 = message.text
        if answer1 == "Да" and answer2 == "Да" or answer1 == "да" and answer2 == "да":
            await message.answer("Спасибо за ваши ответы)")
            await message.answer(f"Ответ 1: {answer1}")
            await message.answer(f"Ответ 2: {answer2}")
            await message.answer("Поздравляю! Вы, канибал Валерий..")
        elif answer1 == "Нет" and answer2 == "Да" or answer1 == "нет" and answer2 == "да":
            await message.answer("Спасибо за ваши ответы)")
            await message.answer(f"Ответ 1: {answer1}")
            await message.answer(f"Ответ 2: {answer2}")
            await message.answer("Поздравляю! Вы, человек разумный, а проще говоря Алёша")
        elif answer1 == "Нет" and answer2 == "Нет" or answer1 == "нет" and answer2 == "нет":
            await message.answer("Спасибо за ваши ответы)")
            await message.answer(f"Ответ 1: {answer1}")
            await message.answer(f"Ответ 2: {answer2}")
            await message.answer("Поздравляю! Вы, человек странный, а проще говоря ДЕБИЛ МАЛОЛЕТНИЙ")
        elif answer1 == "Да" and answer2 == "Нет" or answer1 == "да" and answer2 == "нет":
            await message.answer("Спасибо за ваши ответы)")
            await message.answer(f"Ответ 1: {answer1}")
            await message.answer(f"Ответ 2: {answer2}")
            await message.answer("Поздравляю! Вы, пельмеш обыкновеннный")
        else:
            await message.answer("Спасибо за ваши ответы)")
            await message.answer(f"Ответ 1: {answer1}")
            await message.answer(f"Ответ 2: {answer2}")
            await message.answer("Отвечай пожалуйста правильно!")
        await state.reset_state()  # await state.reset_state(with data=False) - без очистки даты
