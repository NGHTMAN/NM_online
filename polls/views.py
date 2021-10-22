from django.utils import timezone

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.views.generic import UpdateView, CreateView, DeleteView

from .forms import CreateForm
from .models import Questions, Choice


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Questions.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Questions
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Questions
    template_name = 'polls/results.html'


class QuestionsUpdateView(UpdateView):
    model = Questions
    fields = ['question_text']
    template_name = 'polls/question_update_form.html'


class ChoiceUpdateView(UpdateView):
    model = Choice
    fields = ['question', 'choice_text']
    template_name = 'polls/choice_update_form.html'


class ChoiceDeleteView(DeleteView):
    model = Choice
    pk_url_kwarg = "choice_id"
    success_url = '/polls/'
    template_name = 'polls/choice_delete_form.html'


class ChoiceCreateView(CreateView):
    model = Choice
    fields = ['question', 'choice_text']
    template_name = 'polls/choice_create_form.html'


def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def create_form(request):
    return render(request, 'polls/create_form.html')


def create(request):
    if request.method == "POST":
        form = CreateForm(request.POST)
        if form.is_valid():
            name = request.POST['question_name']
            new_question = Questions(question_text=name, pub_date=timezone.now())
            new_question.save()
            return HttpResponseRedirect(reverse('polls:success_saved'))
    else:
        form = CreateForm()
        return render(request, 'polls/create.html', {'form': form})


def success_saved(request):
    return render(request, 'polls/success_saved.html')
