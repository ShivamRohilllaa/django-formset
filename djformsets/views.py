from django.shortcuts import redirect, render
from .forms import *
from .models import *
# Create your views here.

def home(request):
    ques = Question.objects.all()
    context = {'ques':ques}
    return render(request, 'index.html', context)


def add_questions(request):
    ques= QuestionsForm()
    formset = AnswerFormset(queryset=Answer.objects.none())
    if request.method=='POST':
        ques= QuestionsForm(request.POST)
        formset = AnswerFormset(request.POST)
        if ques.is_valid() and formset.is_valid():
            ques = ques.save()
            for form in formset:
                answer = form.save(commit=False)
                answer.question = ques
                answer.save() 
            return redirect('home')
    return render(request, "add-ques.html", {'ques':ques, 'formset':formset})

