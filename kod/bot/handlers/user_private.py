from typing import Any
from aiogram.filters import CommandStart, Command, Filter
from aiogram.types import Message
from aiogram import  html ,Router,F, types
from buttons import button1, button2
from api import create_user

router=Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    # print(create_user(message.chat.first_name,message.chat.last_name,"17","Manuchexra.@gmail.com","900"))

    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=button1)
    

user_data = {}

class MyFilter(Filter):
    def __init__(self, text: str) -> None:
        self.text = text

    async def __call__(self, message: Message) -> Any:
        # Ensure message.text is not None before calling lower()
        if message.text and self.text.lower() in message.text.lower():
            return True
        return False

@router.message(F.text == "Marafon haqida 🕺")
async def Register(message: Message) -> None:
    await message.answer("👉👉   Marafon   👈👈\nMarafon yo\'li: Samarqand - Jizzax (chegaralari)🚏 \nSana: 30-sentyabr📅\n1-o\'rin 🥇\nAvtomobil Nexia 3\n2-o\'rin 🥈\n2 xonali uy \n3-o\'rin 🥉\nNoutbook")


@router.message(F.text == "Marafon narxlari 💸")
async def Register(message: Message) -> None:
    await message.answer("💸Har bir qatnashuvchidan 100 000 so\'m to\'lash talab qilinadi!")

@router.message(F.text == "Marafon egasi 👮🏻‍♀️")
async def Register(message: Message) -> None:
    await message.answer("Egasi :Valiyev Ali Botirovich\nTelfon raqam: +998 99 777 07 70")

@router.message(F.text == "Ro'yxatdan o'tish 🪪")
async def Register(message: Message) -> None:
    user_id = message.from_user.id
    user_data[user_id] = {'step': 'name'}
    await message.answer("Ismingizni kiriting!\n\nMasalan:\nIsm: Ali")



@router.message(MyFilter( "ism"))
async def Name(message: Message) -> None:
    user_id = message.from_user.id
    if user_id in user_data and user_data[user_id].get('step') == 'name':
        user_data[user_id]['first_name'] = message.text.split(':')[1].strip()
        user_data[user_id]['step'] = 'surname'
        await message.answer("Familiyangizni kiriting!\n\nMasalan:\nFamiliya: Valiyev")

@router.message(MyFilter( "familiya"))
async def Name1(message: Message) -> None:
    user_id = message.from_user.id
    if user_id in user_data and user_data[user_id].get('step') == 'surname':
        user_data[user_id]['last_name'] = message.text.split(':')[1].strip()
        user_data[user_id]['step'] = 'age'
        await message.answer("Yoshingizni kiriting!\n\nMasalan:\nYosh: 18")
@router.message(MyFilter( "yosh"))
async def Register(message: Message) -> None:
    user_id = message.from_user.id
    if user_id in user_data and user_data[user_id].get('step') == 'age':
        user_data[user_id]['age'] = message.text.split(':')[1].strip()
        user_data[user_id]['step'] = 'email'
        await message.answer("Emailingizni kiriting! \n\nMasalan:\nEmail: ali_valiyev@gmail.com")
@router.message(MyFilter( "email"))
async def Register(message: Message) -> None:
    user_id = message.from_user.id
    if user_id in user_data and user_data[user_id].get('step') == 'email':
        user_data[user_id]['email'] = message.text.split(':')[1].strip()
        user_data[user_id]['step'] = 'phone'
        await message.answer("Telefon raqamni yuboring📱! \n\nMasalan: \nPhone: +998 90 555 55 55", reply_markup=button2)

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
        await message.answer("Tabriklayman! \nSiz muvaffaqiyatli ro'yxatdan o'tdingiz.")
        # Optionally, clean up user data
        del user_data[user_id]

Name(Message)