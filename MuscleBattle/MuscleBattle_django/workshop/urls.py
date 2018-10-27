from django.urls import path, include
from . import views

app_name = 'workshop'
urlpatterns = [
    path('hobby/', views.hobby, name='hobby'),
    path('intro/', views.intro, name='intro'),
    path('syumi/', views.syumi, name='syumi'),
]
