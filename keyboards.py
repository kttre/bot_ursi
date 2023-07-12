from aiogram import types
from aiogram.types import InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton

#register
register_button = InlineKeyboardButton(text='Зарегистрироваться', callback_data='register')
register_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(register_button)

#main menu
to_main_menu_button = InlineKeyboardButton(text='Перейти в главное меню', callback_data='to_main_menu')
to_main_menu_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(to_main_menu_button)

#main menu inline
сhange_lead_button = InlineKeyboardButton(text='Сменить руководителя', callback_data='сhange_lead')
close_club_button = InlineKeyboardButton(text='Закрыть клуб', callback_data='close_club')
consutation_button = InlineKeyboardButton(text='Записаться на консультацию', callback_data='consutation')
change_logo_button = InlineKeyboardButton(text='Заменить логотип клуба', callback_data='change_logo')
change_back_button = InlineKeyboardButton(text='Заменить фон клуба', callback_data='change_back')
question_button = InlineKeyboardButton(text='Задать вопрос', callback_data='question')
main_menu_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(сhange_lead_button,
                                                                               close_club_button,
                                                                               consutation_button,
                                                                               change_logo_button,
                                                                               change_back_button,
                                                                               question_button)

#close club
reason_1_button = InlineKeyboardButton(text='Причина 1', callback_data='reason_1')
reason_2_button = InlineKeyboardButton(text='Причина 2', callback_data='reason_2')
reason_other_button = InlineKeyboardButton(text='Другое', callback_data='reason_other')
close_club_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(reason_1_button,
                                                                                reason_2_button,
                                                                                reason_other_button,
                                                                                to_main_menu_button)

#close_reasons
reasons_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(to_main_menu_button)

#colsultation
consutation_button = InlineKeyboardButton(text='Записаться на консультацию', url='https://docs.google.com/spreadsheets/d/1_iuEycevOiY0euh3jVDo_WTD4xSs_BV215fqdxNXkcs/edit?usp=sharing')
consultation_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(consutation_button,
                                                                                  to_main_menu_button)

#question
question_1_button = InlineKeyboardButton(text='Вопрос 1', callback_data='question_1')
question_2_button = InlineKeyboardButton(text='Вопрос 2', callback_data='question_2')
own_question_button = InlineKeyboardButton(text='Задать свой вопрос', callback_data='own_question')
question_inkb = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).add(question_1_button,
                                                                              question_2_button,
                                                                              own_question_button,
                                                                              to_main_menu_button)