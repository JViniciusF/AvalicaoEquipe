
from django.urls import path
from question import views

urlpatterns = [
    path('registerQuestions/',views.registerQuestion, name = "registerQuestion"),
    path('registerTypeSkill/',views.registerTypeSkill,name = "registerTypeSkill"),
    path('getAllQuestions/', views.getAllQuestions, name = "getAllQuestions"),
    path('getQuestionById/<id>',views.getQuestionById,name= "getQuestionById"),
    path('getAllTypeSkill/', views.getAllTypeSkill, name = "getAllTypeSkill"),
    path('getTypeSkillById/<id>',views.getTypeSkillById,name= "getTypeSkillById"),
]
