from django.contrib import admin
from questions.models import Examination, Question, Subject, Topic
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'question', 'option_a', 'option_b', 'option_c', 
        'option_d', 'option_e', 'ans', 'examination', 'subject'
        )
    list_filter = ('examination', 'subject')
    fields = (
        'subject', 'topic', 'question_text', 'option_a', 
        'option_b', 'option_c', 'option_d', 'option_e', 
        'ans'
        )
    search_fields = (
        'question_text', 'option_a', 'option_b', 'option_c', 
        'option_d', 'option_e', 'question_code'
        )
    ordering = ('question_code',)
    save_as = True

admin.site.register(Examination)
admin.site.register(Question)
admin.site.register(Subject)
admin.site.register(Topic)