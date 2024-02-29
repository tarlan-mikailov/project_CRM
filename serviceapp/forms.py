from django import forms
from serviceapp import models


class ServiceForm(forms.ModelForm):
    class Meta:
        model = models.Service
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"})
        }


class CreateServiceForm(forms.ModelForm):
    resource = forms.ModelMultipleChoiceField(
        required=False,
        queryset=models.Resource.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = models.Service
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"})
        }


class ResourceForm(forms.ModelForm):
    class Meta:
        model = models.Resource
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"}),
            'amount': forms.NumberInput(attrs={"class": "form-control"}),
        }


class AddResourceForServiceForm(forms.Form):
    resource = forms.ModelMultipleChoiceField(
        queryset=models.Resource.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
