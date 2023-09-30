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
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Рассчитать проект 🧾", callback_data="расчёт")
    markup.add(item1)

    await message.answer("Здравствуйте  🖐\nЯ чат-бот компании ARTEX\nПомогу вам расщитать стоимость создания сайта 📝\nДля этого выберите нужную вам кнопку ⬇️", reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "расчёт")
async def process_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Рассчитать проект 🧾")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Создание сайтов 🗒", callback_data="создание_сайтов")
    item2 = types.InlineKeyboardButton("Реклама 📢", callback_data="реклама")
    item3 = types.InlineKeyboardButton("Продвижение 📈", callback_data="продвижение")
    item4 = types.InlineKeyboardButton("Получить консультацию 💬", callback_data="консультация")
    markup.add(item1, item2, item3, item4)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Какую задачу нужно решить ?📝",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "создание_сайтов")
async def process_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Создание сайтов 🗒")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Лендинг 📃", callback_data="лендинг")
    item2 = types.InlineKeyboardButton("Бизнес сайт 💼", callback_data="бизнес_сайт")
    item3 = types.InlineKeyboardButton("Интернет магазин 🛒", callback_data="интернет_магазин")
    markup.add(item1, item2)
    markup.add(item3)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Что вам нужно ? 📍",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "лендинг")
async def process_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Лендинг 📃")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Продажа товара 🤝", callback_data="продажа_товара")
    item2 = types.InlineKeyboardButton("Сбор лидов 📊", callback_data="сбор_лидов", url='https://andreykirillov.art/kontakty/')
    item3 = types.InlineKeyboardButton("Приглашение на событие 🎟", callback_data="приглашение_на_событие", url='https://andreykirillov.art/kontakty/')
    item4 = types.InlineKeyboardButton("Другое... 📦", callback_data="другое", url='https://andreykirillov.art/kontakty/')
    markup.add(item1, item2, item3, item4)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Выберите специфику ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "продажа_товара")
async def process_button4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Продажа товара 🤝")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас  уже есть дизайн, макет,  изображения и текст ? 📝",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет")
async def process_button5(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет ❌")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Заказать дизайн 🎨", callback_data="заказать_дизайн", url='https://andreykirillov.art/kontakty/')
    item2 = types.InlineKeyboardButton("Заказать коперайтинг 💻", callback_data="заказать_коперайт", url='https://andreykirillov.art/kontakty/')
    item3 = types.InlineKeyboardButton("Получить консультацию 👨🏻‍💻", callback_data="продвижение", url='https://andreykirillov.art/kontakty/')
    markup.add(item1, item2)
    markup.add(item3)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Если у вас нету дизайна, макета, текста или изображени  вы можете заказать сдесь  ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "бизнес_сайт")
async def process_button6(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Бизнес сайт 💼")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Продажа товаров 🤝", callback_data="ПродажаТоваров")
    item2 = types.InlineKeyboardButton("Сбор лидов 📊", callback_data="сбор_лидов", url='https://andreykirillov.art/kontakty/')
    item3 = types.InlineKeyboardButton("Другое... 📦", callback_data="другое_2", url='https://andreykirillov.art/kontakty/')
    markup.add(item1, item2, item3)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Выберите специфику ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "ПродажаТоваров")
async def process_button7(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Продажа товаров 🤝")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_2")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_2")
    markup.add(item1, item2)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас уже есть дизайн, макет,  изображения и текст ? 📝",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_2")
async def process_button8(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет ❌")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Заказать дизайн 🎨", callback_data="заказать_дизайн_2", url='https://andreykirillov.art/kontakty/')
    item2 = types.InlineKeyboardButton("Заказать коперайтинг 💻", callback_data="Заказать_коперайтинг_2", url='https://andreykirillov.art/kontakty/')
    item3 = types.InlineKeyboardButton("Получить консультацию 👨🏻‍💻", callback_data="Получить_консультацию_2", url='https://andreykirillov.art/kontakty/')
    markup.add(item1, item2)
    markup.add(item3)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Если у вас нету дизайна, макета, текста или изображени  вы можете заказать сдесь  ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_2")
async def process_button9(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да ✅")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Связаться 💬", callback_data="связь_1", url='https://andreykirillov.art/kontakty/')
    markup.add(item1)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Хорошо 👍\nВаш бизнес сайт будет стоить от 8 000₽ 💵\nДля дальнейшего обсуждения дальнейшего заказа напишите нам ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да")
async def process_button10(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да ✅")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Связаться 💬", callback_data="связь_2", url='https://andreykirillov.art/kontakty/')
    markup.add(item1)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Хорошо 👍\nВаш лендинг будет стоить от 6 000₽ 💵\nДля дальнейшего обсуждения заказа напишите нам ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_5")
async def process_button10(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да ✅")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Связаться 💬", callback_data="связь_2", url='https://andreykirillov.art/kontakty/')
    markup.add(item1)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Хорошо 👍\nВаш интернет магазин будет стоить от 8 000₽ 💵\nДля дальнейшего обсуждения заказа напишите нам ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "реклама")
async def process_button11(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Реклама  📢")
    markup = types.InlineKeyboardMarkup(row_width=4)
    item1 = types.InlineKeyboardButton("Услуги 📋", callback_data="услуги", url='https://andreykirillov.art/kontakty/')
    item2 = types.InlineKeyboardButton("Товары 🛒", callback_data="товары", url='https://andreykirillov.art/kontakty/')
    item3 = types.InlineKeyboardButton("Мероприятие 🎟", callback_data="мероприятие", url='https://andreykirillov.art/kontakty/')
    item4 = types.InlineKeyboardButton("Другое... 📦", callback_data="другое_3", url='https://andreykirillov.art/kontakty/')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Что вы хотите рекламировать ? 🖼\nПосле выбора кнопки, вы будете перенаправлены на сайт",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "продвижение")
async def process_button12(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Продвижение 📈")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_3")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_3")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Проводились ли на вашем сайте работы\nПо SEO оптимизации ? 🔝",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_3")
async def process_button13(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да ✅")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_4")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_4")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Проводите ли вы мониторинг позиций Вашего сайта в поисковых системах ? 👨🏻‍💻",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_4")
async def process_button14(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да ✅")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Заказать 📩", callback_data="заказать", url='https://andreykirillov.art/kontakty/')
    markup.add(item1)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Для более детального обсуждения закажите бесплатную констультацию ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_4")
async def process_button15(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет ❌")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Заказать 📩", callback_data="заказать_2", url='https://andreykirillov.art/kontakty/')
    markup.add(item1)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Для более детального обсуждения закажите бесплатную констультацию ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_3")
async def process_button16(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет ❌")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_4")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_4")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Проводите ли вы мониторинг позиций Вашего сайта в поисковых системах ? 👨🏻‍💻",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "консультация")
async def process_button17(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Консультация 💬")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Получить консультацию 💬", callback_data="получить_консультацию", url='https://andreykirillov.art/kontakty/')
    markup.add(item1)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Полную консультацию вы можете получить\nНажав на кнопку ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "да_4")
async def process_button18(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Да ✅")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Заказать 📩", callback_data="заказать", url='https://andreykirillov.art/kontakty/')
    markup.add(item1)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Для борлее детального обсуждения закажите бесплатную констультацию ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "интернет_магазин")
async def process_button19(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Интернет Магазин 🛒")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_5")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_5")
    markup.add(item1, item2)

    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="У вас уже есть дизайн, макет,  изображения и текст ? 📝",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_5")
async def process_button20(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет ❌")
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Заказать дизайн 🎨", callback_data="заказать_дизайн_3", url='https://andreykirillov.art/kontakty/')
    item2 = types.InlineKeyboardButton("Заказать коперайтинг 💻", callback_data="Заказать_коперайтинг_3", url='https://andreykirillov.art/kontakty/')
    item3 = types.InlineKeyboardButton("Получить консультацию 👨🏻‍💻", callback_data="Получить_консультацию_3", url='https://andreykirillov.art/kontakty/')
    markup.add(item1, item2)
    markup.add(item3)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Если у вас нету дизайна, макета, текста или изображени  вы можете заказать сдесь  ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_4")
async def process_button21(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет ❌")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Заказать 📩", callback_data="заказать_2", url='https://andreykirillov.art/kontakty/')
    markup.add(item1)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Для более детального обсуждения закажите бесплатную констультацию ⬇️",
                           reply_markup=markup)


@dp.callback_query_handler(lambda c: c.data == "нет_3")
async def process_button22(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, text="Нет ❌")
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("Да ✅", callback_data="да_4")
    item2 = types.InlineKeyboardButton("Нет ❌", callback_data="нет_4")
    markup.add(item1, item2)
    await bot.send_message(chat_id=callback_query.message.chat.id,
                           text="Проводите ли вы мониторинг позиций Вашего сайта в поисковых системах ? 👨🏻‍💻",
                           reply_markup=markup)


if __name__ == '__main__':
    from aiogram import executor
    loop = asyncio.get_event_loop()
    executor.start_polling(dp, loop=loop, skip_updates=True)
