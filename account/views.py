from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from account.forms import *

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "account/index.html"
    
    # LoginRequiredMixin Values
    login_url = reverse_lazy('account:login')
    redirect_field_name = ''
    

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = "account/register.html"

    def get_success_url(self):
        return reverse_lazy('account:login')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Create an Account"
        return context
    

class LoginView(BaseLoginView):
    template_name = "account/login.html"

    def get_success_url(self):
        return reverse_lazy('account:index')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Create an Account"
        return context
    

class LogoutView(BaseLogoutView):
    next_page = "account:login"

