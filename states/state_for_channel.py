from aiogram.dispatcher.filters.state import StatesGroup, State


class Channel(StatesGroup):
    s1 = State()


class Get(StatesGroup):
    EnterMedia = State()
    EnterText = State()
    Confirm = State()
    Done = State()


class Get1(StatesGroup):
    EnterMedia = State()
    EnterText = State()
    Confirm = State()
    Mem = State()
    Done = State()
