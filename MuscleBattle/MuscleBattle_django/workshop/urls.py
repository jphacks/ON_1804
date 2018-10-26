from django.urls import path
from . import views

app_name = 'workshop'
urlpatterns = [
    path('intro/', views.intro, name='intro'),
    path('syumi/', views.syumi, name='syumi')

]
