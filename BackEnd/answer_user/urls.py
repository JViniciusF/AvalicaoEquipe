from django.urls import path
from answer_user import views

urlpatterns = [
    path('getAnswerByUser/<userId>',views.getAnswerByUser, name = "getAnswerByUser"),
    
]
