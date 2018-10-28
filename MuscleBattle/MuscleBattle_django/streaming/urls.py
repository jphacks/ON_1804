from django.urls import path, include
from . import views

app_name = 'streaming'
urlpatterns = [
    path('start/', views.start_streaming, name='start_streaming'),
    path('list/', views.slist_streaming, name='list_streaming'),
]
