from django.contrib import admin

from questionnaire.models import Questionnaire, Question, Choice


admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(Choice)
