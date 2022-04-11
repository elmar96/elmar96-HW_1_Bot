from aiogram import types, Dispatcher
from aiogram.types import ParseMode, InlineKeyboardMarkup, InlineKeyboardButton

from config import bot


async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello {message.from_user.full_name}")


async def help(message: types.Message):
    await message.reply("что бы запустить викторину введите команду /quiz")



async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_1")
    markup.add(button_call_1)
    question = "Как перевести первый символ строки в верхний регистр"
    answers = ["update",
               "extend",
               "upper",
               "capitalize",

               ]

    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="Для этого есть метод capitalize",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,

    )


def register_handlars_clien(dp: Dispatcher):
    dp.register_message_handler(hello, commands=['start'])
    dp.register_message_handler(help, commands=['help'])
    dp.register_message_handler(quiz_1,commands=['quiz'])