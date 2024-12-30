from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry, name='entry'),
    path('main/<str:name>', views.main, name='main'),
    path('horoscope/<str:sign>', views.horoscope, name='horoscope'),
    path('flowers/<str:color>', views.flowers, name='flowers'),
    path('dog', views.dog, name='dog'),
]