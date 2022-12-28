from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home/home.html"


class AboutPageView(TemplateView):
    template_name = "home/about.html"


class FeaturesPageView(TemplateView):
    template_name = "home/features.html"
