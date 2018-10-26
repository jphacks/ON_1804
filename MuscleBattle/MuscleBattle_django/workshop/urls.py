from django.urls import path, include
from . import views

urlpatterns = [
    path('intro/', views.intro, name = 'intro'),
    path('shumi/', views.shumi, name = 'shumi'),
]
