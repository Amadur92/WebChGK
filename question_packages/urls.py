from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_packages, name='home'),
    path('sq/', views.SingleQuestionPageView.as_view(), name = 'single_question'),
    path('about/', views.AboutPageView.as_view(), name = 'about')
]
