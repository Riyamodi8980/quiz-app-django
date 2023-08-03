from django.db import models

class QuizCategory(models.Model):
    title=  models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.title


# Create your models here.
class QuesModel(models.Model):
    OPTION_CHOICES = (
    ('option1','option1'),
    ('option2', 'option2'),
    ('option3','option3'),
    ('option4','option4'),
)
    category = models.ForeignKey(QuizCategory , on_delete=models.CASCADE,default='')
    question = models.TextField(max_length=200,default='')
    op1 = models.CharField(max_length=200,default='')
    op2 = models.CharField(max_length=200,default='')
    op3 = models.CharField(max_length=200,default='')
    op4 = models.CharField(max_length=200,default='')
    ans = models.CharField(max_length=200,default='',choices=OPTION_CHOICES)

    def __str__(self):
        return self.question

    