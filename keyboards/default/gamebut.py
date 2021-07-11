from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

game = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Камень 🗿")
        ],
        [
            KeyboardButton(text="Ножницы ✂"),
            KeyboardButton(text="Бумага 📃"),
        ],
        [
            KeyboardButton(text="Закончить игру..")
        ],
    ],
    resize_keyboard=True
)
game1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Да"),
            KeyboardButton(text="Нет"),
        ],
    ],
    resize_keyboard=True
)
game2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="/game"),
        ],
    ],
    resize_keyboard=True
)