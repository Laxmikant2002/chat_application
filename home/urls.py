from django.urls import path
from home.views import home_view, chat_view

urlpatterns = [
    path('', home_view, name="home"),
    path('chat/<str:username>/', chat_view, name="chat"),
]