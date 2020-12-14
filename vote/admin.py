from django.contrib import admin

# Register your models here.
from .models import *


class ChoiceInline(admin.TabularInline):
    model = ChoiceModel
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_title']}),
                 ('voted', {'fields': ['voted']}),
                 ('Date Information', {'fields': ['published'], 'classes': ['collapse']}), ]
    inlines = [ChoiceInline]


admin.site.register(QuestionModel, QuestionAdmin)
