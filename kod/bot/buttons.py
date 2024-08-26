from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

button1 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Ro'yxatdan o'tish 🪪")  
        ],[
            KeyboardButton(text="Marafon haqida 🕺")
        ],[
            KeyboardButton(text="Marafon narxlari 💸")
        ],[
            KeyboardButton(text= "Marafon egasi 👮🏻‍♀️")
        ]
    ]
)

button2 = ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Telfon raqamni yuborish📱",request_contact= True)  
        ],[
            KeyboardButton(text="Bosh menu 🏠")
        ]
    ]
)
button3= ReplyKeyboardMarkup(
    resize_keyboard=True,
    keyboard=[
        [
            KeyboardButton(text="Bosh menu 🏠")
        ]
    ])
