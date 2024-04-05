from django.forms import ModelForm
from .models import *
class CreateSchedulesForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['section', 'date', 'time']