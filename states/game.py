from aiogram.dispatcher.filters.state import StatesGroup, State


class Game(StatesGroup):
    q1 = State()
    q2 = State()

