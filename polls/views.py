from django.shortcuts import render, get_object_or_404
from .models import Question
# Create your views here.

def index(request):
    latest_quetions_list = Question.objects.order_by('-date')[:10]
    template = 'polls/index.html'
    context = {'latest_question_list': latest_quetions_list,
    }
    ###
    return render(request, template, context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("404\nQuestion not found")
    question = get_object_or_404(Question, pk=question_id)    
    template = 'polls/detail.html'
    context = {'question': question}
    return render(request, template, context)

def results(request, question_id):
    return HttpResponse("Results %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Voting %s" % question_id)