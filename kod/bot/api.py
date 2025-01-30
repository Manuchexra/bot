import requests
import json

BASE_URL = "http://localhost:8000/api"

def create_user(first_name, last_name, age, email, user_id, phone):
    url = f"{BASE_URL}/users"
    response = requests.get(url=url)
    
    if response.status_code == 200:
        data = response.json()  
        user_exist = any(i["user_id"] == user_id for i in data)  
        
        if not user_exist:
            post_response = requests.post(
                url=url, 
                json={"first_name": first_name, "last_name": last_name, "age": age, "email": email, "user_id": user_id, "phone": phone}
            )
            if post_response.status_code == 201: 
                return "Foydalanuvchi yaratildi."
            else:
                return f"Foydalanuvchini yaratishda xatolik: {post_response.status_code}"
        else:
            return "Foydalanuvchi ro'yxatdan o'tgan."
    else:
        return f"Ma'lumotlarni olishda xatolik: {response.status_code}"
