from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from wallet.models import Wallet


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "wallet/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["wallet"] = Wallet.objects.get(owner=self.request.user)
        return context
