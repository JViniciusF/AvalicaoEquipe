from django.shortcuts import render
from .models import Question, TypeSkill
from django.http import HttpResponse,JsonResponse
# Create your views here.

def registerQuestion(request):
    question = request.POST.get('question')
    type_skill_id = request.POST.get('type_skill_id')

    new_question = Question(
        question = question,
        type_id = type_skill_id
    )

    new_question.save()
    return HttpResponse(new_question.id)

def registerTypeSkill(request):
    type_skill = request.POST.get('type_skill')

    new_type_skill = TypeSkill(
        type_skill = type_skill
    )
    new_type_skill.save()

    return HttpResponse(new_type_skill)
    
def getAllQuestions(request):
    questions = Question.objects.all().values()
    return HttpResponse(questions)

def getQuestionById(request,id):
    question = Question.objects.get(id = id)
    return HttpResponse(question)

def getAllTypeSkill(request):
    type_skill = TypeSkill.objects.all().values()
    return HttpResponse(type_skill)

def getTypeSkillById(request,id):
    type_skill = TypeSkill.objects.get(id = id)
    return HttpResponse(type_skill)