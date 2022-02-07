import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import time
import os
from main import collect_data
from aiogram.utils.markdown import hbold, hlink


TOKEN = "your_telegram_token" # You can get it from telegram bot
bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    start_buttons = ['🔪 Knives', '🧤 Gloves', '🔫 Sniper rifles']
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)

    await message.answer('Choose a category', reply_markup=keyboard)


@dp.message_handler(Text(equals='🔪 Knives'))
async def get_knives(message: types.Message):
    await message.answer('Please waiting...')
    collect_data(cat_type=2)
    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Discount: ")}{item.get("overprice")}%\n' \
               f'{hbold("Price: ")}{item.get("item_price")}🔥'

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)



@dp.message_handler(Text(equals='🧤 Gloves'))
async def get_gloves(message: types.Message):
    await message.answer('Please waiting...')
    collect_data(cat_type=13)
    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Discount: ")}{item.get("overprice")}%\n' \
               f'{hbold("Price: ")}{item.get("item_price")}🔥'

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)


@dp.message_handler(Text(equals='🔫 Sniper rifles'))
async def get_guns(message: types.Message):
    await message.answer('Please waiting...')
    collect_data(cat_type=4)
    with open('result.json') as file:
        data = json.load(file)

    for index, item in enumerate(data):
        card = f'{hlink(item.get("full_name"), item.get("3d"))}\n' \
               f'{hbold("Discount: ")}{item.get("overprice")}%\n' \
               f'{hbold("Price: ")}{item.get("item_price")}🔥'

        if index % 20 == 0:
            time.sleep(3)

        await message.answer(card)


def main():
    executor.start_polling(dp)


if __name__ == '__main__':
    main()



