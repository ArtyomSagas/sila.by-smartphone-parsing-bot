from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Поехали!')]
],
                           resize_keyboard=True,
                           input_field_placeholder='Нажмите чтобы начать',
                           one_time_keyboard=True
                          )


async def inline_products():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text='<--', callback_data='left'),
            InlineKeyboardButton(text='-->', callback_data='right')
        ]
    ])
    return keyboard

