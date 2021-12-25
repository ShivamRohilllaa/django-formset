from django.contrib import admin
from .models import *
# Register your models here.

class AnswersAdmin(admin.TabularInline):
    model = Answer

class QuestionsAdmin(admin.ModelAdmin):
    inlines = [
    AnswersAdmin
    ]
    
admin.site.register(Question, QuestionsAdmin)