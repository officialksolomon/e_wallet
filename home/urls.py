from django.urls import path

from .views import FeaturesPageView, HomePageView, AboutPageView

app_name = "home"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("features/", FeaturesPageView.as_view(), name="features"),
]
