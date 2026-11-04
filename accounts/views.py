from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView

from accounts.models import CustomUser

# Create your views here.
class SignupView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'registration/profile.html'

    fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'course',
    ]

    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user