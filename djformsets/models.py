from django.db import models

# Create your models here.
class Question(models.Model):
    text = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    #Reverse relationship
    def get_answers(self):
        return self.answers.all()    

class Answer(models.Model):
    text = models.CharField(max_length=200, verbose_name='Answer')
    correct = models.BooleanField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question {self.question.text}, answer: {self.text}. correct: {self.correct}"
