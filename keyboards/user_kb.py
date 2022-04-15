from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_register = KeyboardButton('/user')
button_unregister = KeyboardButton('/unregister')


button_admin = ReplyKeyboardMarkup(
    resize_keyboard=True).row(button_register, button_unregister)

