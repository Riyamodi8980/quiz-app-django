from django.shortcuts import redirect,render ,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def base(request):
    context=QuizCategory.objects.all()
    return render(request,'Quiz/base.html',{'context':context})

def editquiz(request,category_title):
    category=QuizCategory.objects.filter(title=category_title).first()
    questions=QuesModel.objects.filter(category=category)
    context = {
        'questions':questions,
        'title':category_title
    }
    return render(request,'Quiz/editquiz.html',context)
    
def startquiz(request,category_title):
    category=QuizCategory.objects.filter(title=category_title).first()
    questions=QuesModel.objects.filter(category=category)
    if request.method == 'POST':
        print(request.POST)
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
                correct+=1
            else:
                wrong+=1
        percent = correct/((correct+wrong)) *100
        context = {
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'Quiz/result.html',context)
    else:
        context = {
            'questions':questions
        }
        return render(request,'Quiz/home.html',context)

    
def newaddQuestion(request,category_title): 
    category=QuizCategory.objects.filter(title=category_title).first()   
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                quiz_ques=form.save(commit=False)
                quiz_ques.category=category
                quiz_ques.save()
                redirect_url = reverse('editquiz', args=[category_title])
                return redirect(redirect_url)
        context={'form':form}
        return render(request,'Quiz/addQuestion.html',context)
    else: 
        return redirect('home') 
    
def editQuestion(request,pk):
    question=get_object_or_404(QuesModel, pk=pk)
    category_title=question.category.title  
    if request.user.is_staff:
        form=addQuestionform(instance=question)
        if(request.method=='POST'):
            form=addQuestionform(request.POST,instance=question)
            if(form.is_valid()):
                form.save()
                redirect_url = reverse('editquiz', args=[category_title])
                return redirect(redirect_url)
        context={'form':form}
        return render(request,'Quiz/editQuestion.html',context)
    else: 
        return redirect('home') 

def deleteQuestion(request,pk):
    question=get_object_or_404(QuesModel, pk=pk)
    print(question)
    category_title=question.category.title
    question.delete()
    redirect_url = reverse('editquiz', args=[category_title])
    return redirect(redirect_url)

#addQuizCategory
def addCategory(request):
    if request.user.is_staff:
        form=addquizCategoryform()
        if(request.method=='POST'):
            form=addquizCategoryform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('base')
        context={'form':form}
        return render(request,'Quiz/addCategory.html',context)
    else: 
        return redirect('home') 


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'Quiz/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('base')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'Quiz/login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('login')

