from django.contrib import admin

# Register your models here.
from .models import Questions, QuestionPackage

admin.site.register([QuestionPackage, Questions])

