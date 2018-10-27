from django.urls import path

from . import views

urlpatterns = [
    path('menu/<int:week_id>/', views.menu, name='menu'),
]
