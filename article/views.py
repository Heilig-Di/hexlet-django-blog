from django.shortcuts import render
from django.views import View
from django.http import HttpResponse


def index(request, tags, article_id):
    return HttpResponse(f"Статья номер {article_id}. Тег {tags}")


class AboutViews(View):
    def get(self, request, *args, **kwargs):
        tags = ["Hexlet Django Blog"]
        return render(request, "template_name.html", {"tags": tags})
