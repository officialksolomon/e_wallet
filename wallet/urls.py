from django.urls import path

from wallet.views import DashboardView

app_name = "wallet"
urlpatterns = [
    path("", DashboardView.as_view(), name="home"),
]
