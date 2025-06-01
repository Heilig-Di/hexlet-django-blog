from hexlet_django_blog.views.index import HomePageView


class AboutPageView(HomePageView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context={"tags": tags}
        return context
