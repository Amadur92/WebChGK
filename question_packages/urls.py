from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('sq/', views.SingleQuestionPageView.as_view(), name = 'single_question'),
    path('about/', views.AboutPageView.as_view(), name = 'about')
]
