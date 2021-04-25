from django.db import models
from django.contrib.auth.models import User
from question.models import Question

# Create your models here.
class Answer_user (models.Model):
    id = models.AutoField(primary_key = True)
    user_id = models.ForeignKey(User, on_delete = models.CASCADE)
    question_id = models.ForeignKey(Question , on_delete = models.CASCADE)
    answer = models.TextField()
    created_at = models.DateField(auto_now_add = True)
    