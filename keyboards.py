from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

#register
register_button = InlineKeyboardButton(text='Зарегистрироваться', callback_data='register')
register_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(register_button)

#main menu
to_main_menu_button = InlineKeyboardButton(text='Перейти в главное меню', callback_data='to_main_menu')
to_main_menu_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(to_main_menu_button)

to_main_menu_admin_button = InlineKeyboardButton(text='Перейти в главное меню', callback_data='to_main_menu_admin')
to_main_menu_admin_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(to_main_menu_admin_button)

#main menu inline
сhange_lead_button = InlineKeyboardButton(text='Сменить руководителя', url='https://my.itmo.ru/requests/new/2266')
close_club_button = InlineKeyboardButton(text='Закрыть клуб', url='https://my.itmo.ru/requests/new/2266')
consutation_button = InlineKeyboardButton(text='Записаться на консультацию', url='https://my.itmo.ru/requests/new/2266')
change_logo_button = InlineKeyboardButton(text='Заменить логотип клуба', url='https://my.itmo.ru/requests/new/2266')
change_back_button = InlineKeyboardButton(text='Заменить фон клуба', url='https://my.itmo.ru/requests/new/2266')
question_button = InlineKeyboardButton(text='Задать вопрос', callback_data='question')
main_menu_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(сhange_lead_button,
                                                                               close_club_button,
                                                                               consutation_button,
                                                                               change_logo_button,
                                                                               change_back_button,
                                                                               question_button)

change_lead_admin_button = InlineKeyboardButton(text='Сменить руководителя', callback_data='admin_change_lead')
close_club_admin_button = InlineKeyboardButton(text='Закрыть клуб', callback_data='admin_close_club')
admin_main_menu_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(change_lead_admin_button,
                                                                                     close_club_admin_button)


#question
question_1_button = InlineKeyboardButton(text='Вопрос 1', callback_data='question_1')
question_2_button = InlineKeyboardButton(text='Вопрос 2', callback_data='question_2')
own_question_button = InlineKeyboardButton(text='Задать свой вопрос', callback_data='own_question')
question_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(question_1_button,
                                                                              question_2_button,
                                                                              own_question_button,
                                                                              to_main_menu_button)