from django.urls import path
from hexlet_django_blog.article import views as article_views
from django.shortcuts import redirect
from django.urls import reverse

urlpatterns = [
    path(
        'articles/<str:tags>/<int:article_id>/',
        article_views.index,
        name='article'
    ),
    path(
        '',
        lambda request: redirect(reverse('article', kwargs={'tags': 'python', 'article_id': 42}))
    ),
]
