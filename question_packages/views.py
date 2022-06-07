from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# Create your views here.
class SingleQuestionPageView(TemplateView):
    template_name = 'single_question.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

def show_packages(request):
    return HttpResponse('Hello World')



