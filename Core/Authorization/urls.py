from django.urls import path
from .views import authenticate_and_fetch

urlpatterns = [
    
    path('', authenticate_and_fetch, name='authenticate_and_fetch'),
]