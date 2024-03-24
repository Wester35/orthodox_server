from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from .models import *
from .forms import *


class NewslineCreate(LoginRequiredMixin, CreateView):
    template_name = "news/index.html"
    form_class = CreateNews

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить публикацию'
        context['name_title_form'] = 'Добавить публикацию'
        context['name_button'] = 'Добавить'
        return context


class NewsUpdate(LoginRequiredMixin, UpdateView):
    template_name = "news/update.html"
    model = News

    fields = ['title', 'content']

    def get_success_url(self):
        return reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование публикации'
        context['name_title_form'] = 'Редактировать публикацию'
        context['name_button'] = 'Редактировать'
        return context


class NewsDetail(DetailView):
    template_name = "news/detail.html"
    model = News
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование публикации'
        context['name_title_form'] = 'Ваша публикация!'
        return context


class NewslineList(ListView):
    template_name = "news/news_line.html"
    model = News
    context_object_name = 'posts'

    extra_context = {'title': 'Статьи'}

