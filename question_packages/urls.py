from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('sq/<int:pk>', views.SingleQuestionPageView.as_view(), name = 'single_question'),
    path('about/', views.AboutPageView.as_view(), name = 'about'),
    path('sq/random', views.RandomQuestionPageView.as_view(), name = 'random_question'),
    path('sq/<int:pk>/delete', views.QuestionDeleteView.as_view(),
         name='delete_question'),
    path('sq/new', views.QuestionCreateView.as_view(), name='create_question'),
    path('sq/<int:pk>/update', views.QuestionUpdateView.as_view(),
         name='update_question'),
    path('accounts/', include('django.contrib.auth.urls'))
]
