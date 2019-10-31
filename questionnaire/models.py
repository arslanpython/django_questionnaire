from django.db import models


class Questionnaire(models.Model):
    title = models.CharField(max_length=280)

    def __str__(self):
        return self.title


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1024)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=1024)
    message = models.CharField(max_length=1024)
    has_next = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text
