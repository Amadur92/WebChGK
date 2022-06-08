from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Questions


# Create your views here.
class SingleQuestionPageView(TemplateView):
    template_name = 'Single_question.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

def show_packages(request):
    return HttpResponse('Hello World')

class HomePageView(ListView):
    model = Questions
    template_name = 'home.html'

