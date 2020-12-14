from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from .models import *


# show last 5 vote
def index(request):
    user = request.user
    question_list = QuestionModel.objects.order_by('-published')[:5]
    context = {
        'question_list': question_list,
        'user': user,
    }
    return render(request, 'vote/index.html', context)


# show detail vote
def detail(request, pk):
    user = request.user
    question = get_object_or_404(QuestionModel, pk=pk)
    context = {
        'question': question,
        'user': user
    }
    print(user)
    print(question.choicemodel_set.all())
    return render(request, 'vote/detail.html', context)


# result
def result(request, pk):
    question = get_object_or_404(QuestionModel, pk=pk)
    context = {
        'question': question,
    }
    return render(request, 'vote/result.html', context)


# vote
def vote(request, pk):
    user = request.user
    if request.method == 'POST':

        question = get_object_or_404(QuestionModel, pk=pk)
        if user in question.voted.all():
            question.voted.remove(user)
        else:
            question.voted.add(user)
        try:
            voted_choice = question.choicemodel_set.get(
                pk=request.POST['choice'])
        except (KeyError, ChoiceModel.DoesNotExist):
            # Redisplay the question voting form.
            return render(request, 'polls/detail.html', {
                'question': question,
            })
        else:
            voted_choice.votes += 1
            voted_choice.save()
            return HttpResponseRedirect(reverse('vote:result', args=(question.id,)))
