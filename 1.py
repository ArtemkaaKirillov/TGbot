import botTG
import logging
import requests
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)
storage=MemoryStorage()

API_TOKEN = '5609936286:AAG99bT1AvkD7ULwSYdmgzAYoZONFZGEWAM'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot,storage=storage)
dp.middleware.setup(LoggingMiddleware())

class ProfStateGroup(StatesGroup):
    user = State()

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer("Напишите имя, телефон, почту через запятую: ")
    await ProfStateGroup.user.set()

@dp.message_handler(state=ProfStateGroup.user)
async def start(message: types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['user'] = message.text
    print(data['user'].split(','))


