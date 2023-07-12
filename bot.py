from aiogram import Bot, Dispatcher, executor, types
from keyboards import register_inkb, to_main_menu_inkb, main_menu_inkb, \
    close_club_inkb, consultation_inkb, question_inkb

API_TOKEN = '6158582931:AAFa5tddFa8126OBf8Pkco9WobMvjk2v0ho'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def register(message: types.Message):
    await message.delete()
    await message.answer('Привет! Это тг бот клубной системы ИТМО. Чтобы начать позьзоваться им, пройди регу',
                         reply_markup=register_inkb)

@dp.callback_query_handler(text='register')
async def to_main_menu(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Вы удачно прошли регу',
                                     reply_markup=to_main_menu_inkb)

@dp.callback_query_handler(text='to_main_menu')
async def main_menu(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Чем вам помочь?',
                                     reply_markup=main_menu_inkb)

@dp.callback_query_handler(text='close_club')
async def close_club(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Почему вы хотите закрыть клуб?',
                                     reply_markup=close_club_inkb)

@dp.callback_query_handler(text='reason_1')
async def reason_1(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Ваш клуб скоро будет закрыт',
                                     reply_markup=to_main_menu_inkb)

@dp.callback_query_handler(text='reason_2')
async def reason_2(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Ваш клуб скоро будет закрыт',
                                     reply_markup=to_main_menu_inkb)

@dp.callback_query_handler(text='reason_other')
async def reason_other(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Опишите, почемы вы хотите закрыть клуб',
                                     reply_markup=to_main_menu_inkb)

@dp.callback_query_handler(text='сhange_lead')
async def сhange_lead(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Тут собираем данные о новом руководе',
                                     reply_markup=to_main_menu_inkb)

@dp.callback_query_handler(text='consutation')
async def consutation(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Тут собираем данные о новом руководе',
                                     reply_markup=consultation_inkb)

@dp.callback_query_handler(text='change_logo')
async def change_logo(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Тут просим картинку',
                                     reply_markup=to_main_menu_inkb)

@dp.callback_query_handler(text='change_back')
async def сhange_back(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Тут просим картинку',
                                     reply_markup=to_main_menu_inkb)

@dp.callback_query_handler(text='question')
async def question(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('тут собраны самые популярные вопросы, вы можете почитать ответы на них или заать свой вопрос',
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

@dp.callback_query_handler(text='own_question')
async def question_own(callback: types.CallbackQuery):
    await callback.message.delete_reply_markup()
    await callback.message.edit_text('Напишите свой вопрос',
                                     reply_markup=to_main_menu_inkb)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)