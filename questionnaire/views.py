from os import remove, path

from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from questionnaire.models import Question, Questionnaire
from questionnaire.serializer import QuestionSerializer, QuestionnaireSerializer


def index(request):
    questionnaires = Questionnaire.objects.all()
    return render(request, 'questionnaire/index.html', {'questionnaires': questionnaires})


def next_question(request, questionnaire_id):
    questionnaire = get_object_or_404(Questionnaire, pk=questionnaire_id)
    serializer = QuestionnaireSerializer(questionnaire)
    questionnaire = serializer.data

    count = request.GET.get('count')
    selected_choice = ''

    if count:
        count = int(count) + 1
        q_id = request.GET.get('question_id')
        c_id = int(request.GET.get('choice_id'))

        question_serializer = QuestionSerializer(get_object_or_404(Question, pk=q_id))
        question = question_serializer.data
        write_logs(question['question_text'])

        selected_choice = [choice for choice in question['choices'] if choice['id'] == c_id]

        if selected_choice:
            selected_choice = selected_choice[0]
            write_logs(selected_choice['choice_text'])

            if not selected_choice.get('has_next'):
                response = selected_choice.get('message') + '<br> %s' % read_logs()
                return HttpResponse(response)
    else:
        count = 0

    if count < len(questionnaire['questions']):
        context = {
            'questionnaire_title': questionnaire['title'],
            'question': questionnaire['questions'][count],
            'count': count,
            'selected_choice': selected_choice or '',
        }
        return render(request, 'questionnaire/next_question.html', context)
    else:
        return HttpResponse(read_logs())


def write_logs(text):
    with open('logs.txt', 'a') as f:
        f.write(text + ' > ')


def read_logs():
    log = ''
    with open('logs.txt') as f:
        for line in f:
            log += line

    if path.exists('logs.txt'):
        remove('logs.txt')

    return log
