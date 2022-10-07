from django.urls import path

from .api.views import UserCreate

app_name = 'users'

urlpatterns = [
    path('users/', UserCreate.as_view(), name='create')
]
