from django.urls import path
from accounts.views import *
urlpatterns = [
    path('profile',Dashboard.as_view() , name='profile')
]
