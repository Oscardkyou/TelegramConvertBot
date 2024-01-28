from telebot import types

def main():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    b1 = types.KeyboardButton(text='💸Конвертация валюты')
    b2 = types.KeyboardButton(text='📏Конвертация единиц измерения')
    b3 = types.KeyboardButton(text='🌐Конвертация крипты')
    b4 = types.KeyboardButton(text='👤Профиль')


    markup.row(b1)
    markup.row(b2)
    markup.row(b3)
    markup.row(b4)


    return markup


def currency(convert):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in convert:
        markup.add(types.KeyboardButton(text=str(i).upper()))
    b5 = types.KeyboardButton(text='Меню')
    markup.row(b5)

    return markup


def crypto_currency(convert):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in convert:
        markup.add(types.KeyboardButton(text=str(i).upper()))
    b5 = types.KeyboardButton(text='Меню')
    markup.row(b5)

    return markup


def unit_of_measurement():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in ['Километр (км)', 'Метр (м)', 'Дециметр (дм)', 'Сантиметр (см)', 'Миллиметр (мм)']:
        markup.add(types.KeyboardButton(text=i))
    markup.add(types.KeyboardButton(text='Меню'))

    return markup

