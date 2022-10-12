from django.urls import path

from .api.views import UserListCreate, UserValidate

app_name = 'users'

urlpatterns = [
    path('users', UserListCreate.as_view(), name='create'),
    path('users/validate', UserValidate.as_view(), name='validate'),
]
