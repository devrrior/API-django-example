from django.urls import path

from .api.views import UserCreate, UserValidate

app_name = 'users'

urlpatterns = [
    path('users', UserCreate.as_view(), name='create'),
    path('users/validate', UserValidate.as_view(), name='validate'),
]
