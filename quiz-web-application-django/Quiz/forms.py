from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1'] 

class addQuestionform(ModelForm):
    class Meta:
        model=QuesModel
        fields=['question','op1','op2','op3','op4','ans']

    

class addquizCategoryform(ModelForm):
    class Meta:
        model=QuizCategory
        fields="__all__"

    
    