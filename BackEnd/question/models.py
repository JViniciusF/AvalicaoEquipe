from django.db import models

# Create your models here.
class Question (models.Model):
    id = models.AutoField(primary_key = True)
    question = models.TextField(max_length = 500)
    type_id = models.ForeignKey('TypeSkill', on_delete = models.CASCADE)
    def __str__(self):
        return self.question

class TypeSkill (models.Model):
    id = models.AutoField(primary_key = True)
    type_skill = models.TextField()
    
    def __str__(self):
        return self.type_skill 