from django.urls import path

from . import views

app_name = 'training'
urlpatterns = [
    path('menu/<int:week_id>/', views.menu, name='menu'),
    path('select/', views.select, name='select'),
]
