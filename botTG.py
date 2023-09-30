import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware

logging.basicConfig(level=logging.INFO)

API_TOKEN = '6657590037:AAH4nYyRYskgnUUR8phgtobMMAQ38lPCxCY'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Рассчитать проект 🧾", callback_data="расчёт")
    markup.add(item1)

    await message.answer("Здравствуйте  🖐\nЯ чат-бот компании ARTEX\nПомогу вам расщитать стоимость создания сайта 📝\nДля этого выберите нужную вам кнопку ⬇️", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "расчёт")
async def process_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Рассчитать проект ")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Многостраничник 🗒", callback_data="сайтмногостраничник")
    item2 = types.InlineKeyboardButton("Интернет магазин 🛒", callback_data="интернетмагазин")
    item3 = types.InlineKeyboardButton("Лендинг 📃", callback_data="лендинг")
    item4 = types.InlineKeyboardButton("Сайт-визитка 📄", callback_data="сайт-визитка")
    item5 = types.InlineKeyboardButton("Пока не опредилися(-ась) 🤔", callback_data="поканеопредилися(-ась)")
    markup.add(item1, item2)
    markup.add(item3, item4)
    markup.add(item5)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Выберите нужный тип сайта 📝",
                           reply_markup=markup)

#Начало МНОГОСТРАНИЧНИК -------------------------------------------------------------------------------------


@dp.callback_query_handler(lambda c: c.data == "сайтмногостраничник")
async def process_button21(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Сайт многостраничник")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Юридические услуги ⚖️", callback_data="юридическиеуслуги")
    item2 = types.InlineKeyboardButton("Строительные услуги 🧱", callback_data="строительныеуслуги")
    item3 = types.InlineKeyboardButton("Спецтехника ⚙️", callback_data="спецтехника")
    item4 = types.InlineKeyboardButton("Туризм и отдых ✈️", callback_data="туризмиотдых")
    item5 = types.InlineKeyboardButton("Изготовление мебели 🛠", callback_data="изготовлениемебели")
    item6 = types.InlineKeyboardButton("Другое... 📦", callback_data="Другое")
    markup.add(item1, item2)
    markup.add(item3, item4)
    markup.add(item5, item6)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Выберите вид вашей деятельности : ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "юридическиеуслуги")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Юридические услуги")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_1")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_1")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_1")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_1")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_1")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "строительныеуслуги")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Строительные услуги")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_2")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_2")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_1")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_2")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_2")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_2")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_3")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_3")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_2")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_4")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_4")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "спецтехника")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Спецтехника")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_3")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_3")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_3")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_5")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_5")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_3")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_6")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_6")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "туризмиотдых")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Туризм и отдых")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_4")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_4")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_4")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_7")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_7")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_4")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_8")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_8")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "изготовлениемебели")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Изготовление мебели")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_5")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_5")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_5")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_9")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_9")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_5")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_10")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_10")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "Другое")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Другое...")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_6")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_6")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_6")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_11")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_11")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_6")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_12")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_12")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)

#Начало ЛЕНДИНГ -------------------------------------------------------------------------------------


@dp.callback_query_handler(lambda c: c.data == "лендинг")
async def process_button21(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Лендинг")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Юридические услуги ⚖️", callback_data="юридическиеуслуги_1")
    item2 = types.InlineKeyboardButton("Строительные услуги 🧱", callback_data="строительныеуслуги_1")
    item3 = types.InlineKeyboardButton("Спецтехника ⚙️", callback_data="спецтехника_1")
    item4 = types.InlineKeyboardButton("Туризм и отдых ✈️", callback_data="туризмиотдых_1")
    item5 = types.InlineKeyboardButton("Изготовление мебели 🛠", callback_data="изготовлениемебели_1")
    item6 = types.InlineKeyboardButton("Другое... 📦", callback_data="Другое_1")
    markup.add(item1, item2)
    markup.add(item3, item4)
    markup.add(item5, item6)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Выберите вид вашей деятельности : ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "юридическиеуслуги_1")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Юридические услуги")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_7")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_7")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_7")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_13")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_13")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "строительныеуслуги_1")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Строительные услуги")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_8")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_8")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_7")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_13")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_13")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_8")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_14")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_14")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_8")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_15")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_15")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "спецтехника_1")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Спецтехника")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_9")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_9")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_9")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_16")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_16")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_9")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_17")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_17")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "туризмиотдых_1")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Туризм и отдых")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_10")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_10")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_10")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_18")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_18")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_10")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_19")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_19")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "изготовлениемебели_1")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Изготовление мебели")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_11")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_11")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_11")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_20")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_20")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_11")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_21")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_21")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "Другое_1")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Другое...")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_12")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_12")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_12")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_22")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_22")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_12")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_23")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_23")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)

#Начало ПОКАНЕОПРЕДЕЛИЛСЯ -------------------------------------------------------------------------------------

@dp.callback_query_handler(lambda c: c.data == "поканеопредилися(-ась)")
async def process_button21(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Пока не опредилися(-ась)")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Юридические услуги ⚖️", callback_data="юридическиеуслуги_2")
    item2 = types.InlineKeyboardButton("Строительные услуги 🧱", callback_data="строительныеуслуги_2")
    item3 = types.InlineKeyboardButton("Спецтехника ⚙️", callback_data="спецтехника_2")
    item4 = types.InlineKeyboardButton("Туризм и отдых ✈️", callback_data="туризмиотдых_2")
    item5 = types.InlineKeyboardButton("Изготовление мебели 🛠", callback_data="изготовлениемебели_2")
    item6 = types.InlineKeyboardButton("Другое... 📦", callback_data="Другое_2")
    markup.add(item1, item2)
    markup.add(item3, item4)
    markup.add(item5, item6)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Выберите вид вашей деятельности : ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "юридическиеуслуги_2")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Юридические услуги")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_13")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_13")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_13")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_24")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_24")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "строительныеуслуги_2")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Строительные услуги")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_14")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_14")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_13")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_25")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_25")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_14")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_26")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_26")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_14")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_27")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_27")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "спецтехника_2")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Спецтехника")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_15")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_15")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_15")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_28")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_28")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_15")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_29")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_29")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "туризмиотдых_2")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Туризм и отдых")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_16")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_16")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_16")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_30")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_30")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_16")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_31")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_31")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "изготовлениемебели_2")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Изготовление мебели")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_17")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_17")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_17")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_32")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_32")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_17")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_33")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_33")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "другое_2")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Другое...")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_18")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_18")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас есть наполнение для для вашего сайта ? 📃",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_18")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_34")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_34")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_18")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Требуется услуга по размещению 👥", callback_data="требуетсяуслугапоразмещению_35")
    item2 = types.InlineKeyboardButton("Самостоятельно 👤", callback_data="самостоятельно_35")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Размещение информации на вашем сайте : ℹ️",
                            reply_markup=markup)

#Начало ИНТЕРНЕТМАГАЗИН -------------------------------------------------------------------------------------


@dp.callback_query_handler(lambda c: c.data == "интернетмагазин")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Интернет магазин")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Готовую еду 🍜", callback_data="готоваяеда")
    item2 = types.InlineKeyboardButton("Электронику 💻", callback_data="Электроника")
    item3 = types.InlineKeyboardButton("Автоаксессуары 🚘", callback_data="автоаксессуары")
    item4 = types.InlineKeyboardButton("Одежду и обувь 👕", callback_data="Одеждаиобувь")
    item5 = types.InlineKeyboardButton("Парфюмерию и косметику 🏻", callback_data="Парфюмерияикосметика")
    item6 = types.InlineKeyboardButton("Другое... 📦", callback_data="другое_987")
    markup.add(item1, item2)
    markup.add(item3, item4)
    markup.add(item5, item6)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Вы продаёте : 🤔",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "готоваяеда")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Готовую еду")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Менее 100", callback_data="менее100")
    item2 = types.InlineKeyboardButton("До 5000", callback_data="до5000")
    item3 = types.InlineKeyboardButton("До 45000", callback_data="до5000")
    item4 = types.InlineKeyboardButton("Другое...", callback_data="другое_133")
    markup.add(item1, item2)
    markup.add(item3, item4)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Количество ваших товаров :",
                            reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "менее100")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Готовая еда")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Настроен приём любых видов платежей через сайт", callback_data="сокр_1")
    item2 = types.InlineKeyboardButton("Подключен выбор сервисов доставки или самовывоза", callback_data="сокр_2")
    item3 = types.InlineKeyboardButton("Интеграция в маркетплейсы", callback_data="сокр_3")
    item4 = types.InlineKeyboardButton("1С и «Мой склад»", callback_data="сокр_4")
    item5 = types.InlineKeyboardButton("Пока не определился(-ась)", callback_data="сокр_5")
    markup.add(item1, item2)
    markup.add(item3, item4)
    markup.add(item5)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                            text="Для вас настроены и нужно подключить :",
                            reply_markup=markup)


if __name__ == '__main__':
    from aiogram import executor
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True)
