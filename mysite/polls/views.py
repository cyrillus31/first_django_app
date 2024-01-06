from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader


from .models import Question


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
            "latest_question_list": latest_question_list,
            }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "polls/detail.html", context)



def results(request, question_id):
    response = f"You are looking at the results of question {question_id}"
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f"You're votin on question {question_id}")




