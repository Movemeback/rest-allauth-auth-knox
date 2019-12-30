from django.contrib import admin

from forum.models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('created', 'modified', 'subject', 'user', 'body')
    readonly_fields = ('created', 'modified', 'subject', 'user', 'body')


admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('created', 'modified', 'user', 'question', 'body')
    readonly_fields = ('created', 'modified', 'user', 'question', 'body')


admin.site.register(Answer, AnswerAdmin)
