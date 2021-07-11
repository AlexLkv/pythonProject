from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Дарова")
        ],
        [
            KeyboardButton(text="Задолбал"),
            KeyboardButton(text="АХМЕД"),
        ],
        [
            KeyboardButton(text="Вкусное сало.."),
            KeyboardButton(text="Смотреть маленькие девочки.."),
        ],
        [
            KeyboardButton(text="Пацан? ТЫкай")
        ],
        [
            KeyboardButton(text="СПЕЩЕЛ ФОР МИША")
        ],
        [
            KeyboardButton(text="Пака")
        ],
    ],
    resize_keyboard=True
)