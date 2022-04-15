from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import user_kb

from config import bot


class FSMADMIN(StatesGroup):
    id = State()
    user_name = State()
    first_name = State()
    last_name = State()


async def user_command(message: types.Message):
    global USER_ID
    USER_ID = message.chat.id
    await bot.send_message(message.chat.id, "Yes user\n"
                                            "What dou you need",
                           reply_markup=user_kb.button_register)
    await message.delete()


async def unregister_command(message: types.Message,
                             state: FSMContext):
    if message.chat.id == USER_ID:
        current_state = await state.get_state()
        if current_state is None:
            return "State is None,Relax"
        await state.finish()
        await message.reply("Canceled Successfully")


async def fsm_start(message: types.Message):
    if message.chat.id == USER_ID:
        await FSMADMIN.id.set()
        await message.reply("enter your")


async def load_id(message: types.Message,
                  state: FSMContext):
    async with state.proxy() as reg:
        reg['id'] = message.chat.id
    await FSMADMIN.next()
    await message.reply("enter your user_name")


async def load_user_name(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as reg:
        reg['user_name'] = message.text
    await FSMADMIN.next()
    await message.reply("enter your first_name")


async def load_first_name(message: types.Message,
                          state: FSMContext):
    async with state.proxy() as reg:
        reg['first_name'] = message.text
    await FSMADMIN.next()
    await message.reply("enter your last_name")


async def load_last_name(message: types.Message,
                         state: FSMContext):
    async with state.proxy() as reg:
        reg['last_name'] = message.text
    await FSMADMIN.next()
    await message.reply("You have successfully registered")
    async with state.proxy() as data:
        await message.reply(str(data))
    await state.finish()


async def user(message: types.Message):
    await message.reply("1.Start /register\n"
                        "2.cancel /unregister\n")


def register_handler_for_users(dp: Dispatcher):
    dp.register_message_handler(user, commands=['user'])
    dp.register_message_handler(user_command, commands=['user'])
    dp.register_message_handler(unregister_command, state='*', commands=['unregister'])
    dp.message_handler(unregister_command, Text(equals='unregister', ignore_case=False), state='*')
    dp.register_message_handler(load_id, commands=['register'], state=None)
    dp.register_message_handler(load_id, state=FSMADMIN.id)
    dp.register_message_handler(load_user_name, state=FSMADMIN.user_name)
    dp.register_message_handler(load_first_name, state=FSMADMIN.first_name)
    dp.register_message_handler(load_last_name, state=FSMADMIN.last_name)
