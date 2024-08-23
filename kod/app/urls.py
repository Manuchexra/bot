from .views import BotUserApiView
from django.urls import path

urlpatterns=[
    path("users", BotUserApiView.as_view(), name="users")
]