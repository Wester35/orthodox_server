from django.urls import path
from .views import *

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('<int:pk>/', DetailUser.as_view(), name='user_detail'),
    path('update/<int:pk>/', UpdateUser.as_view(), name='user_update')
]
