from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Question


def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions':questions})

def list(request):
    return render(request, 'polls/list.html')

def receipt(request):
    return render(request, 'polls/receipt.html')

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/details.html', {'question':question})