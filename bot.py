from aiogram import Bot, Dispatcher, executor, types
from keyboards import *
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from database import *


class MyDialog(StatesGroup):
    answer = State()
    isu_num = State()
    close_club = State()


API_TOKEN = '6158582931:AAFa5tddFa8126OBf8Pkco9WobMvjk2v0ho'
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
id_of_message = 0


@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    await message.delete()
    await message.answer('Привет! Это тг бот клубной системы ИТМО. Чтобы начать позьзоваться им, пройди регистрацию.',
                         reply_markup=register_inkb)


@dp.callback_query_handler(text='register')
async def to_main_menu(callback: types.CallbackQuery):
    global id_of_message
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Введите ваш номер ИСУ')
    id_of_message = callback.message.message_id
    await MyDialog.isu_num.set()


@dp.message_handler(state=MyDialog.isu_num)
async def process_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']

        await MyDialog.answer.set()

    await state.finish()
    if message.from_user.id == 570427565:
        role_client = 'admin'
    else:
        role_client = 'member'

    register_db(message.from_user.id, user_message, role_client)

    await bot.delete_message(message.chat.id, id_of_message)
    await message.delete()

    if role_client == "admin":
        await message.answer('Вы удачно прошли регистрацию',
                                     reply_markup=to_main_menu_admin_inkb)
    else:
        await message.answer('Вы удачно прошли регистрацию',
                                reply_markup=to_main_menu_inkb)


@dp.callback_query_handler(text='to_main_menu')
async def main_menu(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Чем вам помочь?',
                                     reply_markup=main_menu_inkb)


@dp.callback_query_handler(text='to_main_menu_admin')
async def main_menu(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Чем вам помочь?',
                                     reply_markup=admin_main_menu_inkb)


@dp.callback_query_handler(text='close_club')
async def closing_club(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()

    data_of_clubs = admin_of_clubs(callback.from_user.id)

    if len(data_of_clubs):
        answer_to_user = 'Вы можете подать заявку на закрытие следующих клубов:'
        for name in data_of_clubs:
            answer_to_user += f'\n- {name}'

        await callback.message.edit_text(answer_to_user, reply_markup=close_club_url_inkb)
    else:
        await callback.message.edit_text('В данный момент вы не являетесь руководителем какого-либо клуба!',
                                         reply_markup=to_main_menu_inkb)


@dp.callback_query_handler(text='question')
async def question(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Тут собраны самые популярные вопросы, вы можете почитать ответы на них или заать свой вопрос',
                                     reply_markup=question_inkb)


@dp.callback_query_handler(text='question_1')
async def question_1(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Ответ 1',
                                     reply_markup=to_main_menu_inkb)


@dp.callback_query_handler(text='question_2')
async def question_2(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Ответ 2',
                                     reply_markup=to_main_menu_inkb)

"""
@dp.callback_query_handler(text='own_question')
async def question_own(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Напишите свой вопрос',
                                     reply_markup=to_main_menu_inkb)
"""


@dp.callback_query_handler(text='admin_change_lead')
async def question_own(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Введите информацию о смене руководителя в одну строчку в виде:\n*Номер ИСУ старого руководителя* '
                                     '*Номер ИСУ нового руководителя*')
    await MyDialog.answer.set()


@dp.message_handler(state=MyDialog.answer)
async def process_message(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']

        old_isu, new_isu = map(int, user_message.split())

        current_id_club, ans1 = get_id_club(old_isu)

        ans2 = change_lead_club(new_isu, current_id_club)

        await MyDialog.answer.set()

        if ans1 and ans2:
            await message.answer('Руководитель успешно изменён!')
        else:
            await message.answer('Неверные номера ИСУ!')

        await message.answer('Чем вам помочь?',
                             reply_markup=admin_main_menu_inkb)
    await state.finish()


@dp.callback_query_handler(text='admin_close_club')
async def question_own(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Введите название клуба в одну строчку')
    await MyDialog.close_club.set()


@dp.message_handler(state=MyDialog.close_club)
async def process_message(message: types.Message, state: FSMContext):

    async with state.proxy() as data:
        data['text'] = message.text
        user_message = data['text']

        ans = close_club(user_message)

        await MyDialog.close_club.set()

        if ans:
            await message.answer('Клуб успешно закрыт!')
        else:
            await message.answer('Неверно указано имя клуба!')

        await message.answer('Чем вам помочь?',
                             reply_markup=admin_main_menu_inkb)
    await state.finish()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
