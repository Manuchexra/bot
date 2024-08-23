import requests
import json

BASE_URL="http://localhost:8000/api"

def create_user(first_name, last_name, age, email,user_id, phone):
    url= f"{BASE_URL}/users"
    response = requests.get(url=url).text
    data= json.loads(response)
    user_exist= False
    for i in data:
        if user_id== i["user_id"]:
            user_exist= True
            break
    if user_exist== False:
        requests.post(url=url,data={"first_name":first_name,"last_name":last_name,"age":age,"email":email,"user_id":user_id, "phone":phone})
        return "Foydalanuvchi yaratildi."
    else:
        return "Foydalanuvchi ro'yxatdan o'tgan"
