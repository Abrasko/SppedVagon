from django.shortcuts import render, get_object_or_404
from .models import Question, Choice
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic

from django.utils import timezone
# Create your views here.

# def index(request):
#     latest_quetions_list = Question.objects.order_by('-date')[:10]
#     template = 'polls/index.html'
#     context = {'latest_question_list': latest_quetions_list,
#     }
#     ###
#     return render(request, template, context)

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)    
#     template = 'polls/detail.html'
#     context = {'question': question}
#     return render(request, template, context)

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {
#         'question': question,
#     })

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(
        date__lte=timezone.now()
        ).order_by('-date')[:10]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    context_object_name = 'question_detail'

    def get_queryset(self):
        return Question.objects.filter(date__lte = timezone.now())

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
    context_object_name = 'question_result'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(
        #value from form post in html file
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
