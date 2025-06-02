from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View


class AboutViews(View):
    def get(self, request, *args, **kwargs):
        tags = ["Hexlet Django Blog"]
        return render(request, "template_name.html", {"tags": tags})


class IndexView(TemplateView):
    template_name = "template_name.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        return context
