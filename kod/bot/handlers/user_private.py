from typing import Any
from aiogram.filters import CommandStart, Filter
from aiogram.types import Message
from aiogram import html, Router, F
from buttons import button1, button2, button3
from api import create_user
from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
TOKEN = os.getenv("TOKEN")
router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Salom, {html.bold(message.from_user.full_name)}!", reply_markup=button1)

user_data = {}
@router.message(F.text == "Bosh menu 🏠")
async def menu(message: Message) -> None:
    await command_start_handler(message) 
@router.message(F.text == "Marafon haqida 🕺")
async def About(message: Message) -> None:
    await message.answer("👉👉   Marafon   👈👈\nMarafon yo\'li: Samarqand - Jizzax (chegaralari)🚏 \nSana: 30-sentyabr📅\n1-o\'rin 🥇\nAvtomobil Nexia 3\n2-o\'rin 🥈\n2 xonali uy \n3-o\'rin 🥉\nNoutbook")

@router.message(F.text == "Marafon narxlari 💸")
async def Price(message: Message) -> None:
    await message.answer("💸Har bir qatnashuvchidan 100 000 so\'m to\'lash talab qilinadi!")

@router.message(F.text == "Marafon egasi 👮🏻‍♀️")
async def Owner(message: Message) -> None:
    await message.answer("Egasi :Valiyev Ali Botirovich\nTelfon raqam: +998 99 777 07 70")

@router.message(F.text == "Ro'yxatdan o'tish 🪪")
async def register(message: Message) -> None:
    user_id = message.from_user.id
    user_data[user_id] = {'step': 'name'}
    await message.answer("Ismingizni kiriting!\n\nMasalan:\nIsm: Ali", reply_markup=button3)

@router.message(F.text)
async def collect_user_data(message: Message) -> None:
    user_id = message.from_user.id
    if user_id in user_data:
        step = user_data[user_id]['step']
        if step == 'name':
            user_data[user_id]['first_name'] = message.text
            user_data[user_id]['step'] = 'surname'
            await message.answer("Familiyangizni kiriting!\n\nMasalan:\nFamiliya: Valiyev", reply_markup=button3)
        elif step == 'surname':
            user_data[user_id]['last_name'] = message.text
            user_data[user_id]['step'] = 'age'
            await message.answer("Yoshingizni kiriting!\n\nMasalan:\nYosh: 18", reply_markup=button3)
        elif step == 'age':
            user_data[user_id]['age'] = message.text
            user_data[user_id]['step'] = 'email'
            await message.answer("Emailingizni kiriting! \n\nMasalan:\nEmail: ali_valiyev@gmail.com",reply_markup=button3)
        elif step == 'email':
            user_data[user_id]['email'] = message.text
            user_data[user_id]['step'] = 'phone'
            await message.answer("Telefon raqamni yuboring📱! \n\nMasalan: \nPhone: +998 90 555 55 55", reply_markup=button2)

from aiogram import Bot

bot = Bot(token=TOKEN)

ADMIN_CHAT_ID = '6452937721'

@router.message(F.contact)
async def process_contact(message: Message) -> None:
    user_id = message.from_user.id
    if user_id in user_data and user_data[user_id].get('step') == 'phone':
        phone = message.contact.phone_number
        user_data[user_id]['phone'] = phone
        response = create_user(
            first_name=user_data[user_id]['first_name'],
            last_name=user_data[user_id]['last_name'],
            age=user_data[user_id]['age'],
            email=user_data[user_id]['email'],
            user_id=user_id,
            phone=phone
        )
        await message.answer("Tabriklayman! \nSiz muvaffaqiyatli ro'yxatdan o'tdingiz.", reply_markup=button3)
        user_info_message = (
            f"Yangi foydalanuvchi ro'yxatdan o'tdi:\n"
            f"Ism: {user_data[user_id]['first_name']}\n"
            f"Familiya: {user_data[user_id]['last_name']}\n"
            f"Yosh: {user_data[user_id]['age']}\n"
            f"Email: {user_data[user_id]['email']}\n"
            f"Telefon: {user_data[user_id]['phone']}\n"
            f"User ID: {user_id}"
        )
        await bot.send_message(ADMIN_CHAT_ID, user_info_message)
    
        del user_data[user_id]



