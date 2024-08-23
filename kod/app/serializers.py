from .models import BotUsers
from rest_framework.serializers import ModelSerializer

class BotUserSerializers(ModelSerializer):
    class Meta:
        model=BotUsers
        fields=("user_id","first_name","last_name","age","email")