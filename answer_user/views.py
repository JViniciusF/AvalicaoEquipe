from django.shortcuts import render
from django.http import HttpResponse
from .models import Answer_user

# Create your views here.
def getAnswerByUser(request,userId):
    answer = Answer_user.objects.filter(user_id = userId).values()
    return HttpResponse(answer)

def registerAnswer(request):
    user_id = request.POST.get('user_id')
    question_id = request.POST.get('question_id')
    answer = request.POST.get('answer')

    new_answer = Answer_user(
        user_id = user_id,
        question_id = question_id,
        answer = answer
    )

    new_answer.save()

    return HttpResponse(new_answer)