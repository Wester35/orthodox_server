from django.urls import path
from .views import *

urlpatterns = [
    path('list/<int:pk>/', ScheduleslineList.as_view(), name='schedule_list'),
    path('create/', SchedulesCreate.as_view(), name='schedule_create'),
    path('update/<int:pk>/', SchedulesUpdate.as_view(), name='schedule_update'),
    path('<int:pk>/', SchedulesDetail.as_view(), name='schedule'),
]