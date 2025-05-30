from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    tags = ["Hexlet Django Blog"]
    return render(
        request,
        "about.html",
        context={"tags": tags},
    )
