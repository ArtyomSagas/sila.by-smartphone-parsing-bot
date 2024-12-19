from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from answers import *
import keyboards as kb
import asyncio
from datetime import datetime, timedelta

router = Router()
user_pages = {}
user_last_interaction = {}


async def cleanup_inactive_users():
    while True:
        now = datetime.now()
        inactive_users = [
            user_id for user_id, last_time in user_last_interaction.items()
            if now - last_time > timedelta(hours=12)
        ]
        for user_id in inactive_users:
            user_pages.pop(user_id, None)
            user_last_interaction.pop(user_id, None)
        await asyncio.sleep(43200)


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(start_answer, reply_markup=kb.main)


@router.message(F.text == 'Поехали!')
async def cmd_run(message: Message):
    user_id = message.from_user.id
    user_pages[user_id] = 1
    user_last_interaction[user_id] = datetime.now()
    await message.answer(await run_answer(user_pages[user_id]), reply_markup=await kb.inline_products(),
                         disable_web_page_preview=True)


@router.callback_query(F.data == 'left')
async def left(callback: CallbackQuery):
    user_id = callback.from_user.id
    user_last_interaction[user_id] = datetime.now()
    current_page = user_pages.get(user_id, 1)
    if current_page > 1:
        user_pages[user_id] = current_page - 1
        await callback.answer(str(user_pages[user_id]))
        await callback.message.edit_text(await run_answer(user_pages[user_id]), reply_markup=await kb.inline_products(),
                                         disable_web_page_preview=True)
    else:
        await callback.answer(str(user_pages[user_id]))


@router.callback_query(F.data == 'right')
async def left(callback: CallbackQuery):
    user_id = callback.from_user.id
    user_last_interaction[user_id] = datetime.now()
    current_page = user_pages.get(user_id, 1)
    if current_page < 160:
        user_pages[user_id] = current_page + 1
        await callback.answer(str(user_pages[user_id]))
        await callback.message.edit_text(await run_answer(user_pages[user_id]), reply_markup=await kb.inline_products(),
                                         disable_web_page_preview=True)
    else:
        await callback.answer(str(user_pages[user_id]))
