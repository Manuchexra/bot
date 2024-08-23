from .models import BotUsers
from .serializers import BotUserSerializers
from rest_framework.generics import ListCreateAPIView

class BotUserApiView(ListCreateAPIView):
    queryset=BotUsers.objects.all()
    serializer_class=BotUserSerializers
