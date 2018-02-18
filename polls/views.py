from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
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
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {
        'question': question,
    })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
        pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select the choice(.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
    #Returning HttpResponceRedirrect after successfully
    #dealing with POST data. This prevents data from being
    # posted twice if a user hits the 'Back' button.HttpResponseRedirect
        return HttpResponseRedirect(reverse('polls:results',
        args=(question.id,)))
