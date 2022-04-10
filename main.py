from aiogram import types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from config import bot, dp


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id,
                           f"Hello {message.from_user.full_name}")


@dp.message_handler(commands=['help'])
async def help(message: types.Message):
    await message.reply("что бы запустить викторину введитекоманду /quiz")


@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quize_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Следующая Викторина",
                                         callback_data="button_call_2")
    markup.add(button_call_2)
    question = "Найдите конструктор класса"
    answers = ["__def__",
               "__class__",
               "__init__",
               "self",
               "init",
               ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Для этого есть метод capitalize",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=markup,
    )


@dp.callback_query_handler(lambda call: call.data == "button_call_2")
async def quize_3(call: types.CallbackQuery):
    # markup = InlineKeyboardMarkup()
    # button_call_3 = InlineKeyboardButton("Следующая Викторина",
    #                                      callback_data="button_call_3")
    # markup.add(button_call_3)
    question = "какой из вариантов принтует " \
               "вывод указанный выше действий:"
    answers = [
        "1",
        "2",
        "3",
        "Все варианты",
    ]

    photo = open("media/task_image2.jpg", "rb")
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="This is too easy for explanation",
        explanation_parse_mode=ParseMode.MARKDOWN_V2,
        # reply_markup=markup,
    )


# @dp.callback_query_handler(lambda call: call.data == "button_call_3")
# async def quiz_4(call: types.CallbackQuery):
#     question = "Названия языка Python произошло ..."
#     answers = [
#         "Рептилии"
#         "от ТВ-шоу «Летающий цирк Монти Пайтона»"
#         "программисты придумали"
#         "нет правильного ответа"
#     ]
#
#     await bot.send_poll(
#         chat_id=call.message.chat.id,
#         question=question,
#         options=answers,
#         is_anonymous=False,
#         type="quiz",
#         correct_option_id=1,
#         explanation="Создатель языка Гвидо ван Россум заявил, что название "
#                     "языка происходит от ТВ-шоу «Летающий цирк Монти Пайтона»",
#         explanation_parse_mode=ParseMode.MARKDOWN_V2,
#
#     )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
