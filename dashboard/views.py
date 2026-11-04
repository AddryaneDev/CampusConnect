from accounts.models import CustomUser
from django.views.generic import TemplateView
from django.contrib.auth.mixins import (LoginRequiredMixin, UserPassesTestMixin)

# Create your views here.
class DashboardView(TemplateView):
    template_name = 'dashboard/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['members'] = CustomUser.objects.count()
        context['is_admin'] = (self.request.user.role == CustomUser.Role.ADMIN)
        return context

class AdminPanelView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dashboard/admin_panel.html'

    def test_func(self):
        user = self.request.user
        return self.request.user.role == CustomUser.Role.ADMIN