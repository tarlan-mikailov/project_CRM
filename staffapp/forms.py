from django import forms
from django.contrib.auth.models import User, Group
from .models import Schedule


class UpdateStaffUserForm(forms.ModelForm):
    group = forms.ModelChoiceField(
        required=True,
        queryset=Group.objects.all(),
        widget=forms.Select(attrs={"class": "form-select"})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control"}),
            'first_name': forms.TextInput(attrs={"class": "form-control"}),
            'last_name': forms.TextInput(attrs={"class": "form-control"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),
        }


class CreateScheduleStaffForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date', "class": "form-control"}),
            'id_staff': forms.Select(attrs={"class": "form-select"}),
            'start_time': forms.TimeInput(attrs={'type': 'time', "class": "form-control"}),
            'end_time': forms.TimeInput(attrs={'type': 'time', "class": "form-control"})
        }


class FilterScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ('date',)

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'date', "class": "form-control"})
        }
