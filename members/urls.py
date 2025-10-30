from django.urls import path
from . import views

# url
urlpatterns = [
    path('hello/', views.say_hello, name='say_hello'),
]
