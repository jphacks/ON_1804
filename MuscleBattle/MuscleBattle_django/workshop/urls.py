from django.urls import path, include
from . import views

urlpatterns = [
#introきたらviews.introを起動するぜ
    path('intro/', views.intro, name='intro'),
    path('syumi/', views.syumi, name='syumi')
]
