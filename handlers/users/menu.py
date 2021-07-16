from aiogram import types
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.default import menu
from loader import dp, bot


# ==========================================================================================================
# ДАННЫЙ РАЗДЕЛ НЕ НЕСЁТ НИКАКОЙ СМЫСЛОВОЙ НАГРУЗКИ. ПРОПИСАННО ИСКЛЮЧИТЕЛЬНО ДЛЯ ДРУЗЕЙ И В КАЧЕСТВЕ ОБУЧЕНИЯ
# ==========================================================================================================
@dp.message_handler(Command("menu"))
async def show_men(message: Message):
    video_url = "https://www.online-convert.com/ru/downloadfile/7b23b287-9574-4757-bbc4-64e13f375288/338eaa19-63a1-4823-809c-c1378d673e1d"
    await bot.send_voice(chat_id=message.from_user.id,
                         voice=video_url)
    await message.answer("Дарова, задолбал", reply_markup=menu)


@dp.message_handler(text="АХМЕД")
async def darov(message: types.Message):
    video_ur = "https://www.online-convert.com/ru/downloadfile/eb6bc3af-04dd-4a73-a4f4-96454ea5e89b/6e87588f-dffb-4b8e-8420-ff3d14c42f95"
    await bot.send_voice(chat_id=message.from_user.id,
                         voice=video_ur,
                         caption="РАЗБУДИЛ ГАДИНА")


@dp.message_handler(Text(equals=["Вкусное сало.."]))
async def dar(message: types.Message):
    video_u = "https://www.online-convert.com/ru/downloadfile/67c8ee3f-9047-469d-bc44-5de23cce9585/d9710ad2-77fd-4bc7-93fc-ac2f1a702336"
    video = "https://www.online-convert.com/ru/downloadfile/89eca44d-bb43-4add-89aa-844f79f1d023/d18197da-80ef-42dc-bea5-e6c79736a8a6"
    await bot.send_voice(chat_id=message.from_user.id,
                         voice=video_u,
                         caption="МОЭ САЛО")
    await bot.send_voice(chat_id=message.from_user.id,
                         voice=video,
                         caption="Тем временем я....")


@dp.message_handler(Text(equals=["Задолбал"]))
async def dar(message: types.Message):
    video_ = "https://www.online-convert.com/ru/downloadfile/ae83f5c1-d98c-42ac-9ecc-8a8f984d87ad/5a79032b-d63b-4457-ae59-f62f70d33cac"
    await bot.send_voice(chat_id=message.from_user.id,
                         voice=video_,
                         caption=".....")


@dp.message_handler(Text(equals=["Смотреть маленькие девочки.."]))
async def dar(message: types.Message):
    vide = "https://www.online-convert.com/ru/downloadfile/7a6d6ead-bd76-44d0-8200-097c86595db1/8df618f2-f723-4cab-a792-cda5db63bb59"
    await bot.send_voice(chat_id=message.from_user.id,
                         voice=vide,
                         caption="ДОИГРАЛСЯ?????")


@dp.message_handler(Text(equals=["Пацан? ТЫкай"]))
async def dar(message: types.Message):
    vid = "https://www.online-convert.com/ru/downloadfile/17e47566-9f3c-45ea-b5e9-9a9f412dce41/5a46119d-cbe4-469f-8f77-f6fa388c61e8"
    await bot.send_voice(chat_id=message.from_user.id,
                         voice=vid,
                         caption="Красафффчик")


@dp.message_handler(Text(equals=["Пака"]))
async def dar(message: types.Message):
    vi = "https://www.online-convert.com/ru/downloadfile/a6c0cd43-b562-4251-9ed0-4dc4187607dc/4453df9d-509b-492a-8e38-7290bb51d42a"
    await bot.send_voice(chat_id=message.from_user.id,
                         voice=vi)
    await message.answer("До новый встреч..", reply_markup=ReplyKeyboardRemove())


@dp.message_handler(Text(equals=["СПЕЩЕЛ ФОР МИША"]))
async def dar(message: types.Message):
    v = "https://www.online-convert.com/ru/downloadfile/cf966086-29c0-4101-b53e-bfae95d3e2dd/86d1f529-08c5-493e-8ea5-1f7399ac171b"
    await bot.send_voice(chat_id=message.from_user.id,
                         voice=v)


@dp.message_handler(Text(equals=["Дарова"]))
async def dar(message: types.Message):
    va = "https://www.online-convert.com/ru/downloadfile/a619b35c-bd03-440e-9242-17bc07509980/419c2857-dc33-4c11-bdb1-1994b9bed5fb"
    await bot.send_voice(chat_id=message.from_user.id,
                         voice=va)
