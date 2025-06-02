from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View


class AboutViews(View):
    def get(self, request, *args, **kwargs):
        tags = ["Hexlet Django Blog"]
        return render(request, "template_name.html", {"tags": tags})

class HomePageView(TemplateView):
    template_name = "home.html"

def index(self, **kwargs):
        context = super().index(**kwargs)
        context["who"] = "World"
        return context
