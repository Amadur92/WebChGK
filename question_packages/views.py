from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, UpdateView, CreateView, UpdateView
from django.views.generic.edit import CreateView
from .models import Questions
from django.urls import reverse_lazy


# Create your views here.
class SingleQuestionPageView(DetailView):
    model = Questions
    template_name = 'Single_question.html'
    context_object_name = 'question'


class QuestionCreateView(CreateView):
    model = Questions
    template_name = 'create_question.html'
    fields = '__all__'

class AboutPageView(TemplateView):
    template_name = 'about.html'

def show_packages(request):
    return HttpResponse('Hello World')

class HomePageView(ListView):
    model = Questions
    template_name = 'home.html'
    
class RandomQuestionPageView(DetailView):
    model = Questions
    template_name = 'random_question.html'
    context_object_name = 'question'


class QuestionDeleteView(DeleteView):
    model = Questions
    template_name = 'delete_question.html'
    success_url = reverse_lazy('home')


class QuestionUpdateView(UpdateView):
    model = Questions
    template_name = 'update_question.html'
    success_url = reverse_lazy('home')
    fields = '__all__'
