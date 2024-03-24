from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView

from .forms import *


class RegisterUser(CreateView):
    template_name = "main/account_sign.html"
    form_class = CustomUserCreationForm

    def form_valid(self, form):
        form.instance.rights = 1
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_title_form'] = 'Зарегистрироваться'
        context['name_button'] = 'Зарегистрироваться'
        context['title'] = 'Регистрация'
        return context


class DetailUser(DetailView):
    template_name = "main/detail.html"
    model = CustomUser
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователь'
        return context

    extra_context = {'title': 'Статьи'}


class UpdateUser(UpdateView):
    template_name = "main/update.html"
    model = CustomUser
    fields = ['username', 'email', 'phone', 'first_name', 'last_name']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_title_form'] = 'Редактирование'
        context['name_button'] = 'Редактировать'
        context['title'] = 'Пользователь'
        return context

    extra_context = {'title': 'Статьи'}


class LoginUser(LoginView):
    template_name = "main/account_sign.html"
    form_class = CustomAuthenticationForm

    def get_success_url(self):
        return reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name_title_form'] = 'Войти'
        context['name_button'] = 'Войти'
        context['title'] = 'Вход'
        return context

