from random import choice
from django.contrib import admin


admin.site.site_header = 'Polls Admin'
admin.site.site_title = 'Polls Admin Area'
admin.site.index_title = 'Welcome Aboard'
# Register your models here.
from .models import Question,Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),('Date Information', {'fields': ['pub_date'],'classes': ['collapse']}),]
    inlines = [ChoiceInLine]


admin.site.register(Question,QuestionAdmin) 