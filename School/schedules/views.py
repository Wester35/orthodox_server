from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from .models import *
from .forms import *
from django.shortcuts import redirect

class SchedulesCreate(LoginRequiredMixin, CreateView):
    template_name = "schedules/index.html"
    form_class = CreateSchedulesForm

    def get_success_url(self):
        return reverse_lazy('main')

    def get(self, request, *args, **kwargs):
        if (self.request.user.rights == 2 or self.request.user.rights == 0):
            return super().get(request, *args, **kwargs)

        return redirect('main')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить публикацию'
        context['name_title_form'] = 'Добавить публикацию'
        context['name_button'] = 'Добавить'
        return context

class ScheduleslineList(ListView):
    template_name = "schedules/schedule_list.html"
    model = Schedule
    context_object_name = 'posts'

    def get_queryset(self):
        return Schedule.objects.all().filter(section=self.kwargs.get('pk'))

    def render_to_response(self, context):
        if(context.get('object_list').exists()):
            return super().render_to_response(context)
        return redirect('main')

    extra_context = {'title': 'Секции'}

class SchedulesDetail(DetailView):
    template_name = "schedules/detail.html"
    model = Schedule
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Публикация'
        context['name_title_form'] = ''
        return context

class SchedulesUpdate(LoginRequiredMixin, UpdateView):
    template_name = "schedules/index.html"
    model = Schedule

    fields = ['name', 'content', 'photo']

    def get_success_url(self):
        return reverse_lazy('main')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if (self.request.user == self.object.author):
            return super().get(request, *args, **kwargs)

        return redirect('main')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Редактирование секции'
        context['name_title_form'] = 'Редактировать секцию'
        context['name_button'] = 'Редактировать'
        return context