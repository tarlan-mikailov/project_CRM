from django import forms
from django.contrib.auth.models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'last_name')

        widgets = {
            'username': forms.TextInput(attrs={"class": "form-control", 'required': 'required'}),
            'first_name': forms.TextInput(attrs={"class": "form-control", 'required': 'required'}),
            'last_name': forms.TextInput(attrs={"class": "form-control", 'required': 'required'}),
            'email': forms.EmailInput(attrs={"class": "form-control", 'required': 'required'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
